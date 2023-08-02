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


def disable_webdriver(page: Page):
    js = """
        Object.defineProperties(navigator, {webdriver:{get:()=>undefine}});
        """
    page.add_init_script(js)


def add_header(page):
    page.set_extra_http_headers({"Dnt": "1", "Upgrade-Insecure-Requests": "1"})


def delete_header(page):
    def action(route: Route, request: Request):
        if "Sec-Fetch-User" in request.headers:
            del request.headers["Sec-Fetch-User"]
        # override headers
        headers = {
            **request.headers,
        }
        route.continue_(headers=headers)

    page.route("**/*", action)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(
        headless=False,
        # args=["--auto-open-devtools-for-tabs"]
    )

    context = browser.new_context()

    page = context.new_page()

    # add_header(page)
    # delete_header(page)

    disable_webdriver(page=page)

    page.goto("")

    # ---------------------
    Event().wait()

    # ---------------------

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
