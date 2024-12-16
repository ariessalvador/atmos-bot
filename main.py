from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import winsound
import traceback


# Function to play an alert sound
def play_alert_sound():
    winsound.Beep(750, 1000)  # Simple beep sound


# Function to start and run the bot
def run_bot():
    # Paths (replace placeholders with your actual paths before running)
    chrome_driver_path = "<PATH_TO_CHROMEDRIVER>"
    chrome_binary_path = "<PATH_TO_CHROME_BINARY>"
    chrome_profile_path = "<PATH_TO_CHROME_PROFILE>"
    profile_name = "Default"  # Replace with your Chrome profile name if different

    # Chrome options
    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")
    chrome_options.add_argument(f"profile-directory={profile_name}")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless=new")

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the Starkey wallet login page
        driver.get("chrome-extension://hcjhpkgbmechpabifbggldplacolbkoh/fullpage.html#/")
        time.sleep(5)

        # Enter wallet password 
        input_field = driver.find_element(By.XPATH, '//*[@type="password"]')
        input_field.clear()
        input_field.send_keys("<PASSWORD>")
        login_button = driver.find_element(By.XPATH, '//button')
        login_button.click()
        time.sleep(5)

        # Go to Atmos Protocol
        driver.get("https://app.atmosprotocol.com/")
        time.sleep(5)

        # Start main bot functionality
        print("Bot is running.")
        while True:
            try:
                # Enter value and swap
                input_field = driver.find_element(By.XPATH, '//input[@type="text"]')
                input_field.clear()
                input_field.send_keys('0.1')
                time.sleep(1)

                swap_button = driver.find_element(By.XPATH, '//button[contains(text(), "Swap")]')
                swap_button.click()
                time.sleep(2)

                # Handle confirmation window
                driver.switch_to.window(driver.window_handles[-1])
                confirm_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Confirm")]'))
                )
                confirm_button.click()
                print("Confirm button clicked.")
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(12)

            except Exception as inner_exception:
                print(f"Error inside the loop: {inner_exception}")
                play_alert_sound()
                break

    except Exception as e:
        print(f"Critical bot failure: {e}")
        play_alert_sound()
        traceback.print_exc()

    finally:
        driver.quit()
        print("Bot stopped. Restarting...")
        play_alert_sound()



while True:
    print("Starting bot...")
    play_alert_sound()
    run_bot()
    time.sleep(10)
