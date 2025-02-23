from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initial computers data
computers = [
    {
        "name": "computer 1",
        "data": "אני איראני 1"
    },
    {
        "name": "computer 2",
        "data": "אני איראני 2"
    },
    {
        "name": "computer 3",
        "data": "אני איראני 3"
    }
]


# Get all computers (name and ID only)
@app.route('/api/computers', methods=['GET'])
def get_computers():
    simplified_computers = [{"name": computer["name"], "data": computer["data"]} for computer in computers]
    return jsonify(simplified_computers)


# Get specific computer details
@app.route('/api/computers/<computer_id>', methods=['GET'])
def get_computer(computer_id):
    computer = next((s for s in computers if s["name"] == computer_id), None)
    if computer:
        return jsonify(computer)
    else:
        return jsonify({"error": "מחשב לא נמצא"}), 404


# Add new computer
@app.route('/api/computers', methods=['POST'])
def add_computer():
    new_computer = request.json

    # Check if computer with this ID already exists
    if any(s["name"] == new_computer["name"] for s in computers):
        return jsonify({"error": "מחשב עם שם זה כבר קיים במערכת"}), 400

    # Add new computer
    computers.append(new_computer)
    return jsonify(new_computer), 201


# Update computer details
@app.route('/api/computers/<computer_name>', methods=['PUT'])
def update_computer(computer_name):
    update_data = request.json
    computer = next((s for s in computers if s["name"] == computer_name), None)

    if not computer:
        return jsonify({"error": "מחשב לא נמצא"}), 404

    # Update computer fields
    if "name" in update_data:
        computer["name"] = update_data["name"]

    return jsonify(computer)


# Add grade to computer
@app.route('/api/computers/<computer_id>/grades', methods=['POST'])
def add_grade(computer_name):
    grade_data = request.json
    computer = next((s for s in computers if s["name"] == computer_name), None)

    if not computer:
        return jsonify({"error": "מחשב לא נמצא"}), 404

    # Add new grade
    computer["grades"].append(grade_data["grade"])
    return jsonify(computer)


if __name__ == '__main__':
    app.run(debug=True)