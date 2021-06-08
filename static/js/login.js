function login() {
    console.log()
    $.ajax({
        type: "POST",
        url: "/login",
        data: {
            email: $('#email').val(),
            password: $('#password').val()
        },
        success:
            function (response) {
                // 로그인에 성공하면
                if (response['res']) {
                    // 쿠키에 jwt를 저장합니다.
                    setCookie("jwt", response['val']);
                    // 메인페이지로 들어갑니다.
                    window.location.href = '../main';
                }
                // 로그인에 실패하면   
                else {
                    alert(response["msg"])
                }
            }
    })
}