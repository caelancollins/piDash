#Baseball Game Scraper
#When queried, will return a string specifying status of last Vanderbilt baseball game

import datetime
from bs4 import BeautifulSoup
import socket
import requests

while True:
    
    UDP_IP = "0.0.0.0"
    UDP_PORT = 3000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind((UDP_IP, UDP_PORT))

    #wait for one packet
    data, addr = s.recvfrom(1024)
    print "received message:", data
    UDP_IP = addr[0]
    UDP_PORT = addr[1]

    pageName = "http://www.vucommodores.com/sports/m-basebl/sched/vand-m-basebl-sched.html"

    #now use beautiful soup and requests
    page = requests.get(pageName)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find(id="schedtable")
    all_dates = table.findAll(class_="sch-col-1")#.get_text()
    all_opponents = table.findAll(class_="sch-col-2")#.get_text()
    all_scores_or_times = table.findAll(class_="sch-col-4")#.get_text()


    #for testing
    #print(all_dates[0].prettify())



    #create all_games list
    all_games = []
    for i in xrange(0, len(all_dates)):
        date = all_dates[i].get_text()
        opponent = all_opponents[i].get_text()
        score_or_time = all_scores_or_times[i].get_text()
        game_data = (date, opponent, score_or_time)
        all_games.append(game_data)

    del all_games[0] #first entry is just a heading

    #get today's date
    today = datetime.date.today()

    toReturn = ""

    for game in reversed(all_games):
        my_date, opponent, score_or_time = game
        split_date = my_date.split("/")
        #print(split_date)
        #added to prevent error on game with non-existent date (wtf vandy)    
        if len(my_date) < 4:
            continue

        game_date = datetime.date(2000+int(split_date[2]), int(split_date[0]), int(split_date[1]))
       
        #for testing
        #print "today:", today
        #print "game_date:", game_date
 
        #check if game_date is past today
        if today < game_date:
            continue
        
        elif today == game_date:
            #check to see what value of score_or_time is
            if ':' in score_or_time:
                continue
            else:
                toReturn = score_or_time
                break
        
        else:
            toReturn = score_or_time
            break


    toReturn = "Score of last game: " + toReturn


    #Now write UDP Packet sending code

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "Sending message:", toReturn

    s.sendto(toReturn, (UDP_IP, UDP_PORT))
