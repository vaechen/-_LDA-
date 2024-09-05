import lxml.html,requests
import time
from bs4 import BeautifulSoup,Comment

def get_HTMLText(url):      #去掉注释符号，抓取HTML代码。
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}
    try:
        r = requests.get(url,headers=headers)
        # r = requests.get(url, params = kv, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        html = html.replace(r'<!--', '"').replace(r'-->', '"')
        return html
    except:
        return "产生异常"

def get_Info(html):     #处理HTML代码，将对应的一个帖子转换成一个字典。并把所有的字典放在一个列表中返回。
    informations = []  # 存放所有信息的列表
    #html.parser
    soup = BeautifulSoup(html, 'lxml')
    li_tags = soup.find_all('li', class_="j_thread_list clearfix thread_item_box")          #注意，一定要删掉最后一个空格！！！
    # 遍历找到的li标签,一个li标签代表一个帖
    for li in li_tags:
        # 用字典存储获取的信息  
        info = {}  
        try:
            info['title'] = li.find(
                'a', class_="j_th_tit"
                ).text.strip()

            info['link'] = "https://tieba.baidu.com" + \
                           li.find('a', class_='j_th_tit')['href']

            info['author'] = li.find('span', class_='tb_icon_author')['title']

            info['time'] = li.find(
                'span', class_='pull-right is_show_create_time'
                ).text.strip()

            info['replyNum'] = li.find(
                'span', class_='threadlist_rep_num center_text'
                ).text.strip()

            informations.append(info)
        except:
            print("从标签中取信息出了问题！")
    #print(informations)  # 打印测试
    return informations
    
def write_Info_link(infoList):       #将列表中帖子的信息写入文件（主要是链接），encoding=utf-8
    #i=0  # 计页数
    # 以追加方式打开txt文件
    with open('湖北工业大学吧帖子爬取.txt', 'a', encoding='utf-8') as f:
        for info in infoList:  # 遍历列表中的每一个字典
            f.write(
                "标题:{}\t链接:{}\t帖子作者:{}\t发帖时间:{}\t回帖数量:{}\n".format(
                    info['title'], info['link'], info['author'], info['time'], info['replyNum']
                    )
                )
        f.close()


def all_one():
    start_url = "https://tieba.baidu.com/f?kw=湖北工业大学&pn="
    # kv = {'fr':'search', 'kw':'湖北工业大学'}
    for i in range(0,1050,50):
        url = start_url + str(i)
        informations = get_Info(get_HTMLText(url))
        write_Info_link(informations)
        print("第"+str(i)+"页打印完成!")
        time.sleep(1)

all_one()

"""
comments = soup.find_all(text=lambda text: isinstance(text, Comment))
for comment in comments:
    print(comment)
"""