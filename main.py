from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import winsound
import traceback
import random
import os  



def play_alert_sound():
    duration = 1000 
    frequency = 750  
    winsound.Beep(frequency, duration)



def run_bot():
    # Paths (replace placeholders before running)
    chrome_driver_path = "<PATH_TO_CHROMEDRIVER>"
    chrome_binary_path = "<PATH_TO_CHROME_BINARY>"
    chrome_profile_path = "<PATH_TO_CHROME_PROFILE>"
    profile_name = "Default"  # Replace with your Chrome profile name if different


    wallet_password = os.getenv("WALLET_PASSWORD", "<YOUR_PASSWORD>")  # Replace with "<YOUR_PASSWORD>"

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")
    chrome_options.add_argument(f"profile-directory={profile_name}")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless=new")  # Optional: Remove for non-headless execution

    # Initialize ChromeDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:

        driver.get("chrome-extension://hcjhpkgbmechpabifbggldplacolbkoh/fullpage.html#/") 
        time.sleep(5)

        
        input_field = driver.find_element(By.XPATH, '//*[@type="password"]')
        input_field.clear()
        input_field.send_keys(wallet_password)

        login_button = driver.find_element(By.XPATH, '//button')
        login_button.click()
        time.sleep(5)

        
        driver.get("https://app.atmosprotocol.com/")
        time.sleep(5)

        print("Bot is running.")
        counter = 0  

        # Infinite loop for swapping
        while True:
            try:
               
                input_field = driver.find_element(By.XPATH, '//input[@type="text"]')
                input_field.clear()
                random_value = round(random.uniform(0.1, 1.0), 2)
                input_field.send_keys(str(random_value))
                print(f"Traded USDC: {random_value}")

                time.sleep(1)

               
                swap_button = driver.find_element(By.XPATH, '//button[contains(text(), "Swap")]')
                swap_button.click()

                time.sleep(2) 

                
                driver.switch_to.window(driver.window_handles[-1])
                confirm_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Confirm")]'))
                )
                confirm_button.click()

               
                driver.switch_to.window(driver.window_handles[0])

               
                counter += 1
                print(f"Swap completed successfully. Total swaps: {counter}")

                
                time.sleep(12)

            except Exception as loop_exception:
                print(f"Error inside the loop: {loop_exception}")
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



if __name__ == "__main__":
    while True:
        print("Starting bot...")
        play_alert_sound()
        run_bot()
        time.sleep(10) 
