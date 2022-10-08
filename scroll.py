# from ast import main
# from xml.etree.ElementInclude import LimitedRecursiveIncludeError
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys



s = Service("/home/zec/Downloads/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get("https://www.apmaritime.com/en-gb/Exhibit/exhibitor-directory.html")

time.sleep(5)

driver.find_element(By.ID,'onetrust-accept-btn-handler').click()

# body = driver.find_element(By.CSS_SELECTOR,'body')
# body.send_keys(Keys.PAGE_DOWN)
# time.sleep(3)

# divs = driver.find_elements(By.XPATH,'//div[@class = "flexible-content "]')

links = []


driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
time.sleep(10)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
time.sleep(10)

divs = driver.find_elements(By.CLASS_NAME,'flexible-content')
n = 1
for i in divs:
    a = i.find_element(By.TAG_NAME,'a')
    link = a.get_attribute('href')
    print(link)

    links.append(link)
    n = n+1
    # time.sleep(1)
    print(len(links))
    # if (len(links)==1):
    #     driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    #     time.sleep(10)

    # if (len(links)==99):
    #     driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    #     time.sleep(10)



print(len(links))
    


