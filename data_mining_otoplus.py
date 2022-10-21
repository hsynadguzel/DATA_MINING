from selenium import webdriver
from time import sleep
# Data manipulation
import pandas as pd
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:/Users/....../Desktop/chromedriver.exe")

driver.get("https://www.otoplus.com/autos_c84?utm_source=google&utm_medium=cpc&utm_campaign=search-branding-standard-B2C-Turkey-tIS&utm_content=branding-ALL-standard-observation-purebrand-exact&utm_term=e_letgo%20oto%20plus&gclid=Cj0KCQjw-fmZBhDtARIsAH6H8qh5ZtsHa471VL44BS2PYQuhPobQpYx6UlFFt3kVGTDdMU9g3t1PsOIaAnTAEALw_wcB")
sleep(15)

# veri xpath
item_title = driver.find_elements("xpath", '//*[@id="container"]/main/div/div/section/div/div/div[6]/div[2]/div/div[2]/ul/li[*]/a/div/div[2]/div[2]')
item_price = driver.find_elements("xpath", '//*[@id="container"]/main/div/div/section/div/div/div[6]/div[2]/div/div[2]/ul/li[*]/a/div/div[2]/div[1]/span')
item_fuel = driver.find_elements("xpath", '//*[@id="container"]/main/div/div/section/div/div/div[6]/div[2]/div/div[2]/ul/li[*]/a/div/div[2]/div[3]')

# boş liste
titles_list = []
prices_list = []
fuels_list = []

# döngü ile verilerin hepsini alma
for title in item_title:
    titles_list.append(title.text)
for price in item_price:
    prices_list.append(price.text)
for fuel in item_fuel:
    fuels_list.append(fuel.text)

# dolu listeyi yazdırma
print(titles_list)
print(prices_list)
print(fuels_list)

# ekrana tablo olarak yazdırma 
dfs = pd.DataFrame(zip(titles_list, prices_list, fuels_list), columns=['Marka', 'Fiyat', 'Özellik'])
print("----------------------------------------------------")
print(dfs)