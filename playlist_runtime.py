import requests
import bs4
import datetime
print("Enter youtube playlist URL to calculate total runtime")
print("URL format: https://www.youtube.com/playlist?list=<someid>")
while(1):
        try:
            res = str(input("Enter url or 0 to exit\n")) #get the url
            if(res == "0"): #check exit condition
                break
            res = requests.get(res) #make http request to the url
            #print(res.text)
            pret = bs4.BeautifulSoup(res.text,'html.parser') #parse the response to allow traversal
            x = [] #stores the elements containing the time data
            secondArray = [] #variables for storing the values upon parsing
            minutesArray = []
            hoursArray = []
            allSpan = pret.find_all('span') # time data in present in <span aria-label>time data </span>
                                            # therefore first get all span
            for i in allSpan:
                temp = i.get("aria-label") #get all span with aria-label attribute
                if(type(" ") == type(temp)): # check if the result in not None type which causes error
                    x.append(i) #add the data to i
            
            for i in range(4): # The first 4 entries are (subscribe,subscribed,unsubscribe,subscribe number)
                x.pop(0)       # Therefore pop the first four entries from the list
            for i in x:
                try:
                    y = i.text.split(":") # Time data in hour:min:sec format therefore split the data
                    if(len(y) == 3):      # Append the data to the corresponding array
                        hoursArray.append(int(y[0])*60*60)  #Convert minutes and hours to seconds for easy calculation
                        minutesArray.append(int(y[1])*60)
                        secondArray.append(int(y[2]))
                    elif(len(y) == 2):
                        minutesArray.append(int(y[0])*60)
                        secondArray.append(int(y[1]))
                    elif(len(y) == 1):
                        secondArray.append(int(y[0]))

                    sum = 0 #Stores the sum of hours , minutes and seconds
                    for i in hoursArray:
                        sum+=i
                    for i in minutesArray:
                        sum+=i
                    for i in secondArray:
                        sum+=i
                except:
                    print("Error occured please report")
            print("Output format: x days HH:MM:SS")
            print(str(datetime.timedelta(seconds=sum))) # print the converted output 
        except:
            print("Error ocurred check URL or report")
    
