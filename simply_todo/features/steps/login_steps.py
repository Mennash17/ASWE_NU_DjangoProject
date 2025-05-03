import os
import django
import sys
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simply_todo.settings")
django.setup()




from django.contrib.auth.models import User

@given("I am on the login page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://127.0.0.1:8000/tasks/login/")
    time.sleep(1)


@when("I enter a valid username and password")
def step_impl(context):
    user, created = User.objects.get_or_create(username="testuser")
    user.set_password("TtesTtPass")
    user.save()
    
    context.browser.find_element(By.NAME, "username").send_keys("testuser")
    context.browser.find_element(By.NAME, "password").send_keys("TtesTtPass")


@when("I press the login button")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)


@then("I should see the dashboard")
def step_impl(context):
    assert "dashboard" in context.browser.page_source.lower() or "todo" in context.browser.title.lower()
    context.browser.quit()
