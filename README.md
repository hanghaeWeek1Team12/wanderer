# wanderer

* ## Project
    * <details>
      <summary>설명</summary>
      <br>

      간단한 여행지 좋아요 사이트입니다.   
      정해진 여행지 목록에서 좋아요를 누르고   
      다른 사람들은 얼마나 좋아하는지 알아볼 수 있습니다.   
      
      
      </details>
      <br>

* ## Frontend
    * <details>
      <summary>Wireframe</summary>
      <br>

      로그인 페이지   

      ![](img/login_template.png)

      회원가입 페이지   

      ![](img/register_template.png)

      업로드 페이지   

      ![](img/upload_template.png)

      메인 페이지   

      ![](img/main_template.png)
      </details>
      <br>
    


* ## Backend
    * <details>
      <summary>API 설계</summary>
        <br>

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

    </details>

    * <details>
      <summary>기능적 요구</summary>
      <br>

      여행지 데이터 직접 입력 or scraping   

      Jinja2에 대한 연구   

      JWT에 대한 연구   

      responsive grid에 대한 연구   

      </details>
      <br>

 
* ## 협업
    * <details>
      <summary>git</summary>
      <br>

      깃헙에는 branch 라는 개념이 있습니다.   
      각자 수정하신 내용을 따로 commit(업로드) 하는 곳이 branch 입니다.   
      Branch 를 원래 master branch에 업로드 하고 싶으시다면   
      pull request를 해야 합니다.   

      branch 생성하기
      ```
      git checkout -b 브랜치명
      ```

      자신의 branch 에 커밋하기
      ```
      git add .
      git commit -m "html 그리드를 수정"
      git push origin 브린치명
      ```
      
      자신의 branch를 master에 병합 요청
      ```
      
      ```
      </details>


<br>
<br>

드랍다운 예시
```
<br>
<details>
<summary>드랍다운</summary>
<br>

드랍다운 내용
</details>
<br>
```