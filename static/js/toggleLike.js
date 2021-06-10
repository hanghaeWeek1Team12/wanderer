// 좋아요 기능
function toggle_like(placeName, status) {
    $.ajax({
        type: "POST",
        url: "/like",
        data: {
            placeName_give: placeName,
            status: status
        },
        success: function (response) {

            if (!response['res']) {
                modalAlert(response['msg']);
            }
            if (response['res']) {
                window.location.reload();
            }
        }
    })
}