import pytest
import time

from pytest_bdd import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import common.Constants as Constants
import common.LoginCreds as LoginCreds


# Hooks

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f"Step failed: {step}")


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Shared Given Steps

@given('I am on the login page')
def sauce_demo_home(browser):
    browser.get(LoginCreds.URL)


# Shared When Steps
@when('I enter a valid username and password')
def submit_valid_info(browser):
    browser.find_element_by_id(Constants.txt_username).send_keys(
        LoginCreds.STANDARD_USER)
    browser.find_element_by_id(Constants.txt_password).send_keys(
        LoginCreds.STANDARD_PASSWORD)


@when('I login')
def click_login(browser):
    browser.find_element_by_xpath(Constants.btn_login).click()
    time.sleep(2)


# Shared Then Steps
@then('I should see the products page')
def verify_products_page(browser):
    WebDriverWait(browser, 5).until(EC.url_changes)
    assert browser.find_element(By.CLASS_NAME, Constants.pg_product).text == \
        Constants.PRODUCTS


@then('I should see the your information page')
def verify_information_page(browser):
    WebDriverWait(browser, 5).until(EC.url_changes)
    assert browser.find_element(By.CLASS_NAME, Constants.pg_your_info).text == \
        Constants.YOUR_INFORMATION
