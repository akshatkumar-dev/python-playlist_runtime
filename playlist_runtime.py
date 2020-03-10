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
    x = []
    hours = 0
    minutes = 0
    seconds = 0
    secondArray = []
    minutesArray = []
    hoursArray = []
    allSpan = pret.find_all('span')
    for i in allSpan:
        temp = i.get("aria-label")
        if(type(" ") == type(temp)):
            x.append(i)
        
    for i in range(4):
        x.pop(0)

    for i in x:
        y = i.text.split(":")
        if(len(y) == 3):
            hoursArray.append(int(y[0])*60*60)
            minutesArray.append(int(y[1])*60)
            secondArray.append(int(y[2]))
        elif(len(y) == 2):
            minutesArray.append(int(y[0])*60)
            secondArray.append(int(y[1]))
        elif(len(y) == 1):
            secondArray.append(int(y[0]))

    sum = 0
    for i in hoursArray:
        sum+=i
    for i in minutesArray:
        sum+=i
    for i in secondArray:
        sum+=i
    print("Output format: x days HH:MM:SS")
    print(str(datetime.timedelta(seconds=sum)))
    
