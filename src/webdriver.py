import time

from playwright.sync_api import (
    Page,
    Playwright,
    Request,
    Route,
    expect,
    sync_playwright,
)

from src import helper


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

    helper.Anti.disable_webdriver(page=page)

    page.goto("")

    helper.Control.hold()

    # ---------------------

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
