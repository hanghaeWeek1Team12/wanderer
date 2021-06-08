// 로고를 누르면 메인으로 갑니다.
// 반드시 <p class="biglogo" onclick="logoToMain()"> 를 추가해주세요!
function logoToMain() {
    var pathName = window.location.pathname;

    if (pathName == '/') {
        window.location.reload();
    } else {
        window.location.href = '../';
    }
}

