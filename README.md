# wanderer

팀원 : 최수임, 윤송, 김도형   
작업공간 : 게더타운

테스트테스트   
아무거나 또친다!! -수임-   
또또 쳐본다! -수임2   
신난다 신난다. -수임3-   
첫 깃의 발자취는 삭제하지 않습니다 ㅋㅋ


* ## 결과
    * [프로젝트 링크](http://www.wanderer99.com/)   
    * [유튜브 링크](https://www.youtube.com/watch?v=3KDOiHmCx-g&t=43s)
      <br>

* ## Project
    * <details>
      <summary>아아디어</summary>
      <br>

      간단한 여행지 좋아요 사이트입니다.   
      정해진 여행지 목록에서 좋아요를 누르고   
      다른 사람들은 얼마나 좋아하는지 알아볼 수 있습니다.   
      아이디어와 전체적인 기획을 짜는데 하루 정도의 시간이 주어졌습니다.      
      식단 공유 플랫폼/취직 종합 플랫폼/여행지 플랫폼이 후보로 나왔었습니다.   
      4일간의 프로젝트 기간, 아이디어의 난이도를 고려하며 의견을 종합하여   
      결과적으로 여행지 공유 사이트를 구현하게 되었습니다.   
      </details>
      <br>

    * <details>
      <summary>기능</summary>
      <br>

      * 로그인/로그아웃(JWT)
      * 회원가입
      * 사진 url/장소 위치/장소명 저장
      * 회원/타 회원 좋아요 페이지
      * 좋아요 리스트
      * 커스텀 alert 창
      * 모바일 반응형 페이지   
      * Server Side Rendering
      
      </details>
      <br>
        
    * <details>
      <summary>파일구조</summary>
      <br>

      단일한 static html을 사용하는 것은 복잡성과 읽는데 시간을 너무 많이   
      소모되게 만듭니다. 더 좋고 깔끔한 구조를 위해 노력했습니다.   
      ["프로그램을 읽고 쓰는 비율은 확실히 10 대 1을 넘는다."](https://www.goodreads.com/quotes/835238-indeed-the-ratio-of-time-spent-reading-versus-writing-is)
      
      * static
        * img
        * js
          * *.js
        * styles
          * *.css
      * templates   
        * *.html
      * app.py   
      * installer.sh  
      </details>
      <br>

* ## Frontend
    * <details>
      <summary>디자인</summary>
      <br>
      
      더 기능을 추가하거나 작성을 하며 디자인이 많이 바뀌었지만   
      그럼에도 와이어프레임은 좋은 기준이 되었습니다.   
      
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
    
    * <details>
      <summary>반응형</summary>
      <br>

      [responsive grid에 대한 연구](https://codepen.io/astrotim/pen/WQwqbW)   
      [드랍다운에 대한 연구](https://www.w3schools.com/css/css_dropdowns.asp)
      </details>
      <br>
        
    * <details>
      <summary>Jinja2</summary>
      <br>
        
      * SSR
        * 항해99의 요구사항 중 Server Side Rendering이 있었습니다.   
          Flask의 Jinja2를 사용하여 html이 미리 적용된 상태로 주어집니다.   
          저희는 주로 main 페이지의 이미지를 정렬하고 나열하는데 사용하였습니다.   
          ```
          {# jinja2를 이용하여 좋아요 기준 내림차순 출력#}
          {% for placelist in lists | sort(attribute='liked_count', reverse = True) %}
          ...
          ```
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

          클라이언트가 항상 평균적인 성능을 갖지 않습니다.    
          스마트폰마다의 성능도 각기 다릅니다.   
          그럼으로 클라이언트에서 일정한 속도가 나오지 않습니다.   
          
          서버 사이드 렌더링은 backend 측에서 request에서 받은 정보로    
          완성된 html을 출력하기에 일정한 속도가 약속될 수 있습니다.
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
            * response = {res=True, msg="회원가입 되었습니다."}
            * 기능 = 이메일/닉네임 중복확인, 이메일 유효성 확인, 회원가입
            * response = {res=True, msg="회원가입 되었습니다.", val=JWT}
            * 기능 = 이메일/닉네임 중복확인, 회원가입

        * /upload
            * method = post
            * request = {imgsrc="", placeName = "", loaction = ""}
            * cookie = {'jwt' : JWT}
            * response = {res=True, msg="업로드가 완료되었습니다."}
            * 기능 = 장소를 업로드한다.

        * /deletePlace
            * method = post
            * request = {placeName=""}
            * cookie = {'jwt' : JWT}
            * response = {res=True, msg="삭제가 완료되었습니다."}
            * 기능 = 장소를 삭제합니다.

        * /like
            * method = post
            * request = {placeName="한라산", status=True}
            * cookie = {'jwt' : JWT}
            * response = {res=True, msg="좋아요를 완료/취소되었습니다."}
            * 기능 = 로그인된 아이디로 장소를 좋아요/좋아요 취소 한다.
    </details>
    <br>
    
    * <details>
      <summary>페이지 설계</summary>
        <br>

        * /
            * method = get
            * request = {}  
            * cookie = {'jwt' : JWT}
            * responst = main.html
            * 기능 = jwt가 있을 경우 사용자가 만들거나 좋아한 장소를 나타냅니다.
              
        * /mypage
            * method = get
            * request = {email_give=""}  
            * cookie = {'jwt' : JWT}
            * responst = main.html
            * 기능 = 주어진 이메일의 회원이 좋아한 장소를 나타냅니다.

        * /signup
            * method = get
            * request = {}  
            * cookie = {}
            * responst = signup.html
            * 기능 = 회원가입 페이지
        
        * /login
            * method = get
            * request = {}  
            * cookie = {}
            * responst = login.html
            * 기능 = 로그인 페이지
        
        * /upload
            * method = get
            * request = {}  
            * cookie = {}
            * responst = upload.html
            * 기능 = 업로드 페이지
   
        * /likedList
            * method = post
            * request = {placeName="한라산", status=True}
            * cookie = {'jwt' : JWT}
            * response = {res=True, msg="해당 장소를 좋아요 한사람들이 출력됩니다.", 'val': likedUser['likedUser']}
            * 기능 = 특정 게시물의 '좋아요'를 누른 유저들의 리스트 출력
    </details>
    <br>

    * <details>
      <summary>데이터베이스</summary>
        <br>

        * wanderer 
          * user
            * email = str
            * nickname = str
            * password = binary
          * place
            * placeName = str
            * imageURL = str
            * location = str
            * likedUser = arr[email = str]
            * createdUser = str
    </details>
    <br>

    * <details>
      <summary>Bcrypt</summary>  
      <br>

      ## Bcrypt
      우선 bcrypt에 대하여 이해합시다.   
      bcrypt은 단순한 암호화 모듈입니다.   
      ```python
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
      ```
      위 코드에서   
      `password`는 사용자의 암호   

      `salt`는 bcrypt에서 만들어주는 임의의 값입니다.   
      코드가 실행 될 때마다 `bcrypt.gensalt()`가 불러지기에 항상 `salt` 값은 다릅니다.    

      `hashed`는 위의 `password`와 `salt`를 이용해서 암호화 된 값입니다.   
      이 `hashed`값 또한 `salt`값이 변동적이기에 만들 때마다 다르게 나옵니다.    

      `hashed` 값이 항상 다름에도 불구하고 `checkpw`를 사용하면 `hashed`가 `password`에서   
      유래하였는지 확인이 가능하다.   

      여기에서 중요한 점은 `유래`의 `일치`를 확인 가능하다는 점입니다.   
      즉 `파생`되었는지만 확인이 가능하지 `hashed`를 통해 `password` 자체를    
      알아내는 것은 불가하다는 점이 중요합니다.   

      그럼 `salt`도 없는데 도대체 어떻게 그걸 알아요?   
      `salt`는 `hashed`의 값 내에 암호화되어 저장됩니다.(첫 20자 정도)    
      bcrypt는 그래서 `hashed` 값 만으로 그 `파생` 여부를 파악할 수 있습니다.   

      bcrypt는 언어와 상관 없이 다 통상적으로 사용되니 이해하시면 편합니다.   
      </details>
      <br>
    
    * <details>
      <summary>JWT</summary>
      <br>

      ## JWT

      * [JWT에 대한 연구](https://www.youtube.com/watch?v=e-_tsR0hVLQ&t=130s)
      * [JWT에 대한 연구2](https://zzsza.github.io/development/2019/03/04/auth-with-flask/)
      * [JWT의 구조가 잘 설명된 곳](https://mangkyu.tistory.com/56)   
      <br>

      저희의 경우 2번째 블로그를 많이 참고 하였습니다.   

      JWT의 경우 회원 로그인이 완료되면 front에 보내는 토큰입니다.   
      JWT는 header,payload,signature로 이루어져 있습니다.   

      위의 3번째 링크에서 더 정확한 확인이 가능하니 여기에서는 간략하게 요약해드리면   
      header는 토큰의 정의, payload는 토큰의 내용, signature는 토큰의 암호입니다.   

      저희가 사용한 `import jwt`의 경우 header와 signature는 자동으로 생성합니다.   
      그럼으로 payload만 정의하면 됩니다.   

      또한 jwt를 만들기 위해서 SECRET KEY와 ALGORITHM도 줘야 합니다.   
      app 내부에 정의합시다.   
      ```python
      app = Flask(__name__)
      app.config['SECRET_KEY'] = '452325d3c00449738b52eab18c63edf7'
      app.config['ALGORITHM'] = 'HS256'
      ```
 
      그래서    
      ```python
      payload = {
            "sub": user_email,
            "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
      }

      # payload와 우리의 SECRET_KEY를 ALGORITHM을 통해 jwt를 만듭니다.
      token = jwt.encode(payload, app.config["SECRET_KEY"], app.config['ALGORITHM'])
      return {"res":token}
      ```
      간단하죠?   

      마지막으로 토큰을 받아서 유효성을 따지려면
      ```python
      # jwt 토큰이 유효한지 확인   
      payload = jwt.decode(recieved_token, app.config["SECRET_KEY"], app.config['ALGORITHM'])
      # 유효하지 않으면 payload는 None으로 나옵니다.
      ```   

      위에서 `payload`에서 저장한 `sub`, `exp`도 받을 수 있습니다. 
      ```python
      payload["sub"]
      payload["exp"]
      ```

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

* ## 설치
    * <details>
      <summary>AWS</summary>
      <br>

      리눅스 EC2를 구매하고 security group를 지정하세요!   
      [스파르타 코딩클럽 웹종합 5-12 참고](https://online.spartacodingclub.kr/enrolleds/60801f9e63d7a131f468ee6b/edetails/60801f9e63d7a131f468eeb4)   

      wanderer 파일을 zip 하기 이전에 app.py의 app을 서버용 객체로 지정해주세요!   
      `client = MongoClient('mongodb://test:test@localhost', 27017)`   

      wanderer의 zip 파일을 EC2에 넣어주세요!    

      코드   
      `sudo su`   
      `chmod ugo+rwx installer.sh`   
      `./installer.sh`   
      `nohup python app.py &`    

      pip 파일들 설치는 sh에 추가했습니다.   
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
