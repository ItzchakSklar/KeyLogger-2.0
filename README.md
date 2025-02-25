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
*To be updated in the future.*

## Client Side
*To be updated in the future.*

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.