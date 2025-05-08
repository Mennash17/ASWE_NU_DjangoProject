import os
import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from tasks.models import Task
from datetime import datetime

DOWNLOAD_DIR = os.path.join(os.getcwd(), "test_downloads")
EXPORT_FILENAME = "tasks_export.xlsx"


@when('I click the "Export" button')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, "Export").click()
    time.sleep(3)

@then(f'a file named "{EXPORT_FILENAME}" should be downloaded')
def step_impl(context):
    file_path = os.path.join(DOWNLOAD_DIR, EXPORT_FILENAME)
    assert os.path.exists(file_path), f"Expected file '{EXPORT_FILENAME}' not found in {DOWNLOAD_DIR}"
