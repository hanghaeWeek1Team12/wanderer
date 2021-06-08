function upload() {
    console.log()
    $.ajax({
        type: "POST",
        url: "http://localhost:8080/upload",
        data: {
            imageURL: $('#imageURL').val(),
            placeName: $('#placeName').val(),
            location: $('#location').val()
        },
        success:
            function (response) {
                // 업로드에 성공하면
                if (response['res']) {
                    // 메인 페이지로 갑니다.
                    window.location.href = '../main';
                }
                // 업로드에 실패하면
                else {
                    alert(response["msg"])
                }
            }
    })
}