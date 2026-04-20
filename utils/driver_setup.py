from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_driver():
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")

    # Selenium 4.6+ resolves ChromeDriver via Selenium Manager (no webdriver_manager / extra download host).
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    return driver