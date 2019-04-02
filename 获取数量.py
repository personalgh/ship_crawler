from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import numpy as np
NUM_I_WANT=1

base_url="http://www.shipspotting.com/"
##从分类页面上获取所有种类的连接
cate_url=[]
html=urlopen("http://www.shipspotting.com/gallery/categories.php").read().decode('utf-8')
soup = BeautifulSoup(html,features='lxml')
sub_urls=soup.find_all("a",
                        {
                            "href":re.compile("/gallery/search.php\?search_category_1=*")})
title=[]
# print(sub_urls)
##title:name for each catagories
for i in range(len(sub_urls)):
    title.append(sub_urls[i].find("img").get("title"))
# print("\n".join(title))
##cate_url:the url for each categroies
for i in range(len(sub_urls)):
    su=sub_urls[i].get("href")
    cate_url.append(base_url+su)
print("\n".join(cate_url))


##获取每种页面中总的图片数量
# num_part54 = [813,2267,2419,17914,755,7152,287,177,439,2301,14996,31744,39574,82705,54097,99,916,2763,5574,6056,6283,262098,12033,2972,2013,32,2358,6748,16846,72935,173094,36429,784,3321,965,38,45876,1567,4111,7434,8302,15287,28992,34478,8534,3126,1846,7580,20939,1148,1902,11,1553,88864,1372,2072]
# print(sub_urls[0])
##num_of_pic:the num of pics in each catagroies;
##读取奇慢，将改成爬取时再读取
num_of_pic=[]
for i in cate_url:
    sub_html=urlopen(i).read()
    sub_soup = BeautifulSoup(sub_html,features='lxml')
    # print(sub_soup.find("b").get_text())
    picnum=sub_soup.find("b").get_text()
    num_of_pic+=re.findall(r"\d+\.?\d*",picnum)
    print(num_of_pic[-1])
np.savetxt("picnum.txt",print)
print("numbers saved successfully")
