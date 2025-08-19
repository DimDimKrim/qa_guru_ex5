import pytest
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
import os

@pytest.fixture(scope = 'function' , autouse=True)
def browser_open():
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()


@pytest.fixture(scope = 'function')
def setup_browser():
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities,update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options)

        browser.config.driver = driver

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()