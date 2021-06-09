# wanderer

테스트테스트
아무거나 또친다!! -수임-
또또 쳐본다! -수임2
신난다 신난다. -수임3-



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
            * API call 이 아닙니다. front에서 이뤄지면 됩니다.
            * JWT가 저장된 'jwt' 쿠키의 삭제
            * 기능 = 로그아웃

        * /signup
            * method = post
            * request = {email="", password="", nickname=""}
            * cookie = {}
            * response = {res=True, msg="회원가입 되었습니다.", val=JWT}
            * 기능 = 이메일/닉네임 중복확인, 회원가입

        * /
            * method = get
            * request = {}
            * cookie = {'jwt' : JWT}
            * response = {res=True, msg="", val=[{imgsrc="url", likeCount=3, liked=True, placeName="한라산", location="서울시 영등포구 ..."},{...},{...}]}
            * 기능 = front에 모든 장소를 표기, array val로 받음

        * /upload
            * method = post
            * request = {imgsrc="", placeName = "", loaction = ""}
            * cookie = {'jwt' : JWT}
            * response = {res=True, msg="", val=""}
            * 기능 = 장소를 업로드한다.

        * /like
            * method = post
            * request = {placeName="한라산", status=True}
            * cookie = {'jwt' : JWT}
            * response = {res=True, msg="좋아요가 완료되었습니다." val=""}
            * 기능 = 로그인된 아이디로 장소를 좋아요/좋아요 취소 한다.

    </details>

    * <details>
      <summary>데이터베이스</summary>
        <br>

        * wanderer 
          * user
            * email = str
            * nickname = str
            * password = str
          * place
            * placeName = str
            * imageURL = str
            * location = str
            * likedUser = arr[email = str]
            * createdUser = str

    </details>

    * <details>
      <summary>기능적 요구</summary>
      <br>

      * 여행지 데이터 직접 입력 or scraping   

      * Jinja2에 대한 연구    

        jinja2는 flask에서 html에 변수를 보내주어 사용할 수 있는 plugin입니다.   
        <br>

        파이선 서버에서 변수 보내주기 
        ```python
        return render_template("index.html", var = giveVar)
        ```
        <br>

        html 변수표시는 `{var}` 코드는 `{{code}}`로 한다.   
        <br>

        html if 문
        ```html
        {% if template_variable == "Hello" %}
        <p>{{ template_variable }}, World!</p> 
        {% endif %}
        ```
        <br>

        html if, else if, else 문
        ```html
        {% if template_variable < 20 %}
        <p>{{ template_variable }}은 20보다 작다.</p> 
        {% elif template_variable > 20 %}
        <p>{{ template_variable }}은 20보다 크다.</p> 
        {% else %}
        <p>{{ template_variable }}은 20이다.</p> 
        {% endif %}
        ```
        <br>

        html for 문
        ```
        {% for row in rows %}
        {% set gu_name = row.MSRSTE_NM %}
        {% set gu_mise = row.IDEX_MVL %}
        <li>{{ gu_name }}: {{ gu_mise }}</li>
        {% endfor %}
        ```
        <br>

        dictionary for 문
        ```
        <ul>
        {% for key, value in template_dict.items() %}
        <li>{{ key }} : {{ value }}</li>
        {% endfor%}
        </ul>
        ```
        <br>



      * [JWT에 대한 연구](https://www.youtube.com/watch?v=e-_tsR0hVLQ&t=130s)   

      * [responsive grid에 대한 연구](https://codepen.io/astrotim/pen/WQwqbW)

      </details>
      <br>

 
* ## 협업
    * <details>
      <summary>git</summary>
      <br>

      올리는 방법!   
      ```
      git add .   
      git commit -a -m "수정하신 코드에 대한 내용을 적어주세요"   
      git push origin main
      ```
      
      올리려고 했는데 에러가 나면!   
      ```
      git pull origin main
      ```
      
      중간에 병합 (에디터를 직접 확인하시고)
      ```
      <<<<<<<< HEAD
      
      ===============
      
      >>>>>>>>>> dg9nfiod92huf93js
      ```
      코드가 오류가 나지 않게 병합해주세요!   
      위 특수문자를 모두 삭제하고 코드를 정리하면 됩니다.   

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