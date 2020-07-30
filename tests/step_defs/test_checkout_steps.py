"""Testing the checkout page of saucedemo.com"""

import time

import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers
from selenium.webdriver.common.by import By

import common.Constants as Constants


# Scenarios

scenarios('../features/checkout.feature', example_converters=dict(phrase=str))


def get_number_cart_items(browser):
    """ Get the number of items in the cart. """
    has_items_in_cart = len(browser.find_elements(
        By.CLASS_NAME, Constants.cart_item_count_selector)) > 0
    if has_items_in_cart:
        num_items_in_cart = browser.find_element(
            By.CLASS_NAME, Constants.cart_item_count_selector).text
        return int(num_items_in_cart)
    else:
        return 0


# When Steps

@when('I add multiple items to a cart')
def add_multiple_items(browser):
    add_to_cart_buttons = browser.find_elements(
        By.CLASS_NAME, Constants.add_to_cart_buttons_selector)
    num_items_in_cart = 0

    assert get_number_cart_items(browser) == num_items_in_cart, \
        "An unexpected item has been found in the cart."

    for item_button in add_to_cart_buttons:
        item_button.click()
        num_items_in_cart += 1
        assert get_number_cart_items(browser) == num_items_in_cart, \
            "An unexpected item has been found in the cart."
        time.sleep(1)
        assert item_button.text == Constants.REMOVE


@when('I go to the cart page')
def go_to_cart_page(browser):
    browser.find_element(By.CLASS_NAME, Constants.shopping_cart).click()
    time.sleep(1)


@when('I choose to continue shopping')
def continue_shopping(browser):
    browser.find_element(By.CLASS_NAME, Constants.continue_shopping).click()
    time.sleep(1)


@when('I choose to checkout')
def checkout(browser):
    browser.find_element(By.CLASS_NAME, Constants.checkout).click()
    time.sleep(1)


@pytest.mark.parametrize(
    ['item'],
    ["Sauce Labs Bike Light",
     "Sauce Labs Bolt T-Shirt"])
@scenario(
    "../features/checkout.feature",
    "User is able to add one item to a cart",
)
@when('I add an <item> to the cart')
@when('I have an <item> in the cart')
def add_an_item(browser, item):
    add_to_cart_buttons = browser.find_elements(
        By.CLASS_NAME, Constants.add_to_cart_buttons_selector)
    inventory_names = browser.find_elements(
        By.CLASS_NAME, Constants.lbl_item)
    num_items_in_cart = 0
    assert get_number_cart_items(browser) == num_items_in_cart, \
        "An unexpected item has been found in the cart."
    index = 0
    for inventory_name in inventory_names:
        if inventory_name.text == item:
            break
        index = index + 1
    assert index < len(inventory_names), \
        "Requested item not found in the cart."
    item_button = add_to_cart_buttons[index]
    item_button.click()
    time.sleep(1)
    assert item_button.text == Constants.REMOVE
    assert get_number_cart_items(browser) == 1, \
        "An unexpected item has been found in the cart."


@pytest.mark.parametrize(
    ['item'],
    ["Sauce Labs Bike Light"])
@scenario(
    "../features/checkout.feature",
    "User is able to remove items from the cart",
)
@when('I remove an item from the cart')
def remove_an_item(browser):
    item_button = browser.find_element(
        By.CLASS_NAME, Constants.btn_remove_cart)
    num_items_in_cart = 1
    assert get_number_cart_items(browser) == num_items_in_cart, \
        "An unexpected item has been found in the cart."
    item_button.click()
    time.sleep(1)
    assert item_button.text == Constants.ADD_TO_CART
    assert get_number_cart_items(browser) == 0, \
        "An unexpected item has been found in the cart."


# Then Steps
@then(parsers.parse('I should see the <item> in the cart'))
def verify_item_in_cart(browser, item):
    browser.find_element(By.CLASS_NAME, Constants.shopping_cart).click()
    assert item == browser.find_elements(By.CLASS_NAME, Constants.lbl_item)[0].text
    time.sleep(1)


@then('I no longer see any items in the cart')
def verify_cart_is_empty(browser):
    assert get_number_cart_items(browser) == 0, \
        "An unexpected item has been found in the cart."


@then('I should see the items in the cart')
def verify_cart_is_full(browser):
    remove_cart_buttons = browser.find_elements(
        By.CLASS_NAME, Constants.btn_remove_cart)
    assert get_number_cart_items(browser) == len(remove_cart_buttons), \
        "An unexpected item has been found in the cart."
