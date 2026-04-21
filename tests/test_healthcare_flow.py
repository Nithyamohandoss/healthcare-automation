import sys
import time

from pathlib import Path

# Project root (portable; works on any machine / CI checkout)
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.driver_setup import get_driver
from pages.login_page import LoginPage


def test_healthcare_enrollment():
    driver = get_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/login")

        login = LoginPage(driver)
        login.login("tomsmith", "SuperSecretPassword!")

        WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
        assert "You logged into a secure area!" in driver.page_source
        assert "You logged into a secure area!" in driver.page_source
        # time.sleep(15)
        # Removing sleep since it's not necessary!!
        driver.get("https://www.google.com")
        time.sleep(1)
    finally:

        driver.quit()