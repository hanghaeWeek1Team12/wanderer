// 장소 삭제 기능
function deletePlace(placeName) {
    $.ajax({
        type: "POST",
        url: "/deletePlace",
        data: {
            placeName: placeName
        },
        success: function (response) {

            if (!response['res']) {
                modalAlert(response['msg']);
            }
            if (response['res']) {
                modalAlert(response['msg']);
                window.location.reload();
            }
        }
    })
}