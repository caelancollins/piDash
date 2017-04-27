from lxml import html
import requests
import socket
import RPi.GPIO as GPIO
import time


#create booleans for data representation
dow_up = False
raining = False
sunny = False
other = False
baseball_win = False



page = requests.get('http://www.geoiptool.net')
result = html.fromstring(page.content)

answer = result.xpath('//td/text()')

#getting longitude and latitude from parsed data
longitude = ""
latitude = ""
for i in range(0,len(answer)):
	if answer[i] == "Latitude":
		latitude=answer[i+1]
	if answer[i] == "Longitude":
		longitude=answer[i+1]



#weather
WEATHER_PORT = 2000
ADDRESS = socket.gethostbyname("ec2-54-242-241-35.compute-1.amazonaws.com")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(latitude, (ADDRESS,WEATHER_PORT))
sock.sendto(longitude, (ADDRESS,WEATHER_PORT))


#while True:
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
print "received weather message:", data


if "Rain" in data or "Showers" in data or "T-storms" in data:
	raining = True
	sunny = False
	other = False
#"Clouds" only occurs in the description of "A Few Clouds" i.e. sunny
if "Sun" in data or "Sunny" in data or "Fair" in data or "Clouds" in data:
	sunny = True
	raining = False
	other = False
else: 
	other = True 


#for baseball game data
BASEBALL_PORT = 3000

sock.sendto("baseball", (ADDRESS, BASEBALL_PORT))

data, addr = sock.recvfrom(1024)
print data


formatted = data.split(': ')
if formatted[1][0] ==  'L':
	baseball_win = False



#for stock market data
DOW_PORT = 4000
sock.sendto("stock", (ADDRESS, DOW_PORT))

received, addr = sock.recvfrom(1024)
print "Status of Dow:", received

if received == "Dow is down":
	dow_up = False



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)






if not dow_up: #lights up if dow is down
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18,GPIO.LOW)


if not baseball_win: #lights up if vandy lost
    GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23, GPIO.LOW)

if sunny: 
	GPIO.output(16,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(16, GPIO.LOW)

if raining: 
	GPIO.output(12,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(12, GPIO.LOW)

if other:
	GPIO.output(25,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(25, GPIO.LOW)
