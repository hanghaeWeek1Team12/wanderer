// 사진 삭제 기능
function deleteImage(placeName) {
    $.ajax({
        type: "POST",
        url: "/deletePlace",
        data: {
            placeName: placeName
        },
        success: function (response) {

            if (!response['res']) {
                alert(response['msg']);
            }
            if (response['res']) {
                alert(response['msg']);
                window.location.reload();
            }
        }
    })
}