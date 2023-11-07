import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Chrome()
if not os.path.exists('BUOC3'):
    os.mkdir('BUOC3')
A=[]
file_contents=[]
for filename in os.listdir('E:/Code/BTL_KPW/filetext'):
    if filename.endswith('.txt'):
        with open(os.path.join('E:/Code/BTL_KPW/filetext', filename), 'r', encoding='utf-8') as file:
            file_contents = file.read()
url_list = file_contents.split('\n')
Tensp=[]
for i in range(len(url_list)):
    a=url_list[i].replace('https://fptshop.com.vn/may-tinh-xach-tay/','').replace('=','-').replace('?','-')
    Tensp+=[a]
# Loại bỏ các URL trống (nếu có)
count=0
url_list = [url for url in url_list if url.strip()]

for k in range(168,len(url_list)):
    print("Bắt đầu crawl link thứ ",k,'... ',url_list[k])
    url=url_list[k]
    driver.get(url)
    ten=driver.find_elements(By.CSS_SELECTOR,'h1.st-name')
    gia=driver.find_elements(By.CSS_SELECTOR,'div.st-price-main')
    giagoc=driver.find_elements(By.CSS_SELECTOR,'div.st-price-sub')
    thongtin=driver.find_elements(By.CSS_SELECTOR,'div.st-param')
    for i in range(len(ten)):
        chitiet=thongtin[i].find_elements(By.TAG_NAME,'li')
        filename = f'BUOC3/sp{k+1}-{Tensp[k]}.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write('Ten: '+ten[i].text+'\n')
            if len(gia)!=0:
                file.write('Gia: '+gia[i].text+'\n')
            if len(giagoc)!=0:
                file.write('Gia Goc: '+giagoc[i].text+'\n')
            file.write('Chi tiet: ')
            for j in chitiet:
                file.write('- '+j.text+'\n')
    print("Crawl hoàn tất link ",k,'... ',url_list[i])
