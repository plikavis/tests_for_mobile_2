import allure
import pytest
from allure import step
from allure_commons._allure import StepContext
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selene import browser, support
import os
import pydantic

import utils.allure




@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def mobile_management():

    options = UiAutomator2Options().load_capabilities({
        "platformVersion": "14.0",
        # "platformName": "Android",
        "deviceName": "Pixel 3 XL API 34",
        "app": "/Users/polinavishnyakova/PycharmProjects/tests_for_mobile_2/app-alpha-universal-release(1).apk",
        "appium:appWaitActivity": "org.wikipedia.*",
    })

    # browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub',
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=StepContext
    )

    yield
    utils.allure.screenshot()
    utils.allure.page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    # utils.allure.video(login, password, session_id)


@pytest.fixture()
def skip_onboarding():
    with step('Skip onboarding'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

