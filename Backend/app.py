from flask import Flask, jsonify,request
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/computers/<computer_name>', methods=['POST'])
def file_writer(computer_name):
    def write_to_file(filename, text):
        with open(filename, "a") as file:  # "a" - מצב הוספה
            file.write(text + "\n")
    path =  Path.cwd() /f"data/{computer_name}.txt"
    write_to_file(path,request)


if __name__ == '__main__':
    app.run(debug=True)