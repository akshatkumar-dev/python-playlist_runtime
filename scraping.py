import requests
import bs4
import datetime
print("Enter youtube playlist URL to calculate total runtime")
print("URL format: https://www.youtube.com/playlist?list=<someid>")
while(1):
    res = str(input("Enter url or 0 to exit\n"))
    if(res == "0"):
        break
    res = requests.get(res)
    pret = bs4.BeautifulSoup(res.text,'html.parser')
    print(pret)