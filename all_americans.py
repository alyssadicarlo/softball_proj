import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

DRIVER_PATH = 'chromedriver'

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

browser = webdriver.Chrome(executable_path='chromedriver', options=options)

browser.get("https://nfca.org/category/ncaa-i?awarddivision=ncaa-i&awardtype=all-american&awardyear=2022")

df = []

headers = ['pos', 'player', 'school']

rows = browser.find_elements(By.XPATH, "//div[@class='all-region-row']")

for row in rows:
    df_row = []
    columns = row.find_elements(By.XPATH, "./div")
    for column in columns:
        df_row.append(column.text)

    df.append(df_row)

pd_df = pd.DataFrame(df)

pd_df.to_csv('all_americans.csv', header=headers)
