
$(document).ready(function () {
    $('#modal')[0].style.display = 'none'
})


// 좋아요 리스트 모달 창 열기
function openModal(placeName) {

    // $.ajax({
    //     type: "POST",
    //     url: "/likedlist",
    //     data: {
    //         placeName_give: placeName
    //     },
    //     success: function (response) {
    //         console.log(response[likedUser])
    //         let temp_html = ``
    //     }
    // })

    $('#modal')[0].style.display = 'flex'
}

// 좋아요 리스트 모달 창 닫기
function closeModal() {
    // 옵션1. HTML DOM 객체로 진행
    // const modal = document.getElementById("modal")
    // modal.style.display = 'none'

    //옵션2. 제이쿼리 객체로 진행
    $('#modal')[0].style.display = 'none'

}

// 작은 모달창
function messageModal(msg) {
    $('#modal')[0].style.display = 'none'
}
