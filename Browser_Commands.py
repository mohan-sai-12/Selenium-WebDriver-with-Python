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

# This will maximize browser window.
driver.maximize_window()

# This GET command will open facebook.
driver.get("https://www.amazon.com/")

# This will click on amazon.in page link present in amazon.com page
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div/a").click()

time.sleep(3)

# This will close amazon.com page but amazon.in will be still opened i.e. close() command will close parent browser.
driver.close()

driver1 = webdriver.Chrome(service=sev_obj,options=chrome_options)

# This will maximize browser window.
driver1.maximize_window()

# This GET command will open facebook.
driver1.get("https://www.amazon.com/")

# This will click on amazon.in page link present in amazon.com page
driver1.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[1]/div/a").click()

time.sleep(5)

# This will close chrome browser i.e. quit() command will close directly the driver.
driver1.quit()