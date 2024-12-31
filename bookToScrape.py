import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=options)

driver.get('https://books.toscrape.com/catalogue/page-48.html')

actions = ActionChains(driver)

data = []

check_button_next = bool(driver.find_elements(By.XPATH, "//li[@class='next']//a"))

number = 0

while check_button_next:
    try:
        
        books = driver.find_elements(By.XPATH, "//article[@class='product_pod']")
        
        for book in books:
            
            title = book.find_element(By.XPATH, ".//h3//a").get_attribute("title")
            
            price = book.find_element(By.XPATH, ".//div[@class='product_price']//p[@class='price_color']").text
            
        
            
            number += 1
            
            data.append("No: " + str(number) + " Title: " + title + "Price: " + price)
        
        driver.find_element(By.XPATH, "//li[@class='next']//a").click()
    
    except:
        check_button_next = False
        print(len(data))
        print("Page has reach final page")

# print(data)

df = pd.DataFrame(data)

df.to_csv("perkedel.csv", index=False)

driver.quit()

