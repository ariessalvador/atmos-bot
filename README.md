# Atmos Protocol Testnet Trading Bot

This is an automated trading bot built using Python and Selenium to interact with the **Atmos Protocol** testnet. Its primary purpose is to repeatedly perform swap transactions to increase the swap count on the testnet.

---

## Features

- Automates **swap transactions** on the Atmos Protocol testnet.
- Designed to run continuously in a loop until manually stopped.
- Uses Selenium to control Chrome browser and interact with the Atmos interface.

---

## Prerequisites

Before running the bot, ensure you have the following:

1. **Python 3.x** installed.
2. **Chrome browser** and **ChromeDriver** installed.
3. A **Chrome user profile** (optional but recommended for maintaining session).

⚠️ **Important Note**:  
The Chrome browser version and ChromeDriver version **must be compatible**.  
You can check and download the correct versions from this official resource:  
[Chrome for Testing - Compatible Versions](https://googlechromelabs.github.io/chrome-for-testing/)

---

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/ariessalvador/atomos-bot.git
   cd atmos-testnet-bot
   ```
2. Install required dependencies using `pip`:
   ```bash
   pip install selenium
   ```
3. Download **ChromeDriver**:
   - Ensure ChromeDriver matches your Chrome browser version.
   - Place the ChromeDriver executable in a known directory.

---

## Configuration

Update the placeholders in the Python script:

- **`chrome_driver_path`**: Path to your ChromeDriver executable.
- **`chrome_binary_path`**: Path to your Chrome binary (if not using system default).
- **`chrome_profile_path`**: Path to your Chrome user data directory.
- **`profile_name`**: Name of your Chrome profile (e.g., `Default`).
- **`PASSWORD`**: Your password for the testnet account.

Example configuration snippet:

````python
chrome_driver_path = "/path/to/chromedriver"
chrome_binary_path = "/path/to/chrome-binary"
chrome_profile_path = "/path/to/chrome-user-data"
profile_name = "Default"
PASSWORD = "YOUR_PASSWORD_HERE"
````


## Usage

1. Run the bot:
   ```bash
   python bot.py

2. The bot will:  
   - Launch Chrome and log in to the Atmos Protocol testnet.  
   - Perform swap transactions in a loop.  
   - Confirm transactions using a browser extension window.

3. Monitor the terminal output for activity logs.  

---

## Stopping the Bot

To stop the bot, use **Ctrl+C** in the terminal or close the browser manually.

---

## Troubleshooting

1. **Chrome and ChromeDriver version mismatch**:  
   - Verify compatibility using this link:  
     [Chrome for Testing - Compatible Versions](https://googlechromelabs.github.io/chrome-for-testing/).  
   - Download and replace the correct ChromeDriver version.

2. **Missing Dependencies**:  
   - Reinstall Selenium:  
     ```bash
     pip install --upgrade selenium
     ```

3. **Browser Not Launching**:  
   - Ensure the Chrome binary path and user profile paths are correct.  
   - Double-check the file paths in the configuration.

---

## Disclaimer

This bot is designed for **testnet use only**. Use it responsibly and at your own risk. The author is not liable for any misuse or potential issues caused by running this script.

---

## License

This project is licensed under the **MIT License**.

---

### Contributions

Feel free to fork this repository, submit pull requests, or report issues.  

---


## Contact

If you need help or have any questions, feel free to reach out via Telegram:  
[@asaaaaaadd](https://t.me/asaaaaaadd)


