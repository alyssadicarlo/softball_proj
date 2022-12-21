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

browser.get("https://d1softball.com/statistics/")

df = []

headers = ['player', 'team', 'position', 'batting_average', 'obp', 'slugging_percentage', 'ops', 'games_played', 'at_bats', 'runs', 'hits', 'doubles', 'triples', 'homeruns', 'rbi', 'hit_by_pitch', 'walks', 'strikeouts', 'stolen_bases', 'caught_stealing']

while True:
    rows = browser.find_elements(By.XPATH, "//table[@id='batting-stats']/tbody/tr")

    for row in rows:
        df_row = []
        columns = row.find_elements(By.XPATH, "./td")
        for column in columns:
            print(column.text)
            df_row.append(column.text)
        
        df.append(df_row)

    # Need to move screen down before button is clickable
    # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='batting-stats_next']"))).click()

    try:
        next_button = browser.find_element(By.ID, 'batting-stats_next')
        next_button.click()
    except:
        break

pd_df = pd.DataFrame(df)

pd_df.to_csv('softball_data.csv', header=headers)