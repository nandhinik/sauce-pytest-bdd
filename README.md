# sauce-pytest-bdd

# Automation Tests using Selenium, Pytest, Pytest-bdd

Sample code to perform UI testing for www.saucedemo.com

## Initial Setup

This project requires version of Python 3.6

To set up this project on your local machine:

1. Create a virtual env using python-3.6 --> `virtualenv -p python3 sauce_pytest`
2. Activate the virtual env --> `source {path/to/sauce_pytest}/bin/activate`
3. Clone it from this GitHub repository. --> `git clone https://github.com/nandhinik/sauce-pytest-bdd.git`
4. Install all the dependencies from root(sauce-pytest-bdd) directory --> `pip install -r requirements.txt`
5. For Web UI tests, install the appropriate browser and WebDriver executable.
   * These tests use Chrome and chromedriver

## Running Tests
Run tests simply using the `pytest` command.

Other Examples:

`pytest --html=./log/report.html` - To run all tests with html report

`pytest tests/step_defs/test_login_steps.py`

`pytest tests/step_defs/test_checkout_steps.py`

`pytest tests/step_defs/test_login_steps.py --html=./log/report.html`
