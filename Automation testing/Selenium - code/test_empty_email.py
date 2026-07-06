import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = ""

def test_empty_email(driver):
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


        time.sleep(3)

        assert driver.current_url == login_page_url, "URL changed unexpectedly on empty email."

        driver.save_screenshot("empty_email.png")
        print("Empty Email Screenshot Saved")

    except Exception as e:
        print("Error :", e)
        driver.save_screenshot("error_empty_email.png")
        raise e
