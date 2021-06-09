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


# jwt
# 이 annotation(@)이 사용되면 쿠키에 jwt를 확인해주세요
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # jwt를 쿠키에서 jwt로 받습니다.
        jwt_token = request.cookies.get("jwt")
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


# 이 function은 jwt에서 이메일을 추출합니다.
# return = '' / 'email@web.com'
def get_email_from_jwt(jwt_token):
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
            return ''

        # def login()에서 페이로드의 sub에 email을 넣었습니다.
        email = payload["sub"]
        return email


# static url
@app.route('/', methods=["GET"])
def static_home():
    jwt = request.cookies.get('jwt')

    email_receive = get_email_from_jwt(jwt)

    # 현재 로그인한 계정이 '좋아요'른 누른 여행지 출력
    if email_receive != None or email_receive != '':
        liked_list = db.place.find({"likedUser": [{"email": email_receive}]}, {
                                   '_id': 0, 'placeName': 1})

    # 여행지별 좋아요 갯수 출력
    like_count = list(db.place.aggregate([
        {
            '$project': {
                '_id': 0,
                'placeName': 1,
                'totalCount': {'$size': ['$likedUser']}
            }
        }
    ]))

    # 여행지 리스트 출력
    lists = list(db.place.find({}, {'_id': False}))

    return render_template("main.html", lists=lists, liked_list=liked_list, like_count=like_count)


@app.route('/signup', methods=["GET"])
def static_signup():
    return render_template('signup.html')


@app.route('/login', methods=["GET"])
def static_login():
    return render_template('login.html')


@app.route('/upload', methods=["GET"])
@login_required
def static_upload():
    return render_template('upload.html')


# api url
@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    # 이메일이 일치하는 db를 가져옵니다.
    db_user = db.user.find_one({'email': email}, {'_id': False})

    if db_user is None:
        return {'res': False, 'msg': "아이디와 비밀번호를 확인해주세요."}

    #  유니코드를 지원하기 위해 UTF-8을 사용합니다.
    utf_password = password.encode("UTF-8")
    utf_db_password = db_user['password']

    # db_user가 존재하고 bcrypt가 checkPassword를 통과시키면
    if bcrypt.checkpw(utf_password, utf_db_password):
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

        if type(token) == bytes:
            return {'res': True, 'msg': "로그인되었습니다.", 'val': token.decode("UTF-8")}
        elif type(token) == str:
            return {'res': True, 'msg': "로그인되었습니다.", 'val': token}

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


# 좋아요 확인하기
@app.route("/like", methods=['POST'])
def like_place():
    # cookie 'jwt'에서 이메일 받기
    jwt = request.cookies.get('jwt')
    email_receive = get_email_from_jwt(jwt)
    # 이메일을 받지 못하였다면
    if email_receive == '' or email_receive == None:
        return {'res': False, 'msg': "로그인되어있지 않습니다."}

    # post body 받기
    placeName_receive = request.form['placeName_give']
    status = request.form['status']

    # 좋아요 취소 (pull을 이용하여 likedUser에서 해당 이메일 제거)
    if status == 'unlike':
        db.place.update_one({"placeName": placeName_receive},
                            {'$pull': {
                                "likedUser": {"email": email_receive}
                            }
        }
        )
        return {'res': True, 'msg': "좋아요를 취소하셨습니다."}
    # 좋아요 추가 (push로 likedUser에서 해당 이메일 추가)
    else:
        db.place.update_one({"placeName": placeName_receive},
                            {'$push': {
                                "likedUser": {"email": email_receive}
                            }
        }
        )
        return {'res': True, 'msg': "좋아요가 완료되었습니다."}


@app.route("/upload", methods=["POST"])
@login_required
def upload():
    imgsrc = request.form["imgsrc"]
    placeName = request.form["placeName"]
    loaction = request.form["loaction"]
    jwt = request.cookies.get("jwt")
    email = get_email_from_jwt(jwt)

    if (imgsrc == ''):
        return {'res': False, 'msg': "이미지 url을 입력해주세요."}
    if (placeName == ''):
        return {'res': False, 'msg': "장소 명칭을 입력해주세요."}
    if (loaction == ''):
        return {'res': False, 'msg': "장소 위치를 입력해주세요."}
    if (jwt == '' or jwt == None or email == '' or email == None):
        return {'res': False, 'msg': "다시 로그인해주세요."}
    #
    saved_place = db.place.find_one({'placeName': placeName}, {'_id': False})
    print(saved_place)
    if (saved_place != None):
        return {'res': False, 'msg': "같은 장소가 이미 존재합니다."}

    # db 안에 입력합니다.
    db.place.insert_one({
        'placeName': placeName,
        'imageURL': imgsrc,
        'location': loaction,
        'likedUser': [],
        'createdUser': email
    })
    return {'res': True, 'msg': "업로드가 완료되었습니다."}


@app.route("/deletePlace", methods=["POST"])
@login_required
def delete_place():
    placeName = request.form["placeName"]
    jwt = request.cookies.get("jwt")

    saved_place = db.place.find_one({'placeName': placeName}, {'_id': False})

    # 이메일이 일치하지 않는다면
    if saved_place['createdUser'] != get_email_from_jwt(jwt):
        return {'res': True, 'msg': "생성자가 아닙니다."}

    # 이메일이 일치한다면
    db.place.delete_one({'placeName': placeName})
    return {'res': True, 'msg': "삭제가 완료되었습니다."}


if __name__ == "__main__":
    app.run('0.0.0.0', port=8080, debug=True)


# 연습장
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
