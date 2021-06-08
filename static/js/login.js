function login() {
    console.log()
    $.ajax({
        type: "POST",
        url: "http://localhost:8080/login",
        data: {
            email: $('#email').val(),
            password: $('#password').val()
        },
        success:
            function (response) {
                // 로그인에 성공하면
                if (response['res']) {
                    // 메인 페이지로 갑니다.
                    window.location.href = '../main';
                }
                // 회원가입에 실패하면   
                else {
                    alert(response["msg"])
                }
            }
    })
}