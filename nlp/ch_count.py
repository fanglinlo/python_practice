import jieba
import wget

txt_file_path = "../news_2.txt"

with open(txt_file_path, "r")as fn:
    lines = fn.readlines()
    lines = list(map(lambda x: x.strip(),lines)) # 移除斷行字元

jieba.load_userdict("dict.txt.big")
tokens_1 = list(map(lambda x: list(jieba.cut(str(x), HMM=False)), lines))

word_count={}

for list in tokens_1:
    for word in list:
        if word not in word_count.keys():
            word_count[word] = 0
        word_count[word] +=1
print(word_count)

word_count_5up={}

for key,value in word_count.items():
    if value >= 5:
        word_count_5up[key] = value
print(word_count_5up)

import wordcloud
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt

# 下載中文字型檔
url="https://github.com/odek53r/Data-Science-Camp/raw/main/SourceHanSerifK-Light.otf"
ssl._create_default_https_context = ssl._create_unverified_context
wget.download(url)


wordcloud = WordCloud(
        background_color = 'white',
        font_path = 'SourceHanSerifK-Light.otf', # 放入中文字型檔路徑
        colormap=matplotlib.cm.cubehelix,
        width = 1600,
        height = 800,
        margin = 2)

# wordcloud 套件 Input 需放入詞頻統計的 dict 型態變數
wordcloud = wordcloud.generate_from_frequencies(word_count_5up)
plt.figure(figsize=(20,10), facecolor='k')
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
