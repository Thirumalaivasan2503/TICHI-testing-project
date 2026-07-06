import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "not_registered_12345@gmail.com"

def test_unregistered_email(driver):
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

        # Keep sleep(3) for error message to render before taking screenshot
        time.sleep(3)

        # Meaningful assertion: verify URL remains on login or redirects to sign-up
        assert "login" in driver.current_url or "sign-up" in driver.current_url, f"Unexpected URL: {driver.current_url}"

        driver.save_screenshot("unregistered_email.png")
        print("Unregistered Email Screenshot Saved")

    except Exception as e:
        print("Error :", e)
        driver.save_screenshot("error_unregistered_email.png")
        raise e
