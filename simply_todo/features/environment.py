import os
import sys
import time
import logging
import django
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# === Logger Setup ===
log_dir = os.path.join(os.getcwd(), "test_logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"behave_log_{time.strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def before_all(context):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simply_todo.settings')
    django.setup()
    logging.info("🚀 Django initialized")

def before_scenario(context, scenario):
    logging.info(f"\n--- SCENARIO: {scenario.name} ---")
    try:
        context.browser = webdriver.Chrome()
        context.browser.implicitly_wait(5)
    except WebDriverException as e:
        logging.error(f"Browser failed to launch: {e}")
        raise

def after_scenario(context, scenario):
    if scenario.status == "failed":
        logging.error(f"❌ Scenario FAILED: {scenario.name}")
    else:
        logging.info(f"✅ Scenario PASSED: {scenario.name}")
    if hasattr(context, "browser"):
        context.browser.quit()
        del context.browser
        time.sleep(1)

def before_step(context, step):
    logging.info(f"STEP: {step.name}")

def after_step(context, step):
    if step.status == "failed":
        logging.error(f"❌ Step FAILED: {step.name}")
        logging.error(f"   Error: {step.exception}")
        try:
            logging.error(f"   URL: {context.browser.current_url}")
        except Exception:
            logging.warning("   Browser closed before URL could be captured")
    elif step.status == "passed":
        logging.info(f"✅ Step PASSED")

def after_all(context):
    logging.info("🎯 All scenarios completed")
