// 장소를 좋아요 한사람 출력
// main 전용입니다. .modal-window .content
function likedList(placeName) {
    $.ajax({
        type: "POST",
        url: "/likedList",
        data: {
            placeName: placeName
        },
        success: function (response) {
            if (!response['res']) {
                modalAlert(response['msg']);
            }
            if (response['res']) {
                // 모달 창을 비웁니다.
                $('.modal-window .content').empty()
                // 모달 창을 채웁니다.
                for (let res of response['val']) {
                    let line = '<p id = "email-line"><i class="fa fa-heart heart" aria-hidden="true" style="margin-right: 10px"></i>'
                        + res['email'] + '</p>'
                    $('.modal-window .content').append(line)
                }
                // 모달 창을 뛰웁니다.
                $('#modal')[0].style.display = 'flex'
            }
        }
    })
}

