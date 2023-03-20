from playwright.sync_api import sync_playwright
from util import holdon

with sync_playwright() as p:
    browsers = [p.chromium, p.firefox, p.webkit]
    # browsers= [p.chromium]
    for browser_type in browsers:
        browser = browser_type.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.baidu.com/")
        page.screenshot(path=f"output/example-{browser_type.name}.png")

        page.close()
