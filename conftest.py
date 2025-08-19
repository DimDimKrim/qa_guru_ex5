import pytest
from selene import Browser, Config
from selene.support.shared import config
from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options
from utils import attach

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    caps = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(caps)

    selenoid_url =f"https://user1:123@selenoid.autotests.cloud/wd/hub" #os.getenv("SELENOID_URL")
    if not selenoid_url:
        raise RuntimeError("SELENOID_URL env variable is not set")

    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=options
    )

    browser = Browser(Config(driver))  # Создаем объект Selene с WebDriver

    yield browser  # Возвращаем объект browser для тестов

    # После теста собираем артефакты
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()



# @pytest.fixture(scope = 'function' , autouse=True)
# def browser_open():
#     browser.open('https://demoqa.com/automation-practice-form')
#     yield
#     browser.quit()

