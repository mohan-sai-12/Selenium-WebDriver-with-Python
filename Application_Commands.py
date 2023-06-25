from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

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
driver.get("https://facebook.com/")

# This TITLE command will print the title of current page
print(driver.title)

# This CURRENT_URL command will print the currnet url which is opend
print(driver.current_url)

# This PAGE_SOURCE command will show the source code of current page.
print(driver.page_source)