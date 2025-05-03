import os
import sys
import time
import django
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simply_todo.settings")
django.setup()

from django.contrib.auth.models import User



@given("I am on the login page and I click register")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://127.0.0.1:8000/tasks/login/")
    time.sleep(1)
    register_link = context.browser.find_element(By.LINK_TEXT, "Register here")
    register_link.click()
    time.sleep(1)

@when("I enter valid user details and submit")
def step_impl(context):
    username = "newuser"
    password = "StrongPass123"
    context.browser.find_element(By.NAME, "username").send_keys(username)
    context.browser.find_element(By.NAME, "password1").send_keys(password)
    context.browser.find_element(By.NAME, "password2").send_keys(password)
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

@then("I should be redirected to the login page")
def step_impl(context):
    assert "login" in context.browser.current_url.lower()
    context.browser.quit()

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

@then("I should see my task dashboard")
def step_impl(context):
    assert "dashboard" in context.browser.page_source.lower() or "todo" in context.browser.title.lower()
    context.browser.quit()

@when("I enter an incorrect username or password")
def step_impl(context):
    context.browser.find_element(By.NAME, "username").send_keys("wronguser")
    context.browser.find_element(By.NAME, "password").send_keys("wrongpass")

@then("I should see an error message")
def step_impl(context):
    error_elements = context.browser.find_elements(By.CLASS_NAME, "errorlist")
    assert any("invalid" in el.text.lower() for el in error_elements)
    context.browser.quit()
