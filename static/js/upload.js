function upload() {
    $.ajax({
        type: "POST",
        url: "/upload",
        data: {
            imgsrc: $('#imgsrc').val(),
            placeName: $('#placeName').val(),
            loaction: $('#location').val()
        },
        success:
            function (response) {
                // 업로드에 성공하면 성공하면
                if (response['res']) {
                    // '업로드에 성공하였습니다.' 메세지 후 창 새로고침
                    modalAlert(response["msg"]);
                    window.location.href = '/'
                }
                // 업로드에 실패하면   
                else {
                    modalAlert(response["msg"])
                }
            }
    })
}