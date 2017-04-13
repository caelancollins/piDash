#this is a sample file

from bs4 import BeautifulSoup
import socket
import requests


while True:
    received_packets = []

    #TODO: Add UDP Packet receive implementation
    UDP_IP = "0.0.0.0" #raspberry pi IP Address currently unknown
    UDP_PORT = 2000

    s = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    s.bind((UDP_IP, UDP_PORT))

    while len(received_packets) < 2:
        data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
        print "received message:", data
        received_packets.append(data)
        UDP_IP = addr[0]
        UDP_PORT = addr[1]


    #temporary (manual) latitude and longitude values
    latitude = 36.165888518000486
    longitude = -86.78443999499967


    #modifying lat and long appropriately
    latitude = received_packets[0]
    longitude = received_packets[1]


    #Creates URL based on latitude and longitude variabels
    pageName = "http://forecast.weather.gov/MapClick.php?lat=" + str(latitude) + "&lon=" + str(longitude)


    #Scanning through page for relevant data
    page = requests.get(pageName)
    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(id="seven-day-forecast-list")
    most_recent_time = seven_day.find(class_="tombstone-container") #add underscore since class is reserved in python

    #Now, to split the most_Recent_time object into relevant data.
    time_of_day = most_recent_time.find(class_="period-name").get_text()
    weather_description = most_recent_time.find(class_="short-desc").get_text()


    #valid weather descriptions include:
    ''' Sunny
        Mostly Clear
        Mostly Cloudy
        T-storms
        Partly Cloudy
        Partly Sunny
        Showers
        Mostly Sunny
        Breezy
        Mostly Clear
    '''


    #for finding relevant tags
    #print(most_recent_time.prettify())
    print("\n\n\n\n\n")
    print(time_of_day)
    print(weather_description)


    '''
    raining = ""

    if weather_description is "T-Storms" or weather_description is "Showers":
        raining = "raining";
    else:
        raining  = "not raining";
    '''


    #Now write UDP Packet sending code

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "Sending message:", weather_description 

    #s.sendto(raining, (UDP_IP, UDP_PORT))
    s.sendto(weather_description, (UDP_IP, UDP_PORT))



