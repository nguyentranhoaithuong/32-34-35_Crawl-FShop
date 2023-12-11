
from selenium import webdriver
import os

driver = webdriver.Chrome()

output_folder = 'D:\Khai_pha_web\BaoCao\B2_MaNguon'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open('D:\Khai_pha_web\BaoCao\B1_urlSP\B1_Link.txt', 'r') as file:
    urls = file.readlines()

for i, url in enumerate(urls):
    url = url.strip()
    driver.get(url)
    html_source = driver.page_source
    output_file_path = os.path.join(output_folder, f'Sp_{i + 1}.html')
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(html_source)

driver.quit()

