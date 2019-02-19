import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/English-language_idioms"

res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
    data = items.find_all(['th','td'])
    try:
        idiom = data[0].text
        defin = data[2].text
    except IndexError:pass
    print("{}|{}".format(idiom,defin))

print(list[0][2].text)

'''
f = open("i.txt", "r")

l = []
i = 0
str = ""
for line in f:
    if i % 2 == 0:
        str = str + line.strip()
    else:
        str = str + "," + line.strip()
        print(str)
        str = ""
    i = i+1


f.close()

'''

'''
for d in defin:
    d = d.text.replace(":",",").replace("\n","")
    print( "\n")

for c in range(0, len(idioms)):
    i = idioms[c].text.replace(":","")
    d = defin[c].text
'''
