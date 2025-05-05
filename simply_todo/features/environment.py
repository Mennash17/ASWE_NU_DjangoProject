import os
import time
import logging
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


# === Lifecycle Hooks ===

def before_all(context):
    logging.info("===== Test Session Started =====")


def before_scenario(context, scenario):
    logging.info(f"\n--- SCENARIO: {scenario.name} ---")
    try:
        # Launch a fresh browser instance
        context.browser = webdriver.Chrome()
        context.browser.implicitly_wait(5)
    except WebDriverException as e:
        logging.error("❌ Failed to launch browser: %s", str(e))
        raise


def after_scenario(context, scenario):
    if scenario.status == "failed":
        logging.error("❌ Scenario FAILED: %s", scenario.name)
    else:
        logging.info("✅ Scenario PASSED: %s", scenario.name)

    # Always close browser
    if hasattr(context, "browser"):
        context.browser.quit()
        time.sleep(1)


def before_step(context, step):
    logging.info(f"STEP: {step.name}")


def after_step(context, step):
    if step.status == "failed":
        logging.error("❌ Step FAILED: %s", step.name)
        logging.error("   Error: %s", step.exception)
        try:
            logging.error("   Current URL: %s", context.browser.current_url)
        except Exception:
            logging.error("   URL not available.")


def after_all(context):
    logging.info("===== Test Session Completed =====\n")
