from selenium import webdriver
# from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd 
from selenium.webdriver.chrome.options import Options

from tqdm import tqdm

total_iterrations = 100

for i in tqdm(range(total_iterrations), 
              desc="Processing", ncols=100):
    time.sleep(0.1)

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

URL = 'https://bidv.com.vn/vn/ty-gia-ngoai-te'

driver.get(URL)
# time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
table = soup.find('table',{'class':'table-reponsive border-bottom'}).find_all('span',{'class':'mobile-content ng-binding'})

header = soup.find('tr')
key = header.text.strip().splitlines()

danh_sach = []
for span in table:
    danh_sach.append(span.text)

danh_sach1 = []
for i in range(int(len(danh_sach)/5)):

    value = [danh_sach[0+5*i],danh_sach[1+5*i],danh_sach[2+5*i],danh_sach[3+5*i],danh_sach[4+5*i]]
    new_dict = dict(zip(key,value))
    danh_sach1.append(new_dict)


df = pd.DataFrame(danh_sach1)
print(df)
# print(df.to_csv('bidv.csv',encoding='utf-8-sig'))
# Xpath https://scrapinghub.github.io/xpath-playground/ 
# Vào link trên để Xpath



