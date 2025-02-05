# Stress Level Indicator

Stress Level Indicator is a browser extension that helps you monitor your stress levels and reminds you to take breaks. It uses a machine learning model to calculate stress levels based on various metrics such as Words Per Minute (WPM), mouse speed, and hesitation time.

## Features

- **Stress Level Indicator**: Displays your current stress level.
- **Break Reminder**: Reminds you to take a break when your stress level is high.
- **Machine Learning Model**: Calculates stress levels using a dataset of WPM, mouse speed, and hesitation time.

## Installation

1. Clone the repository to your local machine.
    ```sh
    git clone https://github.com/Kapil3Raj/Stress-Level-Indicator-Extension-.git
    ```
2. Open your browser and navigate to the extensions page.
3. Enable "Developer mode".
4. Click on "Load unpacked" and select the cloned repository folder.

## Usage

1. Click on the Stress Level Indicator extension icon in your browser.
2. The popup will display your current stress level.

## Running the Prediction Script

To calculate the stress level using the machine learning model, you need to run the `predict.py` script. Follow these steps:

1. Ensure you have Python installed on your machine.
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the `predict.py` script:
    ```sh
    python predict.py
    ```

## Files

- [popup.html](http://_vscodecontentref_/0): The HTML file for the extension's popup.
- `styles/popup.css`: The CSS file for styling the popup.
- `scripts/popup.js`: The JavaScript file for handling the popup's functionality.
- `predict.py`: The Python script for running the machine learning model to predict stress levels.
- `README.md`: This file.

## How It Works

The extension calculates your stress level using a machine learning model trained on a dataset that includes:

- **Words Per Minute (WPM)**: The speed at which you type.
- **Mouse Speed**: The speed at which you move your mouse.
- **Hesitation Time**: The time you spend hesitating before taking an action.

The model processes these metrics and provides a stress level indicator, which is displayed in the popup.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Repository

You can find the repository for this project [here](https://github.com/Kapil3Raj/Stress-Level-Indicator-Extension-).
