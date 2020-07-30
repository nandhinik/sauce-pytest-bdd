"""Constant variables used throughout the framework."""

from selenium.webdriver.common.by import By

# Strings
REMOVE = "REMOVE"
ADD_TO_CART = "ADD TO CART"
ERR_MSG_USER_NAME = "Username is required"
PRODUCTS = "Products"
YOUR_INFORMATION = "Checkout: Your Information"


# UI Selectors
err_msg_selector = (By.XPATH, '//*[@id="login_button_container"]/div/form')
btn_login = "//input[@id='login-button']"
txt_username = "user-name"
txt_password = "password"
pg_product = "product_label"
pg_your_info = "subheader"
shopping_cart = "shopping_cart_link"
lbl_item = "inventory_item_name"
continue_shopping = "btn_secondary"
checkout = "checkout_button"
add_to_cart_buttons_selector = "btn_primary"
btn_remove_cart = "btn_secondary"
cart_item_count_selector = "shopping_cart_badge"
