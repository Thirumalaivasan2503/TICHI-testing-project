# Tichi Web Application Automation Testing

## 📌 Project Overview

This project is a Selenium WebDriver automation framework developed using **Python** and **Pytest** to automate the login functionality of the Tichi Web Application.

The framework validates multiple login scenarios using automated test cases and generates execution results through Pytest.

---

## 🚀 Tech Stack

- Python 3.x
- Selenium WebDriver
- Pytest
- Chrome Browser
- VS Code

---

## 📂 Project Structure

```
Tichi-final-project/
│── test_valid_login.py
│── test_invalid_email.py
│── test_invalid_password.py
│── test_empty_email.py
│── test_empty_password.py
│── test_unregistered_email.py
│── requirements.txt
│── README.md
```

---

## ✅ Automated Test Scenarios

- Valid Login
- Invalid Email Format
- Invalid Password
- Empty Email
- Empty Password
- Unregistered Email

---

## ▶️ How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute All Tests

```bash
pytest -v
```

---

## 📸 Features

- Automated Login Validation
- Explicit Waits
- Screenshot Capture
- Negative & Positive Test Scenarios
- Pytest Test Execution
- Clean and Reusable Selenium Code

---

## 📊 Expected Result

```text
collected 6 items

test_valid_login.py::test_valid_login PASSED
test_invalid_email.py::test_invalid_email PASSED
test_invalid_password.py::test_invalid_password PASSED
test_empty_email.py::test_empty_email PASSED
test_empty_password.py::test_empty_password PASSED
test_unregistered_email.py::test_unregistered_email PASSED
```

---

## 👨‍💻 Author

**Thirumalai R**

Automation Testing Project using Selenium with Python and Pytest.
