import { getCookie } from './cookie.js';

function upload() {
    $.ajax({
        type: "POST",
        url: "/upload",
        data: {
            imgsrc: $('#imgsrc').val(),
            placeName: $('#placeName').val(),
            loaction: $('#loaction').val(),
            jwt: getCookie('jwt')
        },
        success:
            function (response) {
                // 업로드에 성공하면 성공하면
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