import jieba
from gensim import corpora,models
import pyLDAvis.gensim_models


#将评论分词，并去除停用词，然后把列表转换成字符串存入文件。这只是把结果放到文件中看一下
def a():
    with open("(新)湖工大评论.txt","r",encoding="utf-8") as f:
        stopwords = [line.strip() for line in open('哈工大停用词表.txt', "r", encoding='utf-8').readlines()]
        jieba.load_userdict("保留词.txt")
        with open("分词结果.txt","w",encoding="utf-8") as file:
            for i,temp in enumerate(f.readlines(),start=1):
                words = jieba.cut(temp)
                words = [word for word in words if word not in stopwords and word!=" "]
                if words!=['\n']:
                    file.write(" ".join(words))
            file.close()
        f.close()

#分词（包括去除停用词），构建词袋模型，运行LDA模型
def b():
    pass


# 定义停用词和加载保留词
stopwords = [line.strip() for line in open('哈工大停用词表.txt', "r", encoding='utf-8').readlines()]
jieba.load_userdict("保留词.txt")
# 对新闻文本进行分词、去停用词、去数字和标点符号
news_words = []

with open("(新)湖工大评论.txt","r",encoding="utf-8") as f:
    for i,temp in enumerate(f.readlines(),start=1):
        words = jieba.cut(temp)
        words = [word for word in words if word not in stopwords and word!=" " and word!="\n"]
        news_words.append(words)
    f.close()
#print(news_words)

# 构建词袋模型
dictionary = corpora.Dictionary(news_words)
corpus = [dictionary.doc2bow(words) for words in news_words]

# 运行LDA模型
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=15)

# 输出每个主题的前10个关键词
for topic in lda.print_topics(num_topics=5, num_words=10):
    print(topic)

# pyLDAvis.show(lda)

# # 对每篇新闻文本进行主题推断
# for i, doc in enumerate(corpus):
#     topic = sorted(lda[doc], key=lambda x: x[1], reverse=True)[0][0]
#     print('文本编号：{}，主题编号：{}'.format(i, topic))

#可视化，结果保存为html文件
d = pyLDAvis.gensim_models.prepare(lda, corpus, dictionary, mds = 'pcoa', sort_topics = True)
pyLDAvis.save_html(d, 'lda_show.html') # 将结果保存为html文件











# stopwords = [line.strip() for line in open('哈工大停用词表.txt', "r", encoding='utf-8').readlines()]
# s = "我？\n1"
# words = jieba.cut(s)
# aaa = " ".join(words)
# print(aaa)
# words = [word for word in words if word not in stopwords]
# if words!=[]:
#     print(words)
# print(type(words))