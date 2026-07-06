import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "thirumalaivasanr0@gmail.com"
PASSWORD = "WrongPassword123!"

def test_invalid_password(driver):
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
        print("Continue Clicked")

        password_field = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )

        password_field.clear()

        for ch in PASSWORD:
            password_field.send_keys(ch)
            time.sleep(0.1)

        password_field.send_keys(Keys.TAB)

        login_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Login']")
            )
        )

        login_btn.click()
        print("Login Clicked")

        # Keep sleep(5) for error message to render before taking screenshot
        time.sleep(5)

        # Meaningful assertion: verify URL did not change since it's an invalid password
        assert driver.current_url == login_page_url, "URL changed unexpectedly on invalid password."

        driver.save_screenshot("invalid_password.png")
        print("Invalid Password Screenshot Saved")

    except Exception as e:
        print("Error :", e)
        driver.save_screenshot("error_invalid_password.png")
        raise e
