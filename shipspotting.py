from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import numpy as np
import time
NUM_I_WANT=1

# base_url="http://www.shipspotting.com/"
# ##从分类页面上获取所有种类的连接
# cate_url=[]
# html=urlopen("http://www.shipspotting.com/gallery/categories.php").read().decode('utf-8')
# soup = BeautifulSoup(html,features='lxml')
# sub_urls=soup.find_all("a",
#                         {
#                             "href":re.compile("/gallery/search.php\?search_category_1=*")})
# title=[]
# # print(sub_urls)
# ##title:name for each catagories
# for i in range(len(sub_urls)):
#     title.append(sub_urls[i].find("img").get("title"))
# # print("\n".join(title))
# ##cate_url:the url for each categroies
# for i in range(len(sub_urls)):
#     su=sub_urls[i].get("href")
#     cate_url.append(base_url+su)
# # print("\n".join(cate_url))
# # print(cate_url)
##获取每种的title
title=['Accommodation Vessels & Barges', 'Aircraft Carriers', 'Ancient Motor Vessels', 'Auxiliaries', 'Barge Carriers', 'Barges', 'Battleships', 'Bulkers', 'Bulkers built 1950-1960', 'Bulkers built 1961-1970', 'Bulkers built 1971-1980', 'Bulkers built 1981-1990', 'Bulkers built 1991-2000', 'Bulkers built 2001-2010', 'Bulkers built 2011-2020', 'Bulkers built before 1950', 'Bulkers including more than one ship', 'Buoy/Lighthouse Maintenance Vessels & Lightships', 'Cable and Pipelayers', 'Casualties', 'Cement Carriers', 'Chemical and Product Tankers', 'Coast Guard', 'Combined Carriers (OBO, CABU etc.)', 'Construction Maintenance Vessels', 'Containerships', 'Containerships (only) More than one vessel', 'Containerships built 1971-1980', 'Containerships built 1981-1990', 'Containerships built 1991-2000', 'Containerships built 2001-2010', 'Containerships built 2011-2020', 'Containerships built before 1971', 'Corvettes', 'Crane Ships and Crane Platforms (Specialized)', 'Crane Ships and Floating Sheerlegs', 'Crude Oil Tankers', 'Cruise Ships and Liners', 'Cruise Ships and Liners built 1950-1960', 'Cruise Ships and Liners built 1961-1970', 'Cruise Ships and Liners built 1971-1980', 'Cruise Ships and Liners built 1981-1990', 'Cruise Ships and Liners built 1991-2000', 'Cruise Ships and Liners built 2001-2010', 'Cruise Ships and Liners built 2011-2020', 'Cruise Ships and Liners built before 1950', 'Cruisers', 'Destroyers', 'Dredgers', 'Drill Ships', 'Drilling Rigs/Parts of Drilling Rigs', 'Examples', 'Fast Attack Craft', 'Ferries', 'Fire Fighting Vessels', 'Fisheries research and support vessels', 'Fishing vessel loa 70ft/21m and over', 'Fishing Vessels', 'Fishing vessels loa less than 70ft/21m', 'Floating Production/Storage/Offloading Units', 'Floating Sheerlegs and Crane Barges/Crane Pontoons', 'Formation and group shots', 'Frigates', 'Fruit Juice Tankers', 'Gas Tankers built 1980 - 2020', 'Gas Tankers built before 1980', 'General cargo ship photos, more than one ship', 'General Cargo Ships', 'General cargo ships built 1940-1949 (Over 3000gt)', 'General cargo ships built 1940-1949 (Under 3000gt)', 'General cargo ships built 1950-1959 (Over 3000gt)', 'General cargo ships built 1950-1959 (Under 3000gt)', 'General cargo ships built 1960-1969 (Over 3000gt)', 'General cargo ships built 1960-1969 (Under 3000gt)', 'General cargo ships built 1970-1979 (Over 3000gt)', 'General cargo ships built 1970-1979 (Under 3000gt)', 'General cargo ships built 1980-1989 (Over 3000gt)', 'General cargo ships built 1980-1989 (Under 3000gt)', 'General cargo ships built 1990-1999 (Over 3000gt)', 'General cargo ships built 1990-1999 (Under 3000gt)', 'General cargo ships built 2000-2010 (Over 3000gt)', 'General cargo ships built 2000-2010 (Under 3000gt)', 'General cargo ships built 2011-2020 (Over 3000gt)', 'General cargo ships built 2011-2020 (Under 3000gt)', 'General cargo ships built before 1940 (Over 3000gt)', 'General cargo ships built before 1940 (Under 3000gt)', 'Great Lakes (Tugs & Barges)', 'Great Lakes (Workboats)', 'Great Lakes Bulkers', 'Great Lakes Bulkers (More than one ship )', 'Great Lakes Bulkers (Winter & Summer Lay Ups)', 'Guard Vessels/Safety/Rescue', 'Harbour & tour boats / restaurant vessels', 'Harbour Overview Images', 'Heavy Lift Vessels', 'High Speed Vessels', 'Historical / Unidentified Ship Funnel Marks', 'Hopper Barges', 'Icebreakers', 'Inland Dry Cargo Vessels', 'Inland Passenger Vessels/ Ferries', 'Inland Special Purpose Vessels', 'Inland Tankers', 'Inland Tugs', 'Inland Vessels', 'Landing Ships', 'Law Enforcement', 'Live fish carriers', 'Livestock Carriers', 'Mine Warfare Ships', "Modern rig sailing ships / sailing yachts over 65' (20m) LOA", 'Motor Yachts', 'Museum Ships', 'Mystery Ships', 'Near-shore fishing vessels', 'Offshore', 'Offshore (overview and group photos)', 'Offshore Crew Vessels', 'Ore Carriers', 'Overview - fishing fleets', 'Palletised Cargo Ships', 'Passenger Vessels', 'Patrol forces', 'Pilot Vessels', 'Platforms', 'Port Bunkering and Water Tankers', 'Reefers', 'Reefers (only) more than one vessel', 'Reefers built 1980 onwards', 'Reefers built before 1980', 'Reefers in support of fishing vessels at sea', 'Rescue Vessels', 'Research and Survey Vessels', 'RO/RO', 'Sailing Vessels', 'Salvage Vessels', 'Scrapyard Ships', "SD 14's", 'Service Craft', 'Ship Interior', "Ship's Deck", "Ship's engine rooms", 'Shipping Companies Funnel Marks / Superstructure Logo Boards', 'Ships to be reclassified/waiting identity details', 'Ships under Construction', 'Ships under Repair or Conversion', "Ships' Lifeboats and Tenders", 'Special Purpose Ships', 'Steam Ships (Operating and Preserved)', 'Storm Pictures', 'Submarines', 'Supply Ships/Tug Supplies/AHTS', 'Support Vessels', 'Tankers', 'Tankers built before 1970', "Traditional rig sailing ships from 120'(36.6m) LOA", "Traditional rig sailing ships under 120'(36.6m)LOA", 'Training Ships', 'Tugs', 'Tugs with Tow', 'Unidentified Far Eastern Shipping (Admin use only)', 'Vegetable/Edible Oil Tankers', 'Vehicle Carriers', 'Waste Disposal Vessels', 'Well Stimulation/Testing Vessels', 'Whalers and Sealers', 'Wheelhouse', 'Wine Tankers', 'Wood Chip Carriers', 'Work Boats', 'Wrecks & Relics', '_ Armaments', '_ For preservation', '_ Ships Crests', '_Flight Decks']

##获取每种页面中总的图片数量(54)
num_part54 = [813,2267,2419,17914,755,7152,287,177,439,2301,14996,31744,39574,82705,54097,99,916,2763,5574,6056,6283,262098,12033,2972,2013,32,2358,6748,16846,72935,173094,36429,784,3321,965,38,45876,1567,4111,7434,8302,15287,28992,34478,8534,3126,1846,7580,20939,1148,1902,11,1553,88864,1372,2072]
# print(sub_urls[0])
##num_of_pic:the num of pics in each catagroies;
##读取奇慢，将改成爬取时再读取
# num_of_pic=[]
# for i in cate_url:
#     sub_html=urlopen(i).read()
#     sub_soup = BeautifulSoup(sub_html,features='lxml')
#     # print(sub_soup.find("b").get_text())
#     picnum=sub_soup.find("b").get_text()
#     num_of_pic+=re.findall(r"\d+\.?\d*",picnum)
#     print(num_of_pic[-1])
# np.savetxt("picnum.txt",print)
# print("numbers saved successfully")


##获取category编号
cate_num=['276', '169', '37', '160', '65', '18', '168', '5', '137', '140', '141', '142', '143', '144', '257', '145', '182', '202', '38', '39', '55', '46', '25', '291', '277', '4', '205', '132', '133', '134', '129', '261', '131', '164', '147', '146', '155', '13', '193', '194', '195', '196', '197', '198', '262', '199', '167', '166', '30', '273', '94', '220', '284', '9', '217', '245', '238', '14', '239', '149', '41', '181', '165', '58', '265', '264', '171', '15', '102', '173', '103', '174', '104', '175', '105', '176', '106', '178', '127', '179', '128', '180', '259', '258', '101', '172', '263', '268', '148', '212', '218', '275', '53', '52', '51', '32', '249', '282', '31', '43', '184', '187', '185', '188', '189', '162', '42', '244', '78', '161', '191', '33', '69', '48', '80', '44', '204', '283', '76', '242', '57', '60', '163', '19', '274', '96', '20', '285', '224', '223', '243', '50', '17', '21', '190', '281', '70', '100', '159', '22', '83', '81', '71', '77', '95', '73', '97', '62', '92', '49', '170', '35', '278', '8', '156', '24', '45', '63', '10', '270', '221', '59', '12', '216', '280', '241', '82', '64', '211', '34', '61', '208', '219', '210', '209']
# cate_num=[]
# for i in range(len(cate_url)):
#     cate_num+=re.findall(r".+?category_1=(\d+)",cate_url[i])
# print (cate_num)


##修改URL中每页显示数量为总数量
for i in range(1):
    ##创建文件夹
    
    ##创建文件夹结束
    inner_url="http://www.shipspotting.com/gallery/search.php?limit=12&limitstart=0&search_title=&search_title_option=&search_imo=&search_pen_no=&search_mmsi=&search_eni=&search_callsign=&search_category_1=276&search_cat1childs=&search_uid=&search_country=&search_port=&search_subports=&search_flag=&search_homeport=&search_adminstatus=&search_classsociety=&search_builder=&search_buildyear1=&search_owner=&search_manager=&sortkey=p.lid&sortorder=desc&page_limit=12&viewtype=1"
    sub_part_cate="search_category_1="+cate_num[i]
    sub_part_pagenum="page_limit="+str(num_part54[i])
    inner_url=re.sub('search_category_1=276',sub_part_cate,inner_url)
    inner_url=re.sub('page_limit=12',sub_part_pagenum,inner_url)
    # print(inner_url)
    print("下面开始获取图片链接")
    ##获取图片连接
    pic_page_html=urlopen(inner_url).read()
    pic_page_soup = BeautifulSoup(pic_page_html,features='lxml')
    print("soup完成")
    img_find=pic_page_soup.find_all("img",
                            {
                                "src":re.compile("http://www.shipspotting.com/photos/small/*")})
    print("find_all完成")
    img_url=[]
    num_mark=0
    print("开始循环爬取")
    for i in range(len(img_find)):
        num_mark+=1
        if(num_mark<723):
            continue
        ##修改图片尺寸small->middle
        mg=re.sub('small','middle',img_find[i].get("src"))
        img_url.append(mg)
        print(mg)
    
        ##进行爬取
        r = requests.get(mg, stream=True)
        image_name = mg.split('/')[-1]
        with open('./img2/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        time_now=time.strftime('%H:%M:%S',time.localtime(time.time()))
        print('Saved %s, no.%d , %s' % (image_name, num_mark, time_now))















# all_url=[]
# html = urlopen("http://ship.cnss.com.cn/shippic_schlist.php?doaction=search&fk_catid=161&schMod=&schValue=&withSub=yes&currentPage=1&perPageSize=100&middleShowCount=5&rstOrderBy=&orderType=DESC").read().decode('utf-8')
# soup = BeautifulSoup(html,features='lxml')
# sub_urls=soup.find_all("img",
#                         {
#                             "src":re.compile("/uploads/ship_pic/*")})
# for i in range(len(sub_urls)):
#     su=re.sub('small','middle',sub_urls[i].get("src"))
#     all_url.append(base_url+su)
# # print("\n".join(all_url))
# # print (os.getcwd())
# for u in all_url:
#     r = requests.get(u, stream=True)
#     image_name = u.split('/')[-1]
#     with open('./img/%s' % image_name, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=128):
#             f.write(chunk)
#     print('Saved %s' % image_name)