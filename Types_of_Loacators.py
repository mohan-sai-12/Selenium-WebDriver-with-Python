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

# This will open google chrome
driver = webdriver.Chrome(service=sev_obj,options=chrome_options)

# This will maximize browser window
driver.maximize_window()

# This will open facebook website login page.
driver.get("https://www.facebook.com/")

# This will send "helloall@gmail.com" to username box in login page.
# This is an example to find an element by using ID locator.
# driver.find_element(By.ID,"email").send_keys("helloall@gmail.com")

# This will send "helloall@gmail.com" to username box in login page.
# This is an example to find an element by using NAME locator.
# driver.find_element(By.NAME,"email").send_keys("helloall@gmail.com")

# This will click on login in button. This is an example to find an element by using CLASS NAME locator.
# driver.find_element(By.CLASS_NAME,"_6ltg").click()

# This will click on login in button. This is an example to find an element by using TAG NAME locator.
driver.find_element(By.TAG_NAME,"button").click()







