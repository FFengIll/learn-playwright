from playwright.sync_api import sync_playwright
from util import holdon


def main():
    with sync_playwright() as p:
        # doc: https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch
        # set any browser args and options here
        # ref: https://www.programsbuzz.com/article/maximize-browser-playwright

        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        # browser = p.chromium.launch(
        #     headless=False, args=["--start-fullscreen", "--start-maximized"]
        # )

        # furtheremore, add `no_viewport=True` to confirm it
        # ref: https://github.com/microsoft/playwright-python/issues/585

        context = browser.new_context(no_viewport=True)
        # context = browser.new_context()
        # context = browser.new_context(viewport=dict(width=100, height=100))
        page = context.new_page()
        page.goto("https://www.baidu.com/")

        holdon()


if __name__ == "__main__":
    main()
