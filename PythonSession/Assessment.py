from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
print(driver.title)


driver.find_element(By.ID, 'user-name').send_keys("standard_user")
driver.find_element(By.ID, 'password').send_keys("secret_sauce")
driver.find_element(By.ID, 'login-button').click()
driver.implicitly_wait(300)

driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
driver.find_element(By.ID, 'checkout').click()
driver.find_element(By.ID, 'first-name').send_keys("TOMMY")
driver.find_element(By.ID, 'last-name').send_keys("bobby")
driver.find_element(By.ID, 'postal-code').send_keys("23423")
driver.find_element(By.ID, 'continue').click()
driver.find_element(By.ID, 'finish').click()
order_placed = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
if order_placed:
    print("Order is successfully placed")
else:
    print("order is not placed")
driver.close()
