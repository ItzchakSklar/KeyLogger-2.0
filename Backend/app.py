from flask import Flask, jsonify, request
from flask_cors import CORS
from pathlib import Path
import os
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/computers/<computer_name>', methods=['POST'])
def file_writer(computer_name):
    def write_to_file(filename, text):
        with open(filename, "a") as file:  # "a" - מצב הוספה
            file.write(text + "\n")
    path =  Path.cwd() /f"data/{computer_name}"
    write_to_file(path,request.data.decode())
    return jsonify({"message": "File updated successfully"}),200

# Get all computers (names) [..,..,..]
@app.route('/api/computers', methods=['GET'])
def get_names():
    try:
        folder_path = "data"
        files = os.listdir(folder_path)  # מחזיר רשימה של כל הקבצים והתיקיות בתיקייה
        return list(files),200
    except:
        return 404
# Get specific computer data
@app.route('/api/computers/<computer_name>', methods=['GET'])
def get_data(computer_name):
    with open(f"data/{computer_name}", "r") as file:
        lines = file.readlines()  # קורא את כל השורות לרשימה
        rew_lines_list = [line.strip() for line in lines]  # מסיר רווחים מיותרים
    def decryption(data, code):
        decryption_string = ""
        password_number = code
        arr = list(data)
        for i in arr:
            char = ord(i)
            char = char ^ ord(password_number)
            decryption_char = chr(char)
            decryption_string += str(decryption_char)
        return decryption_string
    lines_list_nise = list()
    for line in rew_lines_list:
         lines_list_nise.append(decryption(line,"Y"))
    def string_to_dict(list1):
        # מחליף מרכאות כפולות במרכאות יחידות כדי להקל על ה-parsing
        list1 = list1.replace('"', "'")

        # מחפש את כל הזוגות של timestamp ותוכן
        pattern = r"'([^']+)': '([^']*)'"
        matches = re.findall(pattern, list1)

        # יוצר מילון מהתוצאות
        result_dict = {timestamp: content for timestamp, content in matches}
        return result_dict

    for i in range(len(lines_list_nise)):
        lines_list_nise[i] = string_to_dict(lines_list_nise[i])
    one_big_dict = dict()
    for dicts in lines_list_nise:
        for key, value in dicts.items():
            if key not in one_big_dict.keys():
                one_big_dict[key] = value
            else:
                one_big_dict[key] += value
    return one_big_dict

@app.route('/api/computers/<computer_name>/times', methods=['GET'])
def times_of_computers(computer_name):
    return list(get_data(computer_name).keys())

@app.route('/api/computers/<computer_name>/<time>', methods=['GET'])
def time_of_computers(computer_name,time):
    return get_data(computer_name)[time]

if __name__ == '__main__':
    app.run(debug=True)