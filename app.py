
from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
import jwt
import bcrypt


app = Flask(__name__)


app.config['SECRET_KEY'] = '452325d3c00449738b52eab18c63edf7'
app.config['ALGORITHM'] = 'HS256'
# how to get a secret key

# UUID Approach
# import uuid
# uuid.uuid4().hex


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


@app.route('/')
def home():
    return


@app.route("/login", methods=["POST"])
def login():
    credential = request.json
    email = request.form["email"]
    password = request.form["password"]

    # 패스워드를 해슁해서 저장하는 꼴
    row = app.database.execute(text("""
          SELECT
              id,
              hashed_password
          FROM users
          WHERE email = :email
      """), {'email': email}).fetchone()

    if row and bcrypt.checkpw(password.encode("UTF-8"), row["hashed_password"].encode("UTF-8")):
        user_id = row["id"]
        payload = {
            "user_id": user_id,
            "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
        }

        token = jwt.encode(payload, app.config["JWT_SECRET_KEY"], "HS256")

        return jsonify({
            "access_token": token.decode("UTF-8")
        })
    else:
        return '', 401


if __name__ == "__main__":
    app.run(debug=True)
