from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.spicejet.com/")
time.sleep(3)
#Move to element
login_ele = driver.find_element(By.XPATH, "//div[contains(text(),'Login')]")
act_chain = ActionChains(driver)
act_chain.move_to_element(login_ele).perform

#driver.find_element(By.LINK_TEXT, 'Our Program')
act_chain.move_to_element()
