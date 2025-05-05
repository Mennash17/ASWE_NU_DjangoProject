from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I am on the "Add Task" page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://127.0.0.1:8000/tasks/add')

@when('I fill in "Title" with "{title}"')
def step_impl(context, title):
    context.browser.find_element(By.NAME, "title").send_keys(title)

@when('I fill in "Due Date" with "{date}"')
def step_impl(context, date):
    context.browser.find_element(By.NAME, "due_date").send_keys(date)

@when('I press "Add Task"')
def step_impl(context):
    context.browser.find_element(By.ID, "submit").click()

@then('I should see "{task}" in the task list')
def step_impl(context, task):
    assert task in context.browser.page_source
    context.browser.quit()
