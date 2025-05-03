from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

df = pd.read_excel("listings.xlsx")

driver = webdriver.Chrome()

driver.get("https://your-realestatewebsite.com/admin")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("your_username")
driver.find_element(By.ID, "password").send_keys("your_password")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

for index, row in df.iterrows():
    print(f"Adding Listing {index+1}: {row['Title']}")

    driver.get("https://your-realestatewebsite.com/add-listing")
    time.sleep(2)
    
    driver.find_element(By.NAME, "title").send_keys(row["Title"])
    driver.find_element(By.NAME, "description").send_keys(row["Description"])
    driver.find_element(By.NAME, "price").send_keys(str(row["Price"]))
    driver.find_element(By.NAME, "address").send_keys(row["Address"])
    driver.find_element(By.NAME, "bedrooms").send_keys(str(row["Bedrooms"]))
    driver.find_element(By.NAME, "bathrooms").send_keys(str(row["Bathrooms"]))
    driver.find_element(By.NAME, "property_type").send_keys(row["Type"])
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)

print("All listings added successfully.")
driver.quit()
