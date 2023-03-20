from path import Path

from playwright.sync_api import sync_playwright

from util import holdon

with sync_playwright() as p:
    browser_type = p.chromium
    browser = browser_type.launch(headless=True)
    context = browser.new_context(accept_downloads=True)

    page = context.new_page()
    # here is a demo website provide a download button (to a pdf)
    page.goto("https://www.mjrui.com/mjrui_FileInfo_364333.html")

    with page.expect_download() as download_info:
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

    download = download_info.value
    # wait for download to complete
    path = download.path()
    print(download)
    # it is a temp path for browser, call `save_as` for yours
    print(path)

    output = Path("output")
    if not output.exists():
        output.makedirs_p()
    download.save_as(output / "test.pdf")

    holdon()

    
    
