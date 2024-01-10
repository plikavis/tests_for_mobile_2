import os
import pydantic


class Config (pydantic.BaseSettings):
    bstack_userName: str = "polinavish_E9hyNj"
    bstack_accessKey: str = "wcmbBf4yzPWeyHV6qPby"
    bstack_app: str = ""


config = Config()
bstack_userName = config.bstack_userName
bstack_accessKey = config.bstack_accessKey
# bstack_userName = os.getenv("bstack_userName")
# bstack_accessKey = os.getenv("bstack_accessKey")