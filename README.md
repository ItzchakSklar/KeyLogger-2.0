# KeyLogger-2.0

## Description
KeyLogger-2.0 is a Python-based keylogger that captures keystrokes, encrypts the data, and writes it to a file or sends it to a server. It is designed for educational purposes and should be used responsibly.

## Features
- Captures keystrokes
- Encrypts captured data using XOR encryption
- Writes encrypted data to a file or sends it to a server
- Periodically resets and writes data to a dictionary

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ItzchakSklar/KeyLogger-2.0.git
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
1. Run the manager.py script to start the keylogger:
    ```sh
    python manager.py
    ```
2. The keylogger will start capturing keystrokes and writing encrypted data to the specified file or sending it to the server.

## KeyLoggerAgent

### Classes

#### [IWriter](https://github.com/ItzchakSklar/KeyLogger-2.0/blob/main/KeyLoggerAgent/writer.py)
An abstract base class for writers with a [write](https://github.com/ItzchakSklar/KeyLogger-2.0/blob/main/KeyLoggerAgent/writer.py) method that must be implemented by subclasses.

#### [DictWriter](https://github.com/ItzchakSklar/KeyLogger-2.0/blob/main/KeyLoggerAgent/writer.py)
A class that writes data to a dictionary, with minutes as keys and text as values.
- **Methods:**
  - [write(data: list) -> None](https://github.com/ItzchakSklar/KeyLogger-2.0/blob/main/KeyLoggerAgent/writer.py): Writes the given list of characters to the dictionary.
  - [get_dict() -> dict](https://github.com/ItzchakSklar/KeyLogger-2.0/blob/main/KeyLoggerAgent/writer.py): Resets the dictionary and returns the last dictionary.
  - `cur_min() -> str`: Returns the current minute as a string.

#### [FileWriter](https://github.com/ItzchakSklar/KeyLogger-2.0/blob/main/KeyLoggerAgent/writer.py)
A class that writes data to a text file.
- **Methods:**
  - [write(data: str) -> None](https://github.com/ItzchakSklar/KeyLogger-2.0/blob/main/KeyLoggerAgent/writer.py): Writes the given string to the file.

#### [NetworkWriter](https://github.com/ItzchakSklar/KeyLogger-2.0/blob/main/KeyLoggerAgent/writer.py)
A class that sends data to a server.
- **Methods:**
  - [write(data: str) -> None](https://github.com/ItzchakSklar/KeyLogger-2.0/blob/main/KeyLoggerAgent/writer.py): Sends the given string to the server.

## Server Side
The server side is implemented using Flask. It provides endpoints to receive and store the encrypted data from the keylogger.

### Endpoints
- `POST /api/computers/<computer_name>`: Receives encrypted data from the keylogger.
- `GET /api/computers`: Returns a list of all computers.
- `GET /api/computers/<computer_name>`: Returns the data for a specific computer.

### Server Setup
1. Navigate to the server directory:
    ```sh
    cd KeyLogger-2.0/Server
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the Flask server:
    ```sh
    python app.py
    ```

## Client Side
The client side is implemented using HTML, CSS, and JavaScript. It provides a user interface to view the data captured by the keylogger.

### Client Setup
1. Navigate to the client directory:
    ```sh
    cd KeyLogger-2.0/Client
    ```
2. Open `index.html` in a web browser to view the captured data.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Creators
- Itzchak Sklar
- David Landau
- Shemaryahu Zalmanov