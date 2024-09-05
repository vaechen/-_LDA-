import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords as nltk_stopwords
import jieba
from gensim import corpora, models

#from sklearn.datasets import make_blobs
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis

def test():
    with open("评论.txt","r",encoding="utf-8") as f:
        tokens = f.readline()
        test = jieba.cut(tokens)
        test = " ".join(test)
        print(test)
        f.close()

def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = [line.strip() for line in file]
    return set(stopwords)

def preprocess(text, stopwords):
    # 分词
    tokens = jieba.cut(text)
    # 去除停用词
    filtered_tokens = [token for token in tokens if token not in stopwords]
    return filtered_tokens

# # 停用词文件路径
# stopwords_file = '哈工大停用词表.txt'  # 根据你的保存路径进行修改

# # 加载停用词表
# stop_words = load_stopwords(stopwords_file)

# # 示例
# text = "这个产品真的很好用！"
# processed_text = preprocess(text, stop_words)
# print(processed_text)


# 可视化分析结果

# t = ("1")
# print(type(t))


#帖子标题补充到评论文件中
def d():
    with open("湖北工业大学吧帖子爬取.txt","r",encoding="utf-8") as f:
        comment_list = []               #用来存储帖子链接的列表
        temp_list = f.readlines()
        for temp in temp_list:
            comment_list.append(temp.split("\t")[0][3:])

        with open("(新)湖工大评论.txt","a",encoding="utf-8") as file:
            for temp in comment_list:
                file.write("{}\n".format(temp))
            file.close()
        f.close()

jieba.load_userdict("保留词.txt")
s = " "
stopwords = [line.strip() for line in open('哈工大停用词表.txt', "r", encoding='utf-8').readlines()]
w = "我想去湖工大上学！"
words = jieba.cut(w)
words = [word for word in words if word not in stopwords and word!=" "]
print(words)


