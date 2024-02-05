from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set up Chrome driver using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the URL
driver.get("https://www.valuepitch.ai/crc-form")

# Perform automation tasks
# ...
#create a list to add xpath
list = ["//input[@id='form1-Name--1116147573']","(//div[@class='form-input-component-wrapper'])[2]"]
time.sleep(3)
actions = ActionChains(driver)

# Enter name
# name = driver.find_element(By.ID, "form1-Name--1116147573")
# actions.send_keys_to_element(name, "Admin").perform()

# Enter email
# email = driver.find_element(By.XPATH, "(//div[@class='form-input-component-wrapper'])[2]")
# actions.send_keys_to_element(email, "admin@admin.com").perform()
#LOOP OVER THE LIST
for i in list:
    name = driver.find_element(By.XPATH, i)
    actions.send_keys_to_element(name, "Admin").perform()

time.sleep(3)
# Quit the driver
driver.quit()