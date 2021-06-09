// 로그인 확인하기
// .header #dropdown-content
function loginCheck() {
    var keyValue = document.cookie.match('(^|;) ?jwt=([^;]*)(;|$)');
    keyValue = keyValue ? keyValue[2] : null;
    // 로그아웃된 경우
    if (keyValue == '' || keyValue == null) {
        const needLogin =
            `<button type="button" class="btn btn-light" id="login" onclick="toPath('/login')">로그인</button>
            <button type="button" class="btn btn-light" id="signup" onclick="toPath('/signup')">회원가입</button>`
        $('.header').append(needLogin)

        const needLoginPopup =
            `<button type="button" class="btn btn-light hidden"><i class="fas fa-caret-down"></i></button>
            <button type="button" class="btn btn-light hidden"><i class="fas fa-caret-down"></i></button>`
        $('#dropdown-content').append(needLoginPopup)
    }
    // 로그인된 경우
    else {
        const needLogout =
            `<button type="button" class="btn btn-light" id="login" onclick="deleteCookie('jwt'); toPath('/')">로그아웃</button>
            <button type="button" class="btn btn-light" id="upload" onclick="toPath('/upload')">
                <i class="fas fa-camera-retro"></i>
            </button>`
        $('.header').append(needLogout)

        const needLogoutPopup =
            `<button type="button" class="btn btn-light hidden" onclick="toPath('/upload')"><i class="fas fa-camera-retro fa-sm"></i></button>
            <button type="button" class="btn btn-light hidden" onclick="deleteCookie('jwt'); toPath('/')"><i class="fas fa-door-open fa-sm"></i></button>`
        $('#dropdown-content').append(needLogoutPopup)
    }
}

if (document.readyState === 'complete') {
    loginCheck()
}

$(document).ready(function () {
    loginCheck()
});