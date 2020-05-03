function notEmpty(username, password) {
    return username != "" && password != ""
}

function checkUsername(username) {
    arr = username.split("@")
    if (arr.length == 2) {
        domain = arr[1].split(".")
        if (domain.length == 2) {
            return true
        }
    }
    return false
}

function checkPassword(password) {
    if (password.length < 6) {
        return false
    }
    upper = false
    lower = false
    number = false
    symbol = false
    for (let i = 0; i < password.length; i++) {
        code = password.charCodeAt(i)
        if (code >= 65 && code <= 90) {
            upper = true
        } else if (code >= 97 && code <= 122) {
            lower = true
        } else if (code >= 48 && code <= 57) {
            number = true
        } else {
            symbol = true
        }
    }
    return upper && lower && number && symbol
}
