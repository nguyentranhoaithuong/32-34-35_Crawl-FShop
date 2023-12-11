import nltk
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud
nltk.download('stopwords')
nltk.download('punkt')

from nltk import FreqDist
from nltk.probability import FreqDist

thumucgoc = 'D:\Khai_pha_web\BaoCao\B7_TXLCmt'

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
                            if TachTu!=[]:
                                print("Number of words: ", len(TachTu))
                                
                                frequency_dist = FreqDist(word.lower() for word in TachTu)

                                print("Top 50 words:")
                                print(frequency_dist.most_common(50))

                                plt.figure(figsize=(12, 6))
                                frequency_dist.plot(20, cumulative=False)
                                
                                wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(frequency_dist)

                                plt.figure(figsize=(10, 5))
                                plt.imshow(wordcloud, interpolation='bilinear')
                                plt.axis("off")
                                plt.title('Word Cloud')
                                plt.show()
                                print("\n ")
                            else:
                                print(f"File {file_path} trống. Bỏ qua...")
                                print("\n")
