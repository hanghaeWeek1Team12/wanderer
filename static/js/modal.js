
// 모달 창 열기
function openModal() {
    // msg 모달창은 modalAlert로만 열립니다.
    $('#modal')[0].style.display = 'flex'
}

// 모달 창 닫기
function closeModal() {
    $('#modal')[0].style.display = 'none';
}

function closeMsgModal() {
    $('#msg-modal')[0].style.display = 'none';
}

// 모달창 뛰우기
// 메시지 모달창 #msg-modal .modal-window .content 가 있어야 합니다.
function modalAlert(msg) {
    // none -> flex
    $('#msg-modal')[0].style.display = 'flex';
    // 텍스트를 바꿉니다.
    $('#msg-modal .modal-window .content').html(msg);
}