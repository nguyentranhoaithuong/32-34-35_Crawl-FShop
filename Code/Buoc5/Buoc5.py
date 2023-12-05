import os
import re
from underthesea import word_tokenize
from emot.emo_unicode import UNICODE_EMOJI, EMOTICONS_EMO
from underthesea import word_tokenize
# Đường dẫn đến thư mục chứa các bình luận
root_dir = 'E:\Code\BTL_KPW\Cmt_raw'

# Đường dẫn đến thư mục TXLCMT
txl_dir = 'E:\Code\BTL_KPW\TXLCMT'

# Kiểm tra xem thư mục TXLCMT có tồn tại hay không
if not os.path.exists(txl_dir):
    # Nếu không, tạo thư mục
    os.makedirs(txl_dir)
    
# Duyệt qua từng thư mục sản phẩm trong thư mục gốc
for product_dir in os.listdir(root_dir):
    product_path = os.path.join(root_dir, product_dir)

    # Kiểm tra xem đường dẫn có phải là thư mục hay không
    if os.path.isdir(product_path):
        # Đổi tên thư mục sản phẩm từ 'rawCMT2_' sang 'TXLCMT2_'
        new_product_dir = product_dir.replace('raw', 'TXL')
        new_product_path = os.path.join(txl_dir, new_product_dir)

        # Duyệt qua từng thư mục con (neutral, positive, negative) trong thư mục sản phẩm
        for sentiment_dir in os.listdir(product_path):
            sentiment_path = os.path.join(product_path, sentiment_dir)

            # Tạo một chuỗi rỗng để lưu trữ nội dung của tất cả các file
            all_files_content = ''

            # Duyệt qua từng file txt trong thư mục con
            for filename in os.listdir(sentiment_path):
                if filename.endswith('.txt'):
                    with open(os.path.join(sentiment_path, filename), 'r', encoding='utf-8') as file:
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
                        text_pre = re.sub(r"!@#$\[\']", "", text_pre) # Remove character: !@#$
                        text_pre= word_tokenize(text, format="text")
                        filename=os.path.join('E:\Code\KPW',"vietnamese-stopwords.txt")
                        with open(filename,'r',encoding='utf-8') as f:
                            List_StopWords=f.read().split("\n")
                        #remove stop words
                        text_pre=" ".join(text for text in text_pre.split() if text not in List_StopWords)
                        text_pre=text_pre.replace(",","").replace(".","").replace("  "," ").replace("!","").replace("...","")
                        
                        all_files_content += str(text_pre) + '\n'  # Thêm nội dung của file vào chuỗi

            output_filepath = os.path.join(new_product_path, sentiment_dir + '.txt')
            os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                output_file.write(all_files_content)  # Chuyển về chuỗi trước khi ghi

            print(f'Đã lưu: {output_filepath}')
