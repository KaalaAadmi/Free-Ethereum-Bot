from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys 
import time

username = "<Enter your email ID>"
password = "<Enter your password>"
driver = webdriver.Edge(executable_path=r'<Path to your web driver>')
time.sleep(5)
driver.get("https://freeethereum.com/free")

time.sleep(10)

username = driver.find_element_by_xpath('/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input').send_keys(username)
password = driver.find_element_by_xpath('/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input').send_keys(password)
cross = driver.find_element_by_xpath('/html/body/div[3]/span').click()
loginBtn = driver.find_element_by_xpath('/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button').click()
time.sleep(7)
while 1:
    roll = driver.find_element_by_xpath('/html/body/main/div/div/div/div/div/div[5]/button').click()
    print('1 hour wait starts now')
    time.sleep(10)
    survey_cross = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/span').click()
    time.sleep(60*60)
    time.sleep(10)
    driver.refresh()
    time.sleep(10)