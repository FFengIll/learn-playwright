from path import Path

from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

from util import holdon


def download_in_chromium(page: "Page", action, output=None):
    """
    action is a callback to process the page

    """
    with page.expect_download() as download_info:
        action(page)

    download = download_info.value
    # wait for download to complete
    path = download.path()
    print(download)
    # it is a temp path for browser, call `save_as` for yours
    print(path)

    if output:
        download.save_as(output)


def main():
    p = sync_playwright().start()
    browser_type = p.chromium
    browser = browser_type.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    page = context.new_page()
    # here is a demo website provide a download button (to a pdf)
    page.goto("https://www.mjrui.com/mjrui_FileInfo_364333.html")

    def action(page: "Page"):
        button = page.query_selector("#HyperLink_Down")
        print(button)

        # add modifiers according to https://github.com/microsoft/playwright-python/issues/675
        # since `pdf` will lead to a view but download
        # and this works for chrome since `alt+left click` = `save as`

        button.click(
            modifiers=[
                "Alt",
            ]
        )

    output = Path("output")
    if not output.exists():
        output.makedirs_p()

    download_in_chromium(page, action, output / "test.pdf")


if __name__ == "__main__":
    main()
