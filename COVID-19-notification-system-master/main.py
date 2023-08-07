from plyer import notification  #for getting notification
import requests                 #for getting req url sites
from bs4 import BeautifulSoup   #for proper formatting of html code
import time                     #for time value

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:/Users/Siyona/Downloads/COVID-19-notification-system-master/COVID-19-notification-system-master/icon.ico.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text


# if __name__ == "__main__":
#     while True:

#     #notifyMe("siyona says","GO CORONA") basic demo
#         myHtmlData = getData("https://www.mohfw.gov.in/")   #website from we collect data

#         soup = BeautifulSoup(myHtmlData, "html.parser")     #for
#         #print(soup.prettify()) this is for showing only table
#         myDataStr = ""
#         for tr in soup.find_all('tbody')[0].find_all('tr'):   #for showing data from all table
#             myDataStr += tr.get_text() 
#         myDataStr = myDataStr[0:]
#         itemList = myDataStr.split("\n\n")

#         states = ["Maharashtra",'Delhi',"Goa"]   #dictionary
#         for item in itemList[0:33]:              # for all states from site containing all rows
#              dataList = item.split('\n')
#              if dataList[1] in states:
#                  nTitle = "Cases of COVID-19"
#                  nText = f"STATE {dataList[1]}\n INDIAN & Foreign : {dataList[2]}\n Cured :{dataList[3]}\n Deaths :{dataList[4]}"
#                  notifyMe(nTitle,nText)
#                  time.sleep(3)
#     time.sleep(3600)

states = ["Maharashtra",'Delhi',"Goa"]
    
if __name__ == "__main__":
    while True:
        myHtmlData = getData("https://www.mohfw.gov.in/")

        soup = BeautifulSoup(myHtmlData, "html.parser")
        
        try:
            tbody = soup.find('tbody')
            if tbody:
                rows = tbody.find_all('tr')
                for tr in rows:
                    columns = tr.find_all('td')
                    if len(columns) >= 5:
                        state = columns[1].get_text().strip()
                        if state in states:
                            nTitle = "Cases of COVID-19"
                            nText = f"STATE {state}\n INDIAN & Foreign : {columns[2].get_text()}\n Cured :{columns[3].get_text()}\n Deaths :{columns[4].get_text()}"
                            notifyMe(nTitle, nText)
                            time.sleep(3)
        except Exception as e:
            print("An error occurred:", e)
        
        time.sleep(3600)

