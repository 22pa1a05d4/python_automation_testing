
from selenium import webdriver #tool to automate and control browser
from selenium.webdriver.common.by import By #locate inputs,buttons

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome driver
driver = webdriver.Chrome()

# Open Streamlit app
driver.get("http://localhost:8501")  # Make sure Streamlit is running
time.sleep(5)  # Wait for Streamlit to fully load (can adjust)

# Explicit wait
wait = WebDriverWait(driver, 10)

try:
    # Locate input boxes
    username_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Username']")))
    password_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Password']")))

    # Send login credentials
    username_box.send_keys("admin")
    password_box.send_keys("1234")

    # Locate Login button using safe XPath
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]")))
    login_button.click()

    # Wait for page to respond after login
    wait.until(lambda d: "💱 Real-Time Currency Converter" in d.page_source or "Invalid username or password" in d.page_source)

    # Check login success
    if "💱 Real-Time Currency Converter" in driver.page_source:
        print("✅ Login Automation Test Passed")
    else:
        print("❌ Login Automation Test Failed")

except Exception as e:
    print(f"❌ Exception occurred: {e}")

finally:
    driver.quit()
