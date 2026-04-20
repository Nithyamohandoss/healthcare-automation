from selenium.webdriver.common.by import By

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    view_plans = (By.ID, "viewPlans")
    select_plan = (By.XPATH, "//button[contains(text(),'Select')]")
    confirm_btn = (By.ID, "confirmBtn")

    def select_health_plan(self):
        self.driver.find_element(*self.view_plans).click()
        self.driver.find_element(*self.select_plan).click()
        self.driver.find_element(*self.confirm_btn).click()