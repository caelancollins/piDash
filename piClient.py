from lxml import html
import requests
import socket

page = requests.get('https://geoiptool.com')
result = html.fromstring(page.content)

answer = result.xpath('//span/text()')

PORT = 2000
ADDRESS = socket.gethostbyname("ec2-54-242-241-35.compute-1.amazonaws.com")

loc = []
longitude = ""
latitude = ""
for i in range(0,len(answer)):
	if answer[i] == "Latitude:":
		latitude=answer[i+1]
	if answer[i] == "Longitude:":
		longitude=answer[i+1]


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(latitude, (ADDRESS,PORT))
sock.sendto(longitude, (ADDRESS,PORT))


while True:
     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
     print "received message:", data

