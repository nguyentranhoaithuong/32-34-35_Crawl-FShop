import os
import re

output_folder = 'D:\Khai_pha_web\BaoCao\B5_ChuanHoaCmt'

if not os.path.exists(output_folder ):
    os.makedirs(output_folder)

lookup_dict = {}
filename = os.path.join("D:\Khai_pha_web\BaoCao\Code", "teencode.txt")
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        pair = line.strip().split('\t')
        if len(pair) == 2:
            lookup_dict[pair[0]] = pair[1]

def teencode(input_text):
    lines = input_text.split('\n')
    text_pre = ""
    for line in lines:
        words = line.lower().split()
        for word in words:
            w = re.sub(r'[^\w\s]', '', word)
            if w in lookup_dict:
                word = lookup_dict[w]
            text_pre = text_pre + " " + word
        text_pre += '\n'      
    return text_pre

for filename in os.listdir('D:\Khai_pha_web\BaoCao\B4_BinhLuan'):
    if filename.endswith('.txt'):
        with open(os.path.join('D:\Khai_pha_web\BaoCao\B4_BinhLuan', filename), 'r', encoding='utf-8') as file:
            text = file.read()

            pattern = re.compile(r"-+|Người dùng: .*|Ngày đăng: .*|Bình luận: ")
            text_pre = re.sub(pattern, '', text)

            text_pre = teencode(text_pre)

            output_filename = filename.replace('blsp', 'rawCMTSP')
            output_filepath = os.path.join(output_folder, output_filename)
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                output_file.write(text_pre)

            print(f'Đã lưu: {output_filepath}')