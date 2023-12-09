import nltk
import re
import os
from underthesea import word_tokenize
import matplotlib.pyplot as plt
from wordcloud import WordCloud
nltk.download('stopwords')
nltk.download('punkt')

from nltk import FreqDist
from nltk.probability import FreqDist
from nltk.corpus import stopwords

thumucgoc = 'E:\Code\BTL_KPW\TXLCMT'

for folder in os.listdir(thumucgoc):
    thumuccon = os.path.join(thumucgoc, folder)
    if os.path.isdir(thumuccon):
        print("------------------------------------------------------------------------------------------------------------------")
        print(f"Xử lý dòng sản phẩm: {thumuccon}")
        for f in os.listdir(thumuccon):
            tmc=os.path.join(thumuccon,f)
            if os.path.isdir(tmc):
                print(f"Xử lý sản phẩm: {tmc}")
                for file in os.listdir(tmc):
                    file_path=os.path.join(tmc,file)
                    if file.endswith(".txt"):
                        if file=='Positive.txt':
                            print("----BÌNH LUẬN TÍCH CỰC CỦA ",f" {tmc}")
                        elif file=='Negative.txt':
                            print("----BÌNH LUẬN TIÊU CỰC CỦA ",f" {tmc}")
                        if file=='Neutral.txt':
                            print("----BÌNH LUẬN TRUNG LẬP CỦA ",f" {tmc}")
                        TachTu=[]
                        with open(file_path,"r",encoding="utf-8") as f:
                            lines = f.read()
                            TachTu+=lines.split()
                            # print(TachTu)
                            if TachTu!=[]:
                                print("Number of words: ", len(TachTu))
                                
                                frequency_dist = FreqDist(word.lower() for word in TachTu)

                                # In 50 từ xuất hiện nhiều nhất
                                print("Top 50 words:")
                                print(frequency_dist.most_common(50))

                                # Vẽ biểu đồ tần suất xuất hiện của 20 từ phổ biến nhất
                                plt.figure(figsize=(12, 6))
                                frequency_dist.plot(20, cumulative=False)
                                
                                # Tạo word cloud từ frequency distribution
                                wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(frequency_dist)

                                # Hiển thị word cloud
                                plt.figure(figsize=(10, 5))
                                plt.imshow(wordcloud, interpolation='bilinear')
                                plt.axis("off")
                                plt.title('Word Cloud')
                                plt.show()
                                print("\n ")
                            else:
                                print(f"File {file_path} trống. Bỏ qua...")
                                print("\n")

