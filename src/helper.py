import time
from threading import Event

from playwright.sync_api import (
    Page,
    Playwright,
    Request,
    Route,
    expect,
    sync_playwright,
)

from threading import Event


class Control:
    @staticmethod
    def hold():
        Event().wait()


class Anti:
    @staticmethod
    def disable_webdriver(page: Page):
        """
        it is different when using webdriver through playwright and so on,
        the `window.navigator.webdriver` maybe set as `true` for runing webdriver.
        so disable it will help to bypass some basic detection.
        """

        js = """
            Object.defineProperties(navigator, {webdriver:{get:()=>undefine}});
            """
        page.add_init_script(js)
