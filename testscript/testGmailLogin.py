import time
from selenium import webdriver

#Username
#user = "example@gmail.com"
user = "kulkradhika0@gmail.com"

#Password
#pwd = "********"
pwd = "Radha@2002"

#Instantiate Chrome Driver
driverpath="/home/demo/Radhika/selenium_demo/chrome_driver/chromedriver"
driver = webdriver.Chrome(driverpath)

#Open Gmail Page
driver.get("http://www.gmail.com")
#driver.get("http://35.234.51.115:8080")

#Enter username or Email
elem = driver.find_element_by_id("identifierId")
elem.send_keys(user)

driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
time.sleep(2)

#Enter password
elem = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
elem.send_keys(pwd)

time.sleep(2)

#Press submit button for login
driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()

#elem.send_keys(Keys.RETURN)
time.sleep(10)