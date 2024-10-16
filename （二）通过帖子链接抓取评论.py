import lxml.html,requests
import time,random
from bs4 import BeautifulSoup,Comment

def get_comment_link():                     #对'湖北工业大学吧帖子爬取.txt'进行清洗，摘取所有的链接，encoding=utf-8
    # 以只读方式打开txt文件
    with open('湖北工业大学吧帖子爬取.txt', 'r', encoding='utf-8') as f:
        comment_list = []               #用来存储帖子链接的列表
        temp_list = f.readlines()
        for temp in temp_list:
            comment_list.append(temp.split("\t")[1][3:])
    return comment_list

def write_Info_comment(comment):       #评论写入文件，encoding=utf-8
     # 以写方式打开txt文件
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
        "Cookie":'__bid_n=18971f5e4808432730d0be; BAIDU_WISE_UID=wapp_1690275616093_738; BDUSS=FJNOWUxc09GQ3ZOZGI0N1BwVn5kdVhUYW9KeVc0ZkU4MWo5SXdtZXJTZExIT2RrSVFBQUFBJCQAAAAAAAAAAAEAAABkyMzoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEuPv2RLj79kS; BDUSS_BFESS=FJNOWUxc09GQ3ZOZGI0N1BwVn5kdVhUYW9KeVc0ZkU4MWo5SXdtZXJTZExIT2RrSVFBQUFBJCQAAAAAAAAAAAEAAABkyMzoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEuPv2RLj79kS; STOKEN=0d9aca0ee08b8d060e0cc0d62721ee3a66885326dc14f89e17917bfe67935b56; NO_UNAME=1; ZFY=7F5Iorl6YKbcsnEsKX:B:AQ4:B8kG1DXzGkqZ1MF8TRASw:C; BAIDUID=E8E14CE7F58E3CFE46F73E5BD4C47CE9:FG=1; BAIDUID_BFESS=E8E14CE7F58E3CFE46F73E5BD4C47CE9:FG=1; USER_JUMP=-1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1690275616,1690276395,1690994089,1692350652; st_key_id=17; arialoadData=false; XFI=0179a220-3da9-11ee-b2af-757212cfa95b; rpln_guide=1; XFCS=40E0E99955846B326A5890B23987FE4060B2F2E6A98D1A425B3650D19F13B83D; XFT=KpVU+exqfkxyNs2TPu23JiJhKhhm/VQ3plhcVHA1kqI=; wise_device=0; BA_HECTOR=25a024a0alah808h00al2g2t1idue6c1o; ab_sr=1.0.1_YWNhY2Q1OGU2MTAxMDgwOWM1MDk1MzlmM2ZiZGM0NmY4YWVhOGIyOThjNWQ2ODcxM2MwY2M2MTkzMzZjMGY2ODgyMTk4NDZmYjVhMDI3OGYzNzVjMjYxOTlhZmQxNGJlZDA5ODE0NmYwNDQ2MTdmYmM4ZWFjODIxZDc4NjRlNTk5NDk1M2RkMGMwMDE0YzQwMWRkZWI3OTJiNzlkYzMwMDVkZWViM2IwNDM0MGY5MmM5YjY4ODBlNTZiMDk3ZjU0; st_data=4432bd72d91dd22c557a5f7fa405dca8ba04020cce018dde51a1927ca4fbb78264f06d0d7c78b282278c35fd926cc829a74e76b9f16de34268d58ffb41d507d70c7e646d5ac1d40be8a4752504a9f7ac324ededa33bb3928bdecf9f6fbf33bb29118709c93a26f37898ab2755f3cd2f0f3c2aaba6210f1a6cbbe12f242b26107aeec42390d73f1436b39821dd5506ab5; st_sign=94aae3e0; tb_as_data=52fc2efb0f84a6eed5d410d281054e045397c1ddb469e3411e177782cf84296417d134078b103f7c93eebb165bfb213874e20cb5e60218ac4da5b02b01bd1e63b92b4b24a51bc9736ad9766481c333b5a80065b3b22cea7cdad3912b8954ca591a057079dd2c964f2d089d007d4a97e9; RT="z=1&dm=baidu.com&si=d4433ae4-d199-49e3-9f40-8bbc9e4d7916&ss=llgdvr3c&sl=8&tt=atq&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=q35&ul=1hkj&hd=1i7z"; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1692350721',
        "Accept":"application/json, text/javascript, */*; q=0.01",	
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
        }
    #headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}
    try:
        r = requests.get(comment, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
    except:
        return "产生异常"
    
    soup = BeautifulSoup(html, 'lxml')
    div_tags = soup.find_all('div', class_="d_post_content j_d_post_content")
    # 用列表存储评论
    comments = []
    for div in div_tags: 
        try:
            comments.append(div.text.strip())
        except:
            print("从div标签中取信息出了问题！")
    print(comments)
    #以追加方式打开txt文件
    with open('测试.txt', 'a', encoding='utf-8') as f:
        for comment in comments:
                f.write("{}\n".format(comment))

def all_two(comment_list):
    for i,comment in enumerate(comment_list,start=1):
        write_Info_comment(comment)
        print("第"+str(i)+"个帖子打印完成")
        time.sleep(1 + random.random())


# with open("湖工大吧评论.txt","r",encoding="utf-8") as f:
#     a = f.readlines()
#     print(type(a[1]))
#     print(list(a[1]))
#     f.close()

