# Automation Testing Framework (Python + Selenium)

## Overview

This project demonstrates a **web automation testing framework** built using **Selenium and PyTest**.
It automates core user flows of an e-commerce website and follows industry best practices.

---

## Features

* Page Object Model (POM) design pattern
* Data-driven testing using JSON
* Screenshot capture on test failure
* Allure reporting integration
* Cross-environment configuration (config file)
* CI/CD integration with GitHub Actions
* Headless browser execution for CI

---

## Tech Stack

* Python
* Selenium WebDriver
* PyTest
* Allure Report
* WebDriver Manager
* GitHub Actions

---

## Project Structure

```
automation-testing-python-selenium/
│
├── tests/
│   ├── test_login.py
│   ├── test_search.py
│   ├── test_cart.py
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── search_page.py
│   ├── cart_page.py
│
├── utils/
│   ├── driver_factory.py
│   ├── config_reader.py
│   ├── data_reader.py
│
├── data/
│   └── testdata.json
│
├── config/
│   └── config.json
│
├── reports/
│   └── screenshots/
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Test Scenarios

### Login

* Valid login
* Invalid password
* Empty credentials

### Search

* Search valid product
* Search invalid keyword

### Cart

* Add product to cart
* Verify cart is empty

---

## Configuration

All environment settings are stored in:

```
config/config.json
```

Example:

```json
{
  "base_url": "https://automationteststore.com/",
  "browser": "chrome",
  "timeout": 10
}
```

---

## How to Run Tests (Local)

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run tests

```
pytest
```

---

## Allure Report

### Generate report

```
pytest
allure serve reports
```

---

## CI/CD (GitHub Actions)

* Tests run automatically on every push
* Uses **headless Chrome** for execution
* Ensures code stability before merge

---

## Screenshot on Failure

* Automatically captures screenshots when a test fails
* Stored in:

```
reports/screenshots/
```

* Attached in Allure report

---

## Sample Report
![Allure Report 1](sample-report\allure-report-1.png)
![Allure Report 2](sample-report\allure-report-2.png)
![Allure Report 3](sample-report\allure-report-3.png)

---

## Key Learnings

* Implemented scalable test automation framework
* Improved test stability using explicit waits
* Applied data-driven testing for better coverage
* Integrated automation tests with CI/CD pipeline

---

## Author

Nguyen Van Phuc
Automation Tester (Fresher)

---

## Notes

This project is built for learning and demonstration purposes, following real-world automation practices.
