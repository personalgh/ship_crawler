from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import os

base_url="http://ship.cnss.com.cn/"
all_url=[]
html = urlopen("http://ship.cnss.com.cn/shippic_schlist.php?doaction=search&fk_catid=161&schMod=&schValue=&withSub=yes&currentPage=1&perPageSize=100&middleShowCount=5&rstOrderBy=&orderType=DESC").read().decode('utf-8')
soup = BeautifulSoup(html,features='lxml')
sub_urls=soup.find_all("img",
                        {
                            "src":re.compile("/uploads/ship_pic/*")})
for i in range(len(sub_urls)):
    su=re.sub('small','middle',sub_urls[i].get("src"))
    all_url.append(base_url+su)
# print("\n".join(all_url))
# print (os.getcwd())
for u in all_url:
    r = requests.get(u, stream=True)
    image_name = u.split('/')[-1]
    with open('./img/%s' % image_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)
    print('Saved %s' % image_name)