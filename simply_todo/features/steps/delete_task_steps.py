from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I have a task titled "{task}"')
def step_impl(context, task):
    # Precondition: Add task for deletion
    context.browser.get('http://127.0.0.1:8000/tasks/add')
    context.browser.find_element(By.NAME, "title").send_keys(task)
    context.browser.find_element(By.ID, "submit").click()

@when('I delete the task titled "{task}"')
def step_impl(context, task):
    delete_button = context.browser.find_element(By.XPATH, f"//tr[td[contains(text(), '{task}')]]//a[contains(@href, 'delete')]")
    delete_button.click()

@then('I should not see "{task}" in the task list')
def step_impl(context, task):
    assert task not in context.browser.page_source
    context.browser.quit()
