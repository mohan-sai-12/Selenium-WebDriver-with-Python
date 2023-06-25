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

# These below 2 lines will send "helloall@gmail.com" to username box in login page.
# This is an example to find an element by using TAG & ID locator.
# SYNTAX : "TAGNAME#ID" or "#ID"
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("helloall@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("helloall@gmail.com")

# This will send "helloall@gmail.com" to username box in login page.
# This is an example to find an element by using TAG & CLASS locator.
# SYNTAX : "TAGNAME.CLASS" or ".CLASS"
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("helloall@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("helloall@gmail.com")

# This will send "helloall@gmail.com" to username box in login page.
# This is an example to find an element by using TAG & ATTRIBUTE locator.
# SYNTAX : "TAGNAME[ATTRIBUTE=VALUE]" or "[ATTRIBUTE=VALUE]"
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("helloall@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("helloall@gmail.com")

# This will send "helloall@gmail.com" to username box in login page.
# This is an example to find an element by using TAG, CLASS & ATTRIBUTE locator.
# SYNTAX : "TAGNAME.CLASS[ATTRIBUTE=VALUE]"
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("helloall@gmail.com")

# This will send "helloall@gmail.com" to username box in login page.
# This is an example to find an element by using ABSOLUTE XPATH or FULL XPATH  locator.
# driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("helloall@gmail.com")


# This will send "helloall@gmail.com" to username box in login page.
# This is an example to find an element by using  RELATIVE XPATH or PARTIAL XPATH locator.
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("helloall@gmail.com")
