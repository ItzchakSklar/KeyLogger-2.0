from flask import Flask, jsonify, request
from flask_cors import CORS
from pathlib import Path
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/computers/<computer_name>', methods=['POST'])
def file_writer(computer_name):
    def write_to_file(filename, text):
        with open(filename, "a") as file:  # "a" - מצב הוספה
            file.write(text + "\n")
    path =  Path.cwd() /f"data/{computer_name}.txt"
    write_to_file(path,request.data.decode())

# Get all computers (names) [..,..,..]
@app.route('/api/computers', methods=['GET'])
def getnames():
    folder_path = "data"  # יש לשנות לנתיב הרצוי
    files = os.listdir(folder_path)  # מחזיר רשימה של כל הקבצים והתיקיות בתיקייה
    return files

# Get specific computer data
@app.route('/api/computers/<computer_name>', methods=['GET'])
def getdata(computer_name):
    with open(f"data/{computer_name}", "r") as file:
        data = file.read()
    def decryption(data, code):
        decryption_string = ""
        password_number = input("Enter password: ")
        arr = list(data)
        for i in arr:
            char = ord(i)
            char = char ^ ord(password_number)
            decryption_char = chr(char)
            decryption_string += str(decryption_char)

        return decryption_string
    return decryption(data,"Y")

if __name__ == '__main__':
    app.run(debug=True)