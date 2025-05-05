import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from tasks.models import Task
from datetime import datetime

@given('a user "taskuser" with password "taskpass" exists')
def step_impl(context):
    user, created = User.objects.get_or_create(username="taskuser")
    user.set_password("taskpass")
    user.save()

@given('I am logged in as "taskuser"')
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000/tasks/login/")
    context.browser.find_element(By.NAME, "username").send_keys("taskuser")
    context.browser.find_element(By.NAME, "password").send_keys("taskpass")
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(1)

@given("I am on the task dashboard")
def step_impl(context):
    assert "dashboard" in context.browser.page_source.lower() or "task" in context.browser.title.lower()

@when('I click the "Add Task" button')
def step_impl(context):
    add_button = context.browser.find_element(By.LINK_TEXT, "Add Task")
    add_button.click()
    time.sleep(1)

@when("I fill the form with:")
def step_impl(context):
    form_data = {row['title']: row['description'] for row in context.table}
    for key, value in form_data.items():
        field = context.browser.find_element(By.NAME, key)
        field.clear()
        field.send_keys(value)
    time.sleep(1)

@when("I submit the task form")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(1)

@then('I should see "{task_title}" in the task list')
def step_impl(context, task_title):
    page_text = context.browser.page_source
    assert task_title in page_text

@given('I have a task titled "{title}"')
def step_impl(context, title):
    user = User.objects.get(username="taskuser")
    Task.objects.get_or_create(
        user=user,
        title=title,
        description="Sample task",
        category="Work",
        priority="Medium",
        due_date=datetime.today().date()
    )

@when('I click the edit button for "{title}"')
def step_impl(context, title):
    edit_button = context.browser.find_element(By.XPATH, f"//td[contains(text(), '{title}')]/..//a[contains(text(),'Edit')]")
    edit_button.click()
    time.sleep(1)

@when('I update the title to "{new_title}"')
def step_impl(context, new_title):
    title_field = context.browser.find_element(By.NAME, "title")
    title_field.clear()
    title_field.send_keys(new_title)
    time.sleep(1)

@when("I save the changes")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(1)

@when('I click the delete button for "{title}"')
def step_impl(context, title):
    delete_button = context.browser.find_element(By.XPATH, f"//td[contains(text(), '{title}')]/..//a[contains(text(),'Delete')]")
    delete_button.click()
    time.sleep(1)

@when("I confirm the deletion")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()
    time.sleep(1)

@then('I should not see "{title}" in the task list')
def step_impl(context, title):
    page_text = context.browser.page_source
    assert title not in page_text
