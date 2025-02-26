"""
    פונקציה המיועדת לסוכן החשאי שיפתח את הקובץ האמצעות הקוד והסיסמא שקיבל.
    יכול להיות שכבר לא צריך לאחר שהובן שאין צורך בכתיבה לקובץ.
"""
def decrypt(path, code):
    with open(path, "r") as file:
        data = file.read()
    decryption_string = ""
    password_number = code
    arr = list(data)
    for i in arr:
        char = ord(i)
        char = char ^ ord(password_number)
        decryption_char = chr(char)
        decryption_string += str(decryption_char)
    return decryption_string
print(decrypt("DALandau", "Y").replace("}S{", "}\n{"))