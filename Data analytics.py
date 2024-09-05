import lxml.html,requests,re
from bs4 import BeautifulSoup,Comment
"""
url="https://www.python.org/dev/peps/pep-0020/"
xpath='//*[@id="the-zen-of-python"]/pre/text()'
res=requests.get(url)
ht=lxml.html.fromstring(res.text)
print(ht)
text=ht.xpath(xpath)
print(text)
print("Hello,\n"+"".join(text))
"""

"""
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"
}
for start_num in range(0,250,25):
    response=requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=headers)
    html=response.text
    soup=BeautifulSoup(html,"lxml")
    all_titles=soup.findAll("span",attrs={"class":"title"})
    for title in all_titles:
        title_string=title.string
        if "/" not in title_string:
            print(title_string)
    print(response)
    soup.find
"""

"""
获取在贴吧搜索钱学森后的页面："""
def getHTMLText(url, kv, headers):
    try:
        r = requests.get(url, params = kv, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}
url = "https://tieba.baidu.com/f"
kv = {'fr':'search', 'kw':'钱学森'}
soup = BeautifulSoup(getHTMLText(url, kv, headers), "html.parser")

comments_with_tags = soup.find_all(string=lambda string: isinstance(string, Comment) and '<' in string)
for comment in comments_with_tags:
    post_content = comment.extract()
    print(post_content)



"""
comments = soup.find_all(text=lambda text: isinstance(text, Comment))
for comment in comments:
    print(comment)
"""




"""
从中国科学院下载钱学森照片：
def getHTMLText(url, headers):
    try:
        r = requests.get(url, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except:
        return "产生异常"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}
url = "https://www.cas.cn/images/qxs1y_topimg.jpg"
path = "学习/钱学森.jpg"
with open(path, "wb") as f:
    f.write(getHTMLText(url, headers))
"""


"""
测试直接传递文件给BeautifulSoup：
newsoup=BeautifulSoup(open("C://Users/chenjun/Desktop/demo.txt",encoding='utf-8'),"lxml")

for child in newsoup.body:
    print(child)
print(newsoup.a.get("href"))
print(type(newsoup("a")[0]))
for link in newsoup.find_all("a"):
    print(link.get("href"))
"""




"""
def getHTMLText(url, kv, headers):
    try:
        r = requests.get(url, params = kv, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}
url = "https://tieba.baidu.com/f"
kv = {'fr':'search', 'kw':'湖北工业大学'}
soup = BeautifulSoup(getHTMLText(url, kv, headers), "html.parser")
bs64_str = re.findall('<code class="pagelet_html" id="pagelet_html_frs-list/pagelet/thread_list" style="display:none;">[.\n\S\s]*?</code>', getHTMLText(url, kv, headers))
bs64_str = ''.join(bs64_str).replace('<code class="pagelet_html" id="pagelet_html_frs-list/pagelet/thread_list" style="display:none;"><!--','')
bs64_str = bs64_str.replace('--></code>','')
print(bs64_str)
"""