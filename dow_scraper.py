from lxml import html
import requests
import socket

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


    page = requests.get('http://www.marketwatch.com/investing/index/djia')
    result = html.fromstring(page.content)

    answer = result.xpath('//span[@class="change--point--q"]/text()')

    isUp = True
    if answer[0][0] == '-':
        isUp = False


    #for finding relevant tags
    print("\n\n\n\n\n")
    print(isUp)




    #Now write UDP Packet sending code

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "Sending message:", weather_description

    #s.sendto(raining, (UDP_IP, UDP_PORT))
    s.sendto(isUp, (UDP_IP, UDP_PORT))
