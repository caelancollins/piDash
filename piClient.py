from lxml import html
import requests
import socket
import RPi.GPIO as GPIO
import time


print("Testing LED")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print "LED on"
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)

page = requests.get('http://www.geoiptool.net')
result = html.fromstring(page.content)

answer = result.xpath('//td/text()')

PORT = 2000
ADDRESS = socket.gethostbyname("ec2-54-242-241-35.compute-1.amazonaws.com")

loc = []
longitude = ""
latitude = ""
for i in range(0,len(answer)):
	if answer[i] == "Latitude":
		latitude=answer[i+1]
	if answer[i] == "Longitude":
		longitude=answer[i+1]


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(latitude, (ADDRESS,PORT))
sock.sendto(longitude, (ADDRESS,PORT))


#while True:
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print "received weather message:", data



#for baseball game data
OTHER_PORT = 3000

sock.sendto("baseball", (ADDRESS, OTHER_PORT))

data, addr = sock.recvfrom(1024)
print "received score of last baseball game:", data

sock.sendto("stock", (ADDRESS, 4000))

received, addr = sock.recvfrom(1024)
print "Status of Dow:", received

if received == "Dow is down":
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18,GPIO.LOW)

formatted = data.split(': ')

if formatted[1][0] ==  'L':
    GPIO.setup(23,GPIO.OUT)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23, GPIO.LOW)
