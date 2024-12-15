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
   git clone https://github.com/your-username/atmos-testnet-bot.git
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


---

## Usage

1. Run the bot:
   ```bash
   python bot.py

````
