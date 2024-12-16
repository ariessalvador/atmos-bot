# Atmos Protocol Testnet Trading Bot

This is an automated trading bot built using **Python** and **Selenium** to interact with the **Atmos Protocol** testnet. It automates repeated swap transactions and is designed to run continuously with features to alert the user if an error occurs or the bot restarts.

---

## Features

- **Automated Swap Transactions**: Repeatedly performs swap actions on the Atmos Protocol testnet.
- **Continuous Execution**: Automatically restarts if the bot crashes or encounters an error.
- **Sound Alerts**: Plays a beep sound to notify the user if the bot starts, crashes, or restarts.
- **Headless Mode**: Runs the Chrome browser in the background for efficient execution.

---

## Prerequisites

Ensure you have the following installed and configured:

1. **Python 3.x** installed.
2. **Google Chrome** installed.
3. **ChromeDriver** (compatible with your Chrome version).

⚠️ **Important Note**: The Chrome browser version and ChromeDriver version **must be compatible**. Use the following resource to check and download the correct versions:
[Chrome for Testing - Compatible Versions](https://googlechromelabs.github.io/chrome-for-testing/)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ariessalvador/atomos-bot.git
   ```

2. Install the required Python library:
   ```bash
   pip install selenium
   ```

3. Download **ChromeDriver**:
   - Ensure it matches your Chrome version.
   - Place the executable in a known directory.

---

## Configuration

Update the placeholders in the script with your actual paths and information:

- **`chrome_driver_path`**: Path to your ChromeDriver executable.
- **`chrome_binary_path`**: Path to your Chrome binary.
- **`chrome_profile_path`**: Path to your Chrome user profile directory.
- **`PASSWORD`**: Replace `<PASSWORD>` with your testnet wallet password.

Example configuration snippet:

```python
chrome_driver_path = "<PATH_TO_CHROMEDRIVER>"
chrome_binary_path = "<PATH_TO_CHROME_BINARY>"
chrome_profile_path = "<PATH_TO_CHROME_PROFILE>"
profile_name = "Default"  # Use your Chrome profile name
```

---

## Usage

1. Run the bot:
   ```bash
   python main.py
   ```

2. The bot will:
   - Launch Chrome in headless mode.
   - Log in to the testnet wallet using the password.
   - Interact with the Atmos Protocol testnet to perform swap transactions.
   - Handle confirmation prompts automatically.
   - Restart automatically if it crashes, playing a beep sound to notify you.

3. **Monitor** the terminal output for activity logs and error messages.

---

## Stopping the Bot

- Use **Ctrl+C** in the terminal to stop the bot.
- Alternatively, close the process running the script.

---

## Troubleshooting

1. **Chrome and ChromeDriver version mismatch**:
   - Verify compatibility here: [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/).
   - Replace ChromeDriver with the correct version.

2. **Missing Dependencies**:
   - Reinstall Selenium:
     ```bash
     pip install --upgrade selenium
     ```

3. **Incorrect File Paths**:
   - Ensure the Chrome binary, ChromeDriver, and user profile paths are correct.

4. **Browser Not Launching**:
   - Confirm Chrome is installed and the paths are properly configured.

---

## Disclaimer

This bot is designed for **testnet use only**. Use it responsibly and at your own risk. The author is not liable for any misuse, technical issues, or outcomes caused by this script.

---

## License

This project is licensed under the **MIT License**.

---

## Contributions

Feel free to fork this repository, submit pull requests, or report issues. Contributions are always welcome!

---

## Contact

For support or inquiries, reach out via Telegram:  
[@asaaaaaadd](https://t.me/asaaaaaadd)
