import tkinter
import json
import classes
import requests
from bs4 import BeautifulSoup



def findLenOfPage(page):

    pageList = []
    url = str(page)
    response = requests.get(url,verify=False)
    html = response.content
    soup = BeautifulSoup(html,"html.parser")
    allThem = soup.find_all("div",{"class": "pageLinks" , "style":False})

    for pages in allThem:
        page = pages.find_all('a')

        for l in page:
            pageList.append(l.text)
        lenOfPage = pageList[-2]
        return lenOfPage


def getInfoFromPage(x,link):
    url = str(link)+"?page="+str(x)
    response = requests.get(url, verify=False)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi, "html.parser")
    allElements = soup.find_all("div", {"class": "companies-item col-md-3 col-xs-4", "style": False})

    for elements in allElements:

        element = elements.find_all('ul')

        for e in element:
            a = e.text.split("\n")
            liste.append(a[1:-1])
        print(liste[-1])


def print_answers():
    key = value_inside.get()
    value = data[key]
    print(key)
    print(value)
    for i in range(1, int(findLenOfPage(str(value))) + 1):
        getInfoFromPage(i,value)
    classes.excelStart()

    for i in range(0, len(liste)):
        objectList.append(classes.infoS(liste[i][0], liste[i][1], liste[i][2]))
        objectList[i].writeExcel(str(i + 2))
    print("{} kategorisinde {} sayfa içerisinde toplam firma sayısı: {}".format(key,findLenOfPage(str(value)),len(liste)))
    liste.clear()
    objectList.clear()
    classes.excelFinish(key)


liste = []
objectList = []

with open("links.json",encoding="utf-8") as f:
    data = json.load(f)
root = tkinter.Tk()
root.title("birmilyonnokta")
root.geometry('350x250')
value_inside = tkinter.StringVar(root)
value_inside.set("Kategori Seçin")
question_menu = tkinter.OptionMenu(root, value_inside, *data.keys())
question_menu.pack(pady=(50,0))
submit_button = tkinter.Button(root, text='Başlat', command=print_answers)
submit_button.pack(pady=(100,0))
root.mainloop()




