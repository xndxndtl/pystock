import requests
from bs4 import BeautifulSoup
r=requests.get("http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100")
c=r.content
soup=BeautifulSoup(c,"html.parser")
all=soup.find("ul",{"class":"type06_headline"})

all2=all.find_all("li")

Result_save=open('news_result.txt','w',encoding='utf-8')

for item in all2:

    ## 기사 제목(타이틀) 가져오기
    title=item.find("dt",{"class":""}).text.replace("\t","").replace("\m","")
    modifyTitle=title[2:len(title)+1]
    print(modifyTitle)
    Result_save.write(modifyTitle)

    ## 그림 가져오기
    try:
        img=item.find("dt",{"class":"photo"})
        img2=img.find("img")["src"]
        print(img2)
        Result_save.write(img2)
    except:
        print("No Image")










