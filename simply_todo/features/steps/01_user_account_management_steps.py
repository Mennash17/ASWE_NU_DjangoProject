import os
import sys
import time
import django
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

# Django setup
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simply_todo.settings")
django.setup()

from django.contrib.auth.models import User


def start_browser(context):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(5)


def stop_browser(context):
    context.browser.quit()


@given("I open the application")
def step_open_app(context):
    start_browser(context)


@given("I am on the login page")
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000/tasks/login/")


@given("I am on the login page and I click register")
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000/tasks/login/")
    register_link = context.browser.find_element(By.LINK_TEXT, "Register here")
    register_link.click()


@given("I am on the registration form")
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000/tasks/register/")


@when("I fill in a unique username and matching passwords")
def step_impl(context):
    username = "TestUser3"
    password = "StrongPass123"
    context.browser.find_element(By.NAME, "username").send_keys(username)
    context.browser.find_element(By.NAME, "password1").send_keys(password)
    context.browser.find_element(By.NAME, "password2").send_keys(password)


@when("I fill in a unique username and mismatched passwords")
def step_impl(context):
    context.browser.find_element(By.NAME, "username").send_keys("MismatchUser")
    context.browser.find_element(By.NAME, "password1").send_keys("Pass1234")
    context.browser.find_element(By.NAME, "password2").send_keys("WrongPass")


@when('I fill in the username "menna" with valid passwords')
def step_impl(context):
    context.browser.find_element(By.NAME, "username").send_keys("menna")
    context.browser.find_element(By.NAME, "password1").send_keys("StrongPass123")
    context.browser.find_element(By.NAME, "password2").send_keys("StrongPass123")


@given('a user "menna" already exists')
def step_impl(context):
    if not User.objects.filter(username="menna").exists():
        User.objects.create_user(username="menna", password="StrongPass123")


@when("I submit the registration form")
def step_impl(context):
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(1)


@then("I should be redirected to the login page")
def step_impl(context):
    assert "login" in context.browser.current_url.lower()


@then('I should see a message "Registration successful"')
def step_impl(context):
    page_text = context.browser.page_source.lower()
    assert "registration successful" in page_text or "login" in context.browser.current_url


@then('I should see an error message "Passwords do not match"')
def step_impl(context):
    page_text = context.browser.page_source.lower()
    assert "passwords do not match" in page_text or "error" in page_text


@then('I should see an error message "Username already taken"')
def step_impl(context):
    page_text = context.browser.page_source.lower()
    assert "username already taken" in page_text or "a user with that username" in page_text


@given('a user "testuser" with password "testpass" exists')
def step_impl(context):
    user, _ = User.objects.get_or_create(username="testuser")
    user.set_password("testpass")
    user.save()


@when('I enter "testuser" and "testpass"')
def step_impl(context):
    context.browser.find_element(By.NAME, "username").send_keys("testuser")
    context.browser.find_element(By.NAME, "password").send_keys("testpass")


@when('I enter "wronguser" and "wrongpass"')
def step_impl(context):
    context.browser.find_element(By.NAME, "username").send_keys("wronguser")
    context.browser.find_element(By.NAME, "password").send_keys("wrongpass")


@then("I should be redirected to the dashboard")
def step_impl(context):
    assert "dashboard" in context.browser.page_source.lower() or "todo" in context.browser.title.lower()


@then('I should see a welcome message')
def step_impl(context):
    assert "welcome" in context.browser.page_source.lower()


@then('I should see an error message "Invalid username or password"')
def step_impl(context):
    error_elements = context.browser.find_elements(By.CLASS_NAME, "errorlist")
    assert any("invalid" in el.text.lower() for el in error_elements)


@given('I am logged in as "testuser"')
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000/tasks/login/")
    context.browser.find_element(By.NAME, "username").send_keys("testuser")
    context.browser.find_element(By.NAME, "password").send_keys("testpass")
    context.browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(1)


@when('I click the "Logout" button')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(1)


@then('I should see a message "You have been logged out"')
def step_impl(context):
    assert "logged out" in context.browser.page_source.lower()


@then("I close the browser")
def step_impl(context):
    stop_browser(context)
