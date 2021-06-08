function login() {
    $.ajax({
        type: "POST",
        url: "http://localhost:8080/login",
        data: {
            email: "dohyung97022@tester.com",
            password: "9999",
            nickname: "kimdoe"
        },
        success:
            function (response) {
                console.log(response)
                const jwt = response['val']
                placelist(jwt)
            }
    })
}

function placelist(jwt) {
    $.ajax({
        type: "POST",
        url: "http://localhost:8080/placelist",
        data: {
            jwt: jwt
        },
        success:
            function (response) {
                console.log(response)
            }
    })
}

login()



// dohyung97022@gmail.com
// password 3851

// dohyung97022@tester.com
// password 9999