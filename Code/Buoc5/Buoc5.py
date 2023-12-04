import os
import re
from underthesea import word_tokenize
from emot.emo_unicode import UNICODE_EMOJI, EMOTICONS_EMO
 

for filename in os.listdir('D:\Khai pha web\CK\Cmt_raw'):
    if filename.endswith('.txt'):
        with open(os.path.join('D:\Khai pha web\CK\Cmt_raw', filename), 'r', encoding='utf-8') as file:
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
            text_pre=re.sub(r'[^\w\s]','',text_pre) # Remove punctuation
            text_pre = re.sub("\d+", " ", text_pre) # Remove number
            text_pre = re.sub(r"[!@#$[]()]'", "", text_pre) # Remove character: !@#$[]()

            path = os.path.join("D:/Khai pha web/CK")
            with open(path + r"\vietnamese-stopwords.txt", "r", encoding="utf-8") as f:
                list_stopwords = f.read().splitlines()
            
            text_pre = " ".join(word for word in word_tokenize(text_pre) if word not in list_stopwords)  # Remove stop words

        output_filename = filename.replace('raw', 'TXL')
        output_filepath = os.path.join('D:\Khai pha web\CK\TXLCMT', output_filename)
        with open(output_filepath, 'w', encoding='utf-8') as output_file:
            output_file.write(str(text_pre))  # Chuyển về chuỗi trước khi ghi

        print(f'Saved preprocessed file as: {output_filepath}')
