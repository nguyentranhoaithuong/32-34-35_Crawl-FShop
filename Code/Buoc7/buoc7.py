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
        print(f"Xử lý thư mục: {thumuccon}")
        for file in os.listdir(thumuccon):
            file_path = os.path.join(thumuccon, file)
            if file.endswith('.txt'):
                if file=='Pos.txt':
                    print("BÌNH LUẬN TÍCH CỰC CỦA ",f" {thumuccon}")
                elif file=='Nes.txt':
                    print("BÌNH LUẬN TIÊU CỰC CỦA ",f" {thumuccon}")
                if file=='neutral.txt':
                    print("BÌNH LUẬN TRUNG LẬP CỦA ",f" {thumuccon}")
                TachTu=[]
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.read()

                        # Tách từ
                    TachTu+=lines.split()
                    
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
