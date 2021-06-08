from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.wanderer


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

    return render_template("main.html")


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)
