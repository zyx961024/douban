import requests
from bs4 import BeautifulSoup
import re
import os
import  pymysql
def insertMovie(name,Pic,Director,Star,Comment):
    db = pymysql.connect(host="localhost", user="root", password="admin", db="t_movie", port=3306)
    cur = db.cursor()
    # print(Director)
    sql="insert into movie (id,pic,name,director,star,comment) values(null,'%s','%s','%s','%s','%s')"%(name,Pic,Director,Star,Comment)
    # print(sql)
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
    finally:
        db.close()

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}


    def getImformation(url):
        r = requests.get(url, headers)
        soup = BeautifulSoup(r.text, 'lxml').find_all('div', class_='item')
        # print(soup)
        str1=""
        for i in range(len(soup)):
            name = re.findall(r'<span class="title">(.*?)</span>', str(soup[i]))[0]
            UnMovies=['三块广告牌','海蒂和爷爷','功夫','疯狂的麦克斯4：狂暴之路','奇迹男孩']
            if(name in UnMovies):
                Director =re.findall(r'导演:\s(.*?)\s', str(soup[i]))[0]
                Star =  re.findall(r'<span class="rating_num" property="v:average">(.*?)</span>', str(soup[i]))[0]
                Comment = '无'
                Pic = re.findall(r'img alt=".*?" class="" src="(.*?)" width=".*?"', str(soup[i]))[0]
                # str1=name+Director+Star+Comment
                insertMovie(name,Pic,Director,Star,Comment)

            else:
                Director = re.findall(r'导演:\s(.*?)\s', str(soup[i]))[0]
                Star = re.findall(r'<span class="rating_num" property="v:average">(.*?)</span>', str(soup[i]))[0]
                Comment = re.findall(r'<span class="inq">(.*?)</span>', str(soup[i]))[0]
                Pic = re.findall(r'img alt=".*?" class="" src="(.*?)" width=".*?"', str(soup[i]))[0]

                # str1 = name + Director + Star + Comment
                insertMovie(name, Pic, Director, Star, Comment)
            # with open("E:\py1.txt",'a+',encoding='utf-8') as f:
            #    f.write(str1+'\n')
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=%s&filter='%(25*i)
        print(url)
        getImformation(url)

except Exception as err:
    print(err)

