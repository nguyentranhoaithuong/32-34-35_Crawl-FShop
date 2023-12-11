from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re
import time

output_folder = 'D:\Khai_pha_web\BaoCao\B4_BinhLuan'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_folder_no_cmt = 'D:\Khai_pha_web\BaoCao\B4_BinhLuan\SP_Khong_Co_Danh_Gia'
if not os.path.exists(output_folder_no_cmt):
    os.makedirs(output_folder_no_cmt)

def clean_filename(filename):
    cleaned_filename = re.sub(r'[\\/*?:"<>|]', '', filename)
    return cleaned_filename

def CrawlComment(driver):
    comments = []

    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'root-review')))
        review_element = driver.find_element(By.ID, 'root-review')
        try:
            WebDriverWait(review_element, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.user-block')))
            comment_elements = review_element.find_elements(By.CSS_SELECTOR, '.user-block')

            for comment_element in comment_elements:
                try:
                    NguoiDung = comment_element.find_element(By.CSS_SELECTOR, '.avatar-name .text').text
                    BinhLuan = comment_element.find_element(By.CSS_SELECTOR, '.avatar-para .text').text
                    NgayDang = comment_element.find_element(By.CSS_SELECTOR, '.avatar-time .text.text-grayscale').text

                    text = f"Người dùng: {NguoiDung}\nNgày đăng: {NgayDang}\nBình luận: {BinhLuan}\n------------------------------------\n"
                    comments.append(text)
                except StaleElementReferenceException:
                    comment_elements = review_element.find_elements(By.CSS_SELECTOR, '.user-block')
                    time.sleep(3)
                    continue
                except NoSuchElementException:
                    pass
        except TimeoutException:
            pass
    except NoSuchElementException:
        pass

    return comments

def CrawlCommentAllPages():
    driver = webdriver.Chrome()
    spKhongCoCmt = []

    SoThuTu = 1

    with open('D:\Khai_pha_web\BaoCao\B1_urlSP\B1_Link.txt', 'r') as file:
        for line in file:
            url = line.strip()
            driver.get(url)

            TenSP = url.split('/')[-1]
            TenSP = clean_filename(TenSP)
            TenSP_STT = f"blsp{SoThuTu}_{TenSP}"

            comments = []

            while True:
                comments.extend(CrawlComment(driver))

                try:
                    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'root-review')))
                    review_element = driver.find_element(By.ID, 'root-review')
                    next_page_element = review_element.find_element(By.CSS_SELECTOR, "ul.pagination a.pagination-link i.cm-ic-angle-right")
                    next_page_element.click()
                    time.sleep(3)
                except NoSuchElementException:
                    break

            if comments:
                output_file_path = os.path.join(output_folder, f"{TenSP_STT}.txt")
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    for comment in comments:
                        f.write(comment)
                print(f'Đã lưu: {TenSP_STT}.txt {url}')
            else:
                spKhongCoCmt.append(TenSP_STT)
                print(f"Không có đánh giá: {url}")

            SoThuTu += 1

    filename = os.path.join(output_folder_no_cmt, "KhongCoDanhGia.txt")
    with open(filename, 'w', encoding='utf-8') as f:
        for TenSP in spKhongCoCmt:
            f.write(f"{TenSP} \n")

    driver.quit()

CrawlCommentAllPages()