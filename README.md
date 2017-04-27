# piDash
CS4283 Computer Networks Final Project     

Final Functionality:  
* A LED Dashboard connected to a RaspberryPi with the following LED notifications: 
  * A RGB LED representing the current weather that turns blue when rain is in the forecast, green for sunny days, and red for other. 
  * A Yellow LED that lights up if Vanderbilt Baseball won their last game. 
  * A Green LED that is lit if the Dow Jones Industrial Average is up on the day. 

Implemented Technologies: 
* RaspianOS on a RaspberryPi 2 Model B  
* 4 Python web scrapers  
* A python client-server UDP connection between the Pi and an Amazon EC2 Instance
  * The pi scrapes an IP locator website ~~(https://www.iplocation.net)~~ (https://www.geoiptool.net -- the old website lost its certificate) to send the current latitude and longitude via UDP packets to the Amazon EC2 Instance. 
  * The EC2 instance receives the location and returns the weather information via UDP Packets. 
  * The last score of the Vanderbilt Baseball team is scraped and returned.
  * The current status of the Dow Jones industrial average is scraped and returned. 
  * The EC2 Instance will have added scraping capabilities to return additional information to the Pi. 

Feasibility Study:  
* After installing the RaspianOS on the Raspberry Pi, we have set up a very basic LED display using a breadboard.  

* As some sort of scraper will be key to representing current data on our dashboard, we have built a very simple scraper that returns a boolean.  

* If the scraper returns true, the light is turned on. Otherwise it is kept off. (We negated the result for testing).  

Dates:  

* March 28: Feasibility Study
* April 13: Work in Progress
* April 27: Final Code and Video Submission
