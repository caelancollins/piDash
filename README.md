# piDash
CS4283 Computer Networks Final Project   

Dates:

* March 28: Feasibility Study
* April 13: Work in Progress
* April 27: Final Code and Video Submission  

Feasibility Study:  
* After installing the RaspianOS on the Raspberry Pi, we have set up a very basic LED display using a breadboard.  

* As some sort of scraper will be key to representing current data on our dashboard, we have built a very simple scraper that returns a boolean.  

* If the scraper returns true, the light is turned on. Otherwise it is kept off. (We negated the result for testing).  


Final Desired Functionality: _TBD_  

Implemented Technologies: _As of April 13_ 
* RaspianOS on a RaspberryPi 2 Model B  
* Python web scraper  
* A python client-server UDP connection between the Pi and an Amazon EC2 Instance
  * The pi scrapes an IP locator website (https://www.iplocation.net) to send the current latitude and longitude via UDP packets to the Amazon EC2. The EC2 instance then receives the location and can return information based on it. Currently it is set to return weather information via UDP Packets. An RGB LED on the pi returns a different color based on the weather for the day.
  * The last score of the Vanderbilt Baseball team is also scraped and returned. An LED will be used to indicate a loss or a win. 
* Proposed Ideas:
  * The EC2 Instance will have added scraping capabilities to return additional information to the Pi. 
