function upload() {
    $.ajax({
        type: "POST",
        url: "/upload",
        data: {
            imgsrc: $('#imgsrc').val(),
            placeName: $('#placeName').val(),
            loaction: $('#location').val(),
            jwt: getCookie('jwt')
        },
        success:
            function (response) {
                // 업로드에 성공하면 성공하면
                if (response['res']) {
                    // '업로드에 성공하였습니다.' 메세지 후 창 새로고침
                    alert(response["msg"]);
                    window.location.reload();
                }
                // 업로드에 실패하면   
                else {
                    alert(response["msg"])
                }
            }
    })
}