import os
import re
from underthesea import word_tokenize
from emot.emo_unicode import UNICODE_EMOJI, EMOTICONS_EMO

ThuMucCMT = 'D:\Khai pha web\CK\Cmt_raw'

ThuMucTXL = 'D:\Khai pha web\CK\TXLCMT_CSV'

if not os.path.exists(ThuMucTXL):
    os.makedirs(ThuMucTXL)
    
for ThuMucSP in os.listdir(ThuMucCMT):
    path = os.path.join(ThuMucCMT, ThuMucSP)

    if os.path.isdir(path):
        new_ThuMucSP = ThuMucSP.replace('raw', 'TXL')
        new_path = os.path.join(ThuMucTXL, new_ThuMucSP)

        for PhanLoai in os.listdir(path):
            PhanLoai_Path = os.path.join(path, PhanLoai)

            all_files_content = ''

            for file in os.listdir(PhanLoai_Path):
                if file.endswith('.txt'):
                    with open(os.path.join(PhanLoai_Path, file), 'r', encoding='utf-8') as file:
                        text = file.read()
                        #################################
                        ######## Text Processing ########
                        #################################
                        def converting_emojis(text):
                            for x in EMOTICONS_EMO:
                                text = text.replace(x, "_".join(EMOTICONS_EMO[x].replace(",","").replace(":","").split()))
                                
                            for x in UNICODE_EMOJI:
                                text = text.replace(x, "_".join(UNICODE_EMOJI[x].replace(",","").replace(":","").split()))
                                    
                            return text


                        text_pre=text.replace("\n","")  # Remove the newline command
                        text_pre=text.lower() # Convert text to lowercase
                        text_pre = word_tokenize(text, format="text")
                        text_pre = re.sub(r'[^\w\s_]','',text_pre)
                        text_pre = re.sub("\d+", " ", text_pre) # Remove number
                        text_pre = re.sub(r"!@#$\[\']", "", text_pre) # Remove character: !@#$
                        filename=os.path.join('D:/Khai pha web/CK',"vietnamese-stopwords.txt")
                        with open(filename,'r',encoding='utf-8') as f:
                            List_StopWords=f.read().split("\n")
                        #remove stop words
                        text_pre=" ".join(text for text in text_pre.split() if text not in List_StopWords)
                        all_files_content += str(text_pre) + '\n'

            output_filepath = os.path.join(new_path, PhanLoai + '.txt')
            os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                output_file.write(all_files_content)

            print(f'Đã lưu: {output_filepath}')
