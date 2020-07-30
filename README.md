# sauce-pytest-bdd

# Selenium, Pytest, Pytest-bdd Automation Tests

Sample code to perform UI testing for www.saucedemo.com

## Initial Setup

This project requires version of Python 3.6

To set up this project on your local machine:

1. Create a virtual env using python-3.6 --> `virtualenv -p python3 sauce_pytest`
2. Activate the virtual env --> `source {path/to/sauce_pytest}/bin/activate`
3. Clone it from this GitHub repository.
4. Install all the dependencies --> `pip install -r requirements.txt`
5. For Web UI tests, install the appropriate browser and WebDriver executable.
   * These tests use Chrome and chromedriver

## Running Tests
Run tests simply using the `pytest` command.

Examples:
`pytest tests/step_defs/test_login_steps.py`
`pytest tests/step_defs/test_checkout_steps.py`
`pytest tests/step_defs/test_login_steps.py --html=./log/report.html`