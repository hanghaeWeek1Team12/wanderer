// 좋아요 기능
function toggle_like(placeName,status, email) {
    // 테스트용
    email = "ysong0504@gmail.com"

    if (email == null) {
        alert('로그인을 먼저 해주세요!')
    } else {
        $.ajax({
        type: "POST",
        url: "/like",
        data: {
            placeName_give: placeName,
            email_give: email,
            status_give: status
        },
        success: function (response) {
            window.location.reload()
        }
    })
    }



}