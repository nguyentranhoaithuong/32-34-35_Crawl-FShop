import os
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

output_folder = 'D:\Khai_pha_web\BaoCao\B3_ThongTinSP'

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

file_contents=[]
for filename in os.listdir('D:\Khai_pha_web\BaoCao\B1_urlSP'):
    if filename.endswith('.txt'):
        with open(os.path.join('D:\Khai_pha_web\BaoCao\B1_urlSP', filename), 'r', encoding='utf-8') as file:
            file_contents = file.read()
url_list = file_contents.split('\n')

Tensp=[]
for i in range(len(url_list)):
    a=url_list[i].replace('https://fptshop.com.vn/may-tinh-xach-tay/','').replace('=','-').replace('?','-')
    Tensp+=[a]

count=0
url_list = [url for url in url_list if url.strip()]

for k in range(0,len(url_list)):
    print("Bắt đầu crawl link thứ ",k,'... ',url_list[k])
    url=url_list[k]
    driver.get(url)
    TenSP=driver.find_elements(By.CSS_SELECTOR,'h1.st-name')
    Gia=driver.find_elements(By.CSS_SELECTOR,'div.st-price-main')
    GiaGoc=driver.find_elements(By.CSS_SELECTOR,'div.st-price-sub')
    ThongTin=driver.find_elements(By.CSS_SELECTOR,'div.st-param')
    for i in range(len(TenSP)):
        ChiTiet=ThongTin[i].find_elements(By.TAG_NAME,'li')
        output_file_path = os.path.join(output_folder, f'sp{k+1}-{Tensp[k]}.txt')
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write('Ten: '+TenSP[i].text+'\n')
            if len(Gia)!=0:
                file.write('Gia: '+Gia[i].text+'\n')
            if len(GiaGoc)!=0:
                file.write('Gia Goc: '+GiaGoc[i].text+'\n')
            file.write('Chi tiet: ')
            for j in ChiTiet:
                file.write('- '+j.text+'\n')
    print("Crawl hoàn tất link ",k,'... ',url_list[i])