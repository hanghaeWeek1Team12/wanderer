# wanderer


* ## API 설계
    * /login   
        * method = post
        * request = {email="", password=""}
        * response = {res=True, msg="로그인 되었습니다.", val=JWT}
        * 기능 = 비밀번호, 이메일 확인, 로그인

    * /logout
        * method = post
        * jwt를 연구하고 구현 or 프런트에서 해결
        * 기능 = 로그아웃

    * /signup
        * method = post
        * request = {email="", password="", nickname=""}
        * response = {res=True, msg="회원가입 되었습니다.", val=JWT}
        * 기능 = 이메일/닉네임 중복확인, 회원가입

    * /placelist
        * method = get
        * request = {email=""}
        * response = {res=True, msg="", val=[{imgsrc="url", likeCount=3, liked=True, placeName="한라산", location="서울시 영등포구 ..."},{...},{...}]}
        * 기능 = front에 모든 장소를 표기, array val로 받음

    * /upload
        * method = post
        * request = {imgsrc="", placeName = "", loaction = ""}
        * response = {res=True, msg="", val=""}
        * 기능 = 장소를 업로드한다.

    * /like
        * method = post
        * request = {placeName="한라산", email=""}
        * response = {res=True, msg="좋아요가 완료되었습니다." val=""}
        * 기능 = place 데이터베이스에 해당 이메일이 존재한다면 like를 하고 존재하지 않는다면 unlike를 한다. 로그인된 아이디로 장소를 좋아요/좋아요 취소 한다.

    

* ### 그외 필요한 것    
    * 여행지 데이터 직접 입력 or scraping
 