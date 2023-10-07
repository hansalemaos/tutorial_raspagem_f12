import re
from time import sleep

import bs4
from seleniumbase import Driver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from a_selenium2df import get_df
from PrettyColorPrinter import add_printer

add_printer(1)


def obter_dataframe(query="*"):
    df = pd.DataFrame()
    while df.empty:
        df = get_df(
            driver,
            By,
            WebDriverWait,
            expected_conditions,
            queryselector=query,
            with_methods=True,
        )
    return df


driver = Driver(uc=True)
sleep(2)
driver.get("https://f12.bet/prejogo/?btag=a_2089b_36c_#league/2417-undefined")
sleep(5)
while True:
    try:
        df = obter_dataframe(query="tr")
        df= df.aa_innerHTML.apply(bs4.BeautifulSoup).apply(lambda soup: [x.text.strip() for x in soup.find_all('td')]).apply( lambda x: [x[0]] + x[1].split(' - ') + x[2:] if '|' in x[0] else pd.NA).dropna().apply(pd.Series)[list(range(4)) + [5, 7]].rename( columns={1: 'team1_nome', 2: 'team2_nome', 0: 'data' , 3: 'team1', 5: 'empate', 7: 'team2'}).astype({'team1': 'Float64', 'empate': 'Float64', 'team2': 'Float64'} ).reset_index(drop=True)
        break
    except Exception as e:
        print(e)
        sleep(2)
