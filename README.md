# Accu Type

The Typing Speed Test web application is designed to help users assess and improve their typing skills through an interactive online interface. Built using Flask for the backend and HTML and CSS for the frontend, this application provides an intuitive and engaging user experience. It offers a dynamic and responsive platform for users of all skill levels to test their typing speed and accuracy.

## Features

- Multiple difficulty levels: Easy, Medium, and Hard
- Calculates typing speed in Words Per Minute (WPM)
- Provides accuracy of typing
- Leaderboard to track top scores
- Pause and resume functionality

## Technologies Used

- Python
- Flask
- HTML
- CSS

## Setup Instructions

### Prerequisites

- Python 3.x installed on your machine
- `pip` package manager

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/typing-speed-test.git
    cd typing-speed-test
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Make sure your directory structure looks like this:

    ```
    typing-speed-test/
    ├── app.py
    ├── templates/
    │   └── index.html
    └── static/
        └── styles.css
    ```

2. Start the Flask server:

    ```bash
    python app.py
    ```

3. Open your web browser and go to:

    ```
    http://127.0.0.1:5000/
    ```

## Directory Structure

