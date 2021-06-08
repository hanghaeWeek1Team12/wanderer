// 좋아요 기능
<<<<<<< HEAD:static/js/main.js
function toggle_like(placeName,status, email) {
    // 테스트용
    email = "ysong0504@gmail.com"

    if (email == null) {
        alert('로그인을 먼저 해주세요!')
    } else {
        $.ajax({
=======
function toggle_like(placeName, status) {
    let email = "ysong0504@gmail.com"
    $.ajax({
>>>>>>> d31f3c48e12424cc6e3e3d76d3afe9e3a6aa2239:static/js/toggleLike.js
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
<<<<<<< HEAD:static/js/main.js
    }



}
=======
}
>>>>>>> d31f3c48e12424cc6e3e3d76d3afe9e3a6aa2239:static/js/toggleLike.js
