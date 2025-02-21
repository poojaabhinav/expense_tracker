from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
driver.get("http://127.0.0.1:5001/add")

# Fill form
driver.find_element(By.NAME, "category").send_keys("Food")
driver.find_element(By.NAME, "amount").send_keys("10")
driver.find_element(By.NAME, "description").send_keys("Lunch")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)  # Wait for redirect
driver.get("http://127.0.0.1:5001")

assert "Food" in driver.page_source
assert "$10" in driver.page_source

print("Test Passed!")
driver.quit()
