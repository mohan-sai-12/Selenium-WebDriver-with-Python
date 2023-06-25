import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Creating an object for Options
chrome_options = Options()

# This will resolve the error if chrome browser is closing automatically after opening.
chrome_options.add_experimental_option("detach", True)

# This will create an object for Service where we need to provide the chromedriver.exe path
sev_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")

# This will open chrome browser
driver = webdriver.Chrome(service=sev_obj,options=chrome_options)

# This will maximize browser window.
driver.maximize_window()

# This will create object for WebDriverWait.
wait = WebDriverWait(driver,8)

# This will open google.com
driver.get('https://www.google.com')

# This will find element search box on chrome.
Search = driver.find_element(By.NAME,'q')

# This will send amazon to search box.
Search.send_keys("amazon")

# This submit is used as Enter key in keyboard
Search.submit()

# This  statement will wait till element is available but for 8 seconds only and moves to next step
link = wait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Amazon.in']")))

# This will click on amazon.in link
link.click()
