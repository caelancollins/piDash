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

Implemented Technologies: _TBD_  
* RaspianOS on a RaspberryPi 2 Model B  
* Python web scraper  
* (Proposed): In order to limit the actual workload on Raspberry Pi, perform all parsing on an Amazon EC2 instance, and have Raspberry Pi fetch fresh data in the form of simple boolean values, to be displayed on the dash.
