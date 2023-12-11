
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os

driver = webdriver.Chrome()
All_LinksBao = set()

driver.get(f'https://fptshop.com.vn/may-tinh-xach-tay?sort=ban-chay-nhat&trang=15')
LinksBao = driver.find_elements(By.CSS_SELECTOR, 'div.cdt-product__info')
for link in LinksBao:
    try:
        links = link.find_elements(By.TAG_NAME, 'a')
        for a in links:
            href = a.get_attribute('href')
            if "https://fptshop.com.vn/so-sanh-san-pham?" not in href:
                All_LinksBao.add(href)
    except NoSuchElementException:
        pass

output_folder = 'D:\Khai_pha_web\BaoCao\B1_urlSP'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

filename = os.path.join(output_folder, "B1_Link.txt")
with open(filename, 'w', encoding='utf-8') as file:
    for link in All_LinksBao:
        file.write(link + '\n')

