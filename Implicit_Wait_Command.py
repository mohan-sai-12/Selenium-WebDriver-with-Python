import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Creating an object for Options
chrome_options = Options()

# This will resolve the error if chrome browser is closing automatically after opening.
chrome_options.add_experimental_option("detach", True)

# This will create an object for Service where we need to provide the chromedriver.exe path
sev_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")

# This will open chrome browser
driver = webdriver.Chrome(service=sev_obj,options=chrome_options)

# This implicitly wait will be applicable for all statement in script.
# If the page takes time to load or the element is unavailable, this timer will wait for 8 seconds.
# This will be applicable to all the statements which are below ths line.
driver.implicitly_wait(8)

# This will maximize browser window.
driver.maximize_window()

# This will open google.com
driver.get('https://www.google.com')

# This will find element search box on chrome.
Search = driver.find_element(By.NAME,'q')

# This will send amazon to search box.
Search.send_keys("amazon")

# This submit is used as Enter key in keyboard
Search.submit()

# This will find heading which has amazon.in in it and click on that.
driver.find_element(By.XPATH,"//h3[text()='Amazon.in']").click()