import time

from path import Path

from playwright.sync_api import sync_playwright
from util import holdon

# `sync_playwright` is a context manager, so we need to call start for general use
p = sync_playwright().start()

browser_type = p.chromium
browser = browser_type.launch(headless=False)
context = browser.new_context(accept_downloads=True)

page = context.new_page()

# use ant design component for test
page.goto("https://ant.design/components/date-picker-cn")

# load js and render
page.wait_for_load_state("domcontentloaded")

# get date input
item = page.query_selector("//input[@placeholder='请选择日期']")
item.evaluate("n => n.removeAttribute('readonly')")
item.hover()
item.click()

# delay to show the date picker detail
page.wait_for_timeout(2 * 1000)


# ref: https://www.lambdatest.com/learning-hub/automate-date-pickers-with-playwright
date_input = page.query_selector(
    "#components-date-picker-demo-basic > section.code-box-demo > div > div:nth-child(1) > div > div > input"
)
print("origin: ", date_input.input_value())
date_input.click()

value = "2023-01-01"
date_input.fill(value=value, force=True)

# FIXME: for antd picker, we need a click item to fill in
page.click(
    "body > div:nth-child(11) > div > div > div > div > div.ant-picker-date-panel > div.ant-picker-body > table > tbody > tr:nth-child(1) > td.ant-picker-cell.ant-picker-cell-start.ant-picker-cell-in-view.ant-picker-cell-selected > div"
)

# now value changed
print("select: ", date_input.input_value())

holdon()
