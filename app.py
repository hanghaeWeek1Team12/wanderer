from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests

app = Flask(__name__)
<<<<<<< HEAD
=======
app.config['SECRET_KEY'] = '452325d3c00449738b52eab18c63edf7'
app.config['ALGORITHM'] = 'HS256'

# static url


@app.route('/', methods=["GET"])
def home():
    return render_template('signup.html')


@app.route('/signup', methods=["GET"])
def static_signup():
    return render_template('signup.html')
>>>>>>> d31f3c48e12424cc6e3e3d76d3afe9e3a6aa2239

client = MongoClient('localhost', 27017)
db = client.wanderer

<<<<<<< HEAD
=======
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
>>>>>>> d31f3c48e12424cc6e3e3d76d3afe9e3a6aa2239

# 여행지 리스트 출력
@app.route("/placelist")
def main():
    # 테스트용
    email_receive = "ysong0504@gmail.com"

    # 현재 로그인한 계정이 '좋아요'른 누른 여행지 출력
    if email_receive:
        liked_list = db.place.find({"likedUser": [{"email": email_receive}]},
                                   {'_id': 0, 'placeName': 1})

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


# 좋아요 확인하기
@app.route("/like", methods=['POST'])
def like_place():
    placeName_receive = request.form['placeName_give']
    email_receive = request.form['email_give']
    status_receive = request.form['status_give']

    # 좋아요 취소 (pull을 이용하여 likedUser에서 해당 이메일 제거)
    if status_receive == 'unlike':
        db.place.update({"placeName": placeName_receive},
                            {'$pull': {
                                "likedUser": {"email": email_receive}
                                }
                            }
                        )
    # 좋아요 추가 (push로 likedUser에서 해당 이메일 추가)
    else:
        db.place.update({"placeName": placeName_receive},
                            {'$push': {
                                "likedUser": {"email": email_receive}
                                }
                            }
                        )

<<<<<<< HEAD
    return render_template("main.html")


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)
=======
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

# 이 function은 jwt에서 이메일을 추출합니다.
def get_email_from_jwt(jwt):
    jwt_token = jwt
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


@app.route("/upload", methods=["POST"])

@login_required
def upload():
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



    imgsrc = request.form["imgsrc"]
    placeName = request.form["placeName"]
    loaction = request.form["loaction"]
    uploadedEmail = request.form["uploadedEmail"]

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


if __name__ == "__main__":
    app.run('0.0.0.0', port=8080, debug=True)


diction = {'key': "value"}
array = [diction, diction, diction]

print(array)


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

>>>>>>> d31f3c48e12424cc6e3e3d76d3afe9e3a6aa2239
