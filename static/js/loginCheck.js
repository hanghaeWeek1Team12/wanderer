// 로그인 확인하기
function loginCheck() {
    var keyValue = document.cookie.match('(^|;) ?jwt=([^;]*)(;|$)');
    keyValue = keyValue ? keyValue[2] : null;
    // 로그아웃된 경우
    if (keyValue == '' || keyValue == null) {
        const needLogin =
            `<button type="button" class="btn btn-light" id="login" onclick="toPath('/login')">로그인</button>
            <button type="button" class="btn btn-light" id="signup" onclick="toPath('/signup')">회원가입</button>`
        $('.header').append(needLogin)
    }
    // 로그인된 경우
    else {
        const needLogout =
            `<button type="button" class="btn btn-light" id="login" onclick="deleteCookie('jwt'); toPath('/')">로그아웃</button>
            <button type="button" class="btn btn-light" id="upload" onclick="toPath('/upload')">
                <i class="fas fa-camera-retro"></i>
            </button>`
        $('.header').append(needLogout)
    }
}

loginCheck()