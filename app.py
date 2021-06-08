
from pymongo import MongoClient
from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
import jwt
import bcrypt
from datetime import timedelta, datetime
import json
from functools import wraps

# mongoDB에서 db로 객체를 받아옵니다.
client = MongoClient('localhost', 27017)
db = client.wanderer

app = Flask(__name__)
app.config['SECRET_KEY'] = '452325d3c00449738b52eab18c63edf7'
app.config['ALGORITHM'] = 'HS256'


# 임의의 패스워드?
password = b"password"
# bcrypt에서 소금을 뿌려줍니다.
salt = bcrypt.gensalt()
# password 와 소금을 이용하여 hashed를 만듭니다.
hashed = bcrypt.hashpw(password, salt)
# 위에 만들어진 hashed가 일치하는지 확인합니다.
if bcrypt.checkpw(password, hashed):
    print("match")
else:
    print("does not match")


# static url

@app.route('/', methods=["GET"])
def home():
    return render_template('signup.html')


@app.route('/signup', methods=["GET"])
def static_signup():
    return render_template('signup.html')


@app.route('/main', methods=["GET"])
def static_main():
    return render_template('main.html')

@app.route('/login', methods=["GET"])
def static_login():
    return render_template('login.html')
# api url

@app.route('/upload', methods=["get"])
def static_upload():
    return render_template('upload.html')

# api url


@app.route("/login", methods=["POST"])
def login():
    credential = request.json
    email = request.form["email"]
    password = request.form["password"]

    # 이메일이 일치하는 db를 가져옵니다.
    db_user = db.user.find_one({'email': email}, {'_id': False})

    #  유니코드를 지원하기 위해 UTF-8을 사용합니다.
    utf_password = password.encode("UTF-8")
    utf_db_password = db_user['password']

    # db_user가 존재하고 bcrypt가 checkPassword를 통과시키면
    if db_user and bcrypt.checkpw(utf_password, utf_db_password):

        user_email = db_user["email"]

        # 헤더는 알아서 만들어집니다.
        # typ 토큰의 타입을 지정
        # alg 알고리즘 방식을 지정 (jwt.encode의 세번째 인자 ALGORITHM)

        # 페이로드를 만듭니다.
        # iss: 토큰 발급자(issuer)
        # sub: 토큰 제목(subject) 보통 이메일을 사용
        # aud: 토큰 대상자(audience)
        # exp: 토큰 만료 시간(expiration), NumericDate 형식으로 되어 있어야 함 ex) 1480849147370
        # nbf: 토큰 활성 날짜(not before), 이 날이 지나기 전의 토큰은 활성화되지 않음
        # iat: 토큰 발급 시간(issued at), 토큰 발급 이후의 경과 시간을 알 수 있음
        # jti: JWT 토큰 식별자(JWT ID), 중복 방지를 위해 사용하며, 일회용 토큰(Access Token) 등에 사용
        # 출처 : https://mangkyu.tistory.com/56
        payload = {
            "sub": user_email,
            "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
        }

        # payload와 우리의 SECRET_KEY를 ALGORITHM을 통해 jwt를 만듭니다.
        token = jwt.encode(
            payload, app.config["SECRET_KEY"], app.config['ALGORITHM'])

        return {'res': True, 'msg': "로그인되었습니다.", 'val': token.decode("UTF-8")}
    else:
        return {'res': False, 'msg': "아이디와 비밀번호를 확인해주세요."}


@app.route("/signup", methods=["POST"])
def sign_up():
    email = request.form["email"]
    nickname = request.form["nickname"]
    password = request.form["password"]

    # db 안에 같은 이메일이 존재하는지 확인
    db_email_match = db.user.find_one({'email': email}, {'_id': False})
    if db_email_match is not None:
        return {'res': False, 'msg': "이미 존재하는 이메일입니다"}

    # db 안에 같은 닉네임이 존재하는지 확인
    db_nick_match = db.user.find_one({'nickname': nickname}, {'_id': False})
    if db_nick_match is not None:
        return {'res': False, 'msg': "이미 존재하는 닉네임입니다"}

    # 다 아닐 경우

    # password를 암호화

    # unicodes must be encoded before hashing
    utf_password = password.encode('UTF-8')
    # 소금간
    new_salt = bcrypt.gensalt()
    # 해쉬 생성
    enc_password = bcrypt.hashpw(utf_password, new_salt)

    # db 안에 입력합니다.
    db.user.insert_one({
        'email': email,
        'nickname': nickname,
        'password': enc_password,
    })

    return {'res': True, 'msg': "회원가입 되었습니다."}


# 이 annotation(@)이 사용되면 body의 jwt를 넣어 보내주세요.
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print("this working?")
        # jwt를 body에서 jwt로 받습니다.
        jwt_token = request.form["jwt"]
        # 토큰을 받았다면
        if jwt_token is not None:
            try:
                # jwt 토큰이 유효한지 확인
                payload = jwt.decode(
                    jwt_token, app.config["SECRET_KEY"], app.config['ALGORITHM'])
                # 유효하지 않다면
            except jwt.InvalidTokenError:
                payload = None

            if payload is None:
                return {'res': False, 'msg': "토큰이 유효하지 않습니다."}

            # def login()에서 페이로드의 sub에 email을 넣었습니다.
            email = payload["sub"]

            # 이어서 이메일이 일치하는지 확인
            # db 안에 같은 닉네임이 존재하는지 확인
            db_email_match = db.user.find_one({'email': email}, {'_id': False})
            if db_email_match is None:
                return {'res': False, 'msg': "토큰이 유효하지 않습니다."}
        else:
            return {'res': False, 'msg': "토큰이 유효하지 않습니다."}
        return f(*args, **kwargs)
    return decorated_function


@app.route("/upload", methods=["POST"])
@login_required
def place_list():
    imageURL_receive = request.form['imageURL_give'],
    placeName_receive = request.form['placeName_give'],
    location_receive = request.form['location_give']

    doc = {
        'imageURL': imageURL_receive,
        'placeName': placeName_receive,
        'location': location_receive
    }

    db.wanderer.insert_one(doc)
    return jsonify({'msg': '여행지가 성공적으로 업로드되었습니다.'})


if __name__ == "__main__":
    app.run('0.0.0.0', port=8080, debug=True)

diction = {'key': "value"}
array = [diction, diction, diction]

print(array)
