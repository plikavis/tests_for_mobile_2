import allure
import pytest
from allure import step
from allure_commons._allure import StepContext
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, support
import os
import utils.allure
from config import init_options, settings


@pytest.fixture()
def mobile_management():
    options = init_options()
    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            settings.remote_url,
            options=options
        )
    browser.config.timeout = float(os.getenv('timeout', '5.0'))
    browser.config._wait_decorator = support._logging.wait_with(
        context=StepContext
    )

    yield
    utils.allure.screenshot()
    utils.allure.page_source()

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()
    if settings.contex == 'bstack':
        utils.allure.video(settings.bstack_user_name, settings.bstack_access_key, session_id)


@pytest.fixture
def skip_onboarding():
    with step('Skip onboarding'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
