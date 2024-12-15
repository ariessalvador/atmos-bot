from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace these placeholders with your own configurations
chrome_driver_path = "/path/to/chromedriver"  # Example: "/usr/local/bin/chromedriver"
chrome_binary_path = "/path/to/chrome-binary"  # Example: "/opt/google/chrome/chrome"
chrome_profile_path = "/path/to/chrome-user-data"  # Example: "/home/user/.config/google-chrome"
profile_name = "Your-Profile-Name"  # Example: "Default"

# Input starket wallet passowrd
PASSWORD = "YOUR_PASSWORD_HERE"

# Configure Chrome options
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")
chrome_options.add_argument(f"profile-directory={profile_name}")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless=new")


service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Allow browser to initialize
time.sleep(5)

# Login Process (Update password here)
try:
    input_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div/div/input')
    input_field.clear()
    input_field.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/form/button')
    login_button.click()
except Exception as e:
    print(f"Error during login process: {e}")

# Allow page to load
time.sleep(5)

# Open Atmos Protocol
driver.get("https://app.atmosprotocol.com/")

time.sleep(5)

print("Bot is running.")

# Main Loop
while True:
    try:
        # Locate the input field for entering the value (0.1)
        input_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/input')
        input_field.clear()
        input_field.send_keys('0.1')

        time.sleep(1)

        # Locate and click the "Swap" button
        swap_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/div[2]/div/button[2]')
        swap_button.click()

        # Wait before switching windows
        time.sleep(2)

        # Switch to the last opened window (extension)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

        # Confirm Transaction
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div/div[3]/div/button[2]'))
        )
        confirm_button.click()
        print("Confirm button clicked.")

        # Switch back to the main window
        driver.switch_to.window(window_handles[0])

    except Exception as e:
        print(f"Error in main loop: {e}")

    # Adjust wait time as needed
    time.sleep(12)

# Close the browser (if manually interrupted)
driver.quit()
