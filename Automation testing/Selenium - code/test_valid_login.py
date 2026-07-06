import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "thirumalaivasanr0@gmail.com"
PASSWORD = "Thiru@2825"

def test_valid_login(driver):
    wait = WebDriverWait(driver, 20)
    
    try:
        driver.get("https://tichi-app-webapp-stage.web.app")
        print("Application Opened")
        
        sign_in = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Sign In']")
            )
        )
        sign_in.click()
        print("Sign In Clicked")
        
        # Wait for navigation to login page
        wait.until(EC.url_contains("/login"))
        login_page_url = driver.current_url

        email = wait.until(
            EC.visibility_of_element_located((By.ID, "email"))
        )

        email.clear()
        email.send_keys(EMAIL)

        continue_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Continue']")
            )
        )
        continue_btn.click()

        password = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )

        password.clear()

        for ch in PASSWORD:
            password.send_keys(ch)
            time.sleep(0.1)

        password.send_keys(Keys.TAB)

        login_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Login']")
            )
        )

        login_btn.click()
        print("Login Clicked")

        # Replaced time.sleep(5) with WebDriverWait for URL change
        wait.until(EC.url_changes(login_page_url))
        
        # Meaningful assertion: verify URL changed after successful login
        assert driver.current_url != login_page_url, "Login failed, URL did not change."

        driver.save_screenshot("valid_login_success.png")
        print("Dashboard Screenshot Saved")

    except Exception as e:
        print("Error :", e)
        driver.save_screenshot("valid_login_error.png")
        raise e
