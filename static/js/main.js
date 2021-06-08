// 좋아요 기능
function toggle_like(placeName,status) {
    let email = "ysong0504@gmail.com"
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