function signup() {
    $.ajax({
        type: "POST",
        url: "/signup",
        data: {
            email: $('#email').val(),
            password: $('#password').val(),
            nickname: $('#nickName').val()
        },
        success:
            function (response) {
                // 회원가입에 성공하면
                if (response['res']) {
                    // 로그인 페이지로 갑니다.
                    window.location.href = '../login';
                }
                // 회원가입에 실패하면   
                else {
                    alert(response["msg"])
                }
            }
    })
}