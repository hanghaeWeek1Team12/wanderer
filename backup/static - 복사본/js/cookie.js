// 쿠키 저장하기
function setCookie(key, value) {
    var expires = new Date();
    expires.setTime(expires.getTime() + (1 * 24 * 60 * 60 * 1000));
    document.cookie = key + '=' + value + ';expires=' + expires.toUTCString();
}

// 쿠키 가져오기
function getCookie(key) {
    var keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
    return keyValue ? keyValue[2] : null;
}

// 쿠키 삭제하기
function deleteCookie(key) {
    document.cookie = key + '=;expires=Thu, 01 Jan 1970 00:00:00 UTC;';
}

