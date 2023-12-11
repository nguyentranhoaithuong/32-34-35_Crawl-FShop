import os
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

ThuMucTXL = 'D:\Khai_pha_web\BaoCao\B7_TXLCmt'
tfidf_folder = 'D:\Khai_pha_web\BaoCao\B10_TF-IDF'

if not os.path.exists(tfidf_folder):
    os.makedirs(tfidf_folder)

vectorizer = TfidfVectorizer()

for ThuMucBrand in os.listdir(ThuMucTXL):
    brand_tfidf_folder = os.path.join(tfidf_folder, ThuMucBrand)
    if not os.path.exists(brand_tfidf_folder):
        os.makedirs(brand_tfidf_folder)

    brand_path = os.path.join(ThuMucTXL, ThuMucBrand)
    for ThuMucSP in os.listdir(brand_path):  
        SP_path = os.path.join(brand_path, ThuMucSP)  
        if os.path.isdir(SP_path):
            cmt = []
            file_names = []
            for file_name in ['Negative.txt', 'Neutral.txt', 'Positive.txt']:
                file_path = os.path.join(SP_path, file_name)
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        text = file.read()
                        if text:
                            cmt.append(text)
                            file_names.append(file_name)
            if cmt:
                tf_idf_matrix = vectorizer.fit_transform(cmt)
                df = pd.DataFrame(tf_idf_matrix.toarray(), columns=vectorizer.get_feature_names_out(), index=file_names)
                print(f'{ThuMucSP}')
                name = ThuMucSP.replace('TXL', 'TF_IDF')
                df.to_csv(os.path.join(brand_tfidf_folder, f'{name}.csv'), index=True, encoding='utf-8-sig')

                