from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@when('I update the task titled "{old}" to "{new}"')
def step_impl(context, old, new):
    edit_button = context.browser.find_element(By.XPATH, f"//tr[td[contains(text(), '{old}')]]//a[contains(@href, 'edit')]")
    edit_button.click()
    title_input = context.browser.find_element(By.NAME, "title")
    title_input.clear()
    title_input.send_keys(new)
    context.browser.find_element(By.ID, "submit").click()

