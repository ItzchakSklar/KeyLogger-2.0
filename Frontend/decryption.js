let decryption = (data, code) => {
    decryption_string = ""
    password_number = prompt("Enter password: ")
    arr = arr(data)
    for(i in arr) {
        char = ord(i)
        char = char ^ ord(password_number)
        decryption_char = chr(char)
        decryption_string += str(decryption_char)
    }
    return decryption_string
};