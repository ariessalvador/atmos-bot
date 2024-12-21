from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import winsound
import traceback
import random
import time



def play_alert_sound():
    winsound.Beep(750, 100)



def initialize_driver():
    chrome_driver_path = "<PATH_TO_CHROMEDRIVER>"
    chrome_binary_path = "<PATH_TO_CHROME_BINARY>"
    chrome_profile_path = "<PATH_TO_CHROME_PROFILE>"
    profile_name = "Default"

    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")
    chrome_options.add_argument(f"profile-directory={profile_name}")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--headless=new")

    return webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)


# Function to perform swap action
def perform_swap(driver, counter):
    try:
        # Input random value
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/input'))
        )
        input_field.clear()
        random_value = round(random.uniform(0.1, 1.0), 2)
        input_field.send_keys(str(random_value))
        print(f"Traded USDC: {random_value}")

        # Click the "Swap" button
        swap_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/div[2]/div/button[2]'))
        )
        swap_button.click()

        # Handle extension window
        time.sleep(1)  # Allow time for the extension to open
        driver.switch_to.window(driver.window_handles[-1])  # Switch to the last opened window

        # Click the "Confirm" button in the extension
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div/div[3]/div/button[2]'))
        )
        confirm_button.click()
        print("Confirmed swap in extension.")

        # Switch back to the main window
        driver.switch_to.window(driver.window_handles[0])

        counter += 1
        print(f"Swap completed successfully. Total swaps: {counter}")
        return counter
    except Exception as e:
        print(f"Error during swap: {e}")
        play_alert_sound()
        return counter


# Main bot logic
def run_bot():
    driver = initialize_driver()
    wallet_password ="<YOUR_STARKEY_WALLET_PASSQWORD>"
    try:
        # Login to the Chrome Extension
        driver.get("chrome-extension://hcjhpkgbmechpabifbggldplacolbkoh/fullpage.html#/")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div/div/input'))
        ).send_keys({wallet_password})
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/form/button').click()
        print("Logged into Chrome Extension.")
        driver.get("https://app.atmosprotocol.com/")
        print("Navigated to Atmos Protocol website.")

        counter = 0
        while True:
            counter = perform_swap(driver, counter)

            # Wait for the button to change state before continuing
            try:
                WebDriverWait(driver, 30).until(
                    lambda d: d.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[2]/div[2]/div/button').text.strip() == "Insufficient Balance"
                )
                print("Button state changed to 'Insufficient Balance'. Proceeding to next iteration.")
            except Exception as e:
                print(f"Error waiting for button state to change: {e}")
                break  # Exit the loop if the button state doesn't change in time

    except Exception as e:
        print(f"Critical bot failure: {e}")
        play_alert_sound()
        traceback.print_exc()
    finally:
        driver.quit()


# Restart bot in case of failure
while True:
    print("Starting bot...")
    play_alert_sound()
    run_bot()
    time.sleep(10)  # Short pause before restarting
