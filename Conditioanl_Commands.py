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
driver.get("https://www.facebook.com/signup")

# These below lines will find the location of radio buttons in signup page.
rb_female = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input")
rb_male = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input")

# This is_displayed() command will check whether element is displayed or not. If displayed will give True else false
print("Radio button for female : ",rb_female.is_displayed())

# This is_enabled() command will check whether element is enabled to click or pass values. If enabled will give True else false
print("Radio button for female : ",rb_female.is_enabled())

# This is_selected() command will check whether element is selected or not. If selected will give True else false
print("Status of radio button for female before selection : ",rb_female.is_selected())

rb_female.click()

# This is_selected() command will check whether element is selected or not. If selected will give True else false
print("Status of radio button for female after selection : ",rb_female.is_selected())

# This is_displayed() command will check whether element is displayed or not. If displayed will give True else false
print("Radio button for male : ",rb_male.is_displayed())

# This is_enabled() command will check whether element is enabled to click or pass values. If enabled will give True else false
print("Radio button for male : ",rb_male.is_enabled())

# This is_selected() command will check whether element is selected or not. If selected will give True else false
print("Status of radio button for male before selection : ",rb_male.is_selected())

rb_male.click()

# This is_selected() command will check whether element is selected or not. If selected will give True else false
print("Status of radio button for male after selection : ",rb_male.is_selected())




