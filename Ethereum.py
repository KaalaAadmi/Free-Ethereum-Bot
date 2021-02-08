from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys 
import time

username = "<Enter your email ID>"
password = "<Enter your password>"
driver = webdriver.<Browser Name>(executable_path=r'<Path to your web driver>')
time.sleep(5)
driver.get("https://freeethereum.com/free")

time.sleep(10)

username = driver.find_element_by_xpath('/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[1]/input').send_keys(username)
password = driver.find_element_by_xpath('/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/div[2]/input').send_keys(password)
driver.fullscreen_window()
loginBtn = driver.find_element_by_xpath('/html/body/main/section/section[1]/div/div/div[2]/div/div[1]/button').click()
time.sleep(7)
driver.fullscreen_window()
while 1:
    time.sleep(10)
    driver.switch_to.window(driver.current_window_handle)
    roll = driver.find_element_by_xpath('/html/body/main/div/div/div/div/div/div[5]/button').click()
    print('1 hour wait starts now')
    time.sleep(15)
    driver.refresh()
    time.sleep(60*60)
    time.sleep(10)
    driver.refresh()
