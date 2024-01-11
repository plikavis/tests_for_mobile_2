import os
from typing import Literal
from appium.options.android import UiAutomator2Options
import dotenv
from pydantic_settings import BaseSettings
from utils.file import abs_path_from_project


context_type = Literal["bstack", "local_emulator", "local"]


class Config(BaseSettings):
    contex: context_type = "local_emulator"
    platform_version: str = "9.0"
    app: str = "bs://74681feb37c1602275e61c3409e0d68e27d822b1e"
    app_wait_activity: str = "org.wikipedia.*"
    device_name: str = "Google Pixel 3"
    remote_url: str = "http://hub.browserstack.com/wd/hub"


# без такой загрузки не работвет ни один env файл с отличным от .env названием как можно обойти?
dotenv.load_dotenv(dotenv_path=abs_path_from_project(f'.env.{Config().contex}'))
settings = Config(_env_file=abs_path_from_project(f'.env.{Config().contex}'))


def init_options():
    options = UiAutomator2Options()
    if settings.contex == 'local':
        pass  # нет возможности подключить реальный девайс
    if settings.contex == 'bstack':
        dotenv.load_dotenv('.env.credentials')
        options.set_capability('platformVersion', settings.platform_version)
        options.set_capability('deviceName', settings.device_name)
        options.set_capability('app', settings.app)
        options.set_capability('appWaitActivity', settings.app_wait_activity)
        options.set_capability('bstack:options', {"projectName": "First Python project",
                                                  "buildName": "browserstack-build-1",
                                                  "sessionName": "BStack first_test",
                                                  "userName": os.getenv('BSTACK_USER_NAME'), #settings.bstack_user_name
                                                  "accessKey": os.getenv('BSTACK_ACCESS_KEY')})
    if settings.contex == 'local_emulator':
        options.set_capability('platformVersion', settings.platform_version)
        options.set_capability('deviceName', settings.device_name)
        options.set_capability('app', abs_path_from_project(settings.app))
        options.set_capability('appWaitActivity', settings.app_wait_activity)
    return options


