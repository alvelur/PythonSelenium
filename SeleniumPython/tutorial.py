from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.saucedemo.com/")

print(driver.title)

username = driver.find_element(By.NAME, 'user-name')
username.send_keys("standard_user")

password = driver.find_element(By.NAME, 'password')
password.send_keys("secret_sauce")

username.send_keys(Keys.ENTER)

try:
    inventory = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )
    
    inventories = driver.find_element(By.CLASS_NAME, "inventory_list" )

    items = inventories.find_elements(By.CLASS_NAME, "inventory_item")
    for item in items:
        title = item.find_element(By.CLASS_NAME, "inventory_item_name")
        print(title.text)
    

finally:
    driver.quit()



##print(driver.page_source)


driver.quit()

