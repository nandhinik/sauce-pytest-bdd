"""Testing the login page of saucedemo.com"""

import time

from pytest_bdd import scenarios, when, then, parsers

from common.Constants import txt_password, err_msg_selector, txt_username
from common.LoginCreds import STANDARD_USER, STANDARD_PASSWORD, URL, LOCKED_OUT_USER


# Scenarios

scenarios('../features/login.feature', example_converters=dict(phrase=str))


@when('I enter a username')
def submit_username(browser):
    browser.find_element_by_id(txt_username).send_keys(
        STANDARD_USER)


@when('I enter a locked out username and password')
def submit_locked_info(browser):
    browser.find_element_by_id(txt_username).send_keys(
        LOCKED_OUT_USER)
    browser.find_element_by_id(txt_password).send_keys(
        STANDARD_PASSWORD)


@then(parsers.parse('I should get a message "{message}"'))
def verify_msg_display(browser, message):
    assert message in \
           browser.find_elements_by_xpath(err_msg_selector[1])[0].text
    time.sleep(2)


@then('I should see the login page')
def verify_login_page(browser):
    assert browser.current_url == URL
