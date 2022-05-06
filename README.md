# DIY Repeater Guy
This project, while perhaps not so aptly named, establishes a framework and
toolkit to construct phrases based on the voice used on the S-COM 7330 repeater
controller (and perhaps other S-COM repeater controllers).  The voice is that
of professional voiceover talent, [Sean Caldwell](https://www.seancaldwell.com/).

## Prerequisites
### debian-based linux
`sudo apt update`  
`sudo apt install git python3 wget sox`  

### windows-based windows
You'll figure it out.  

## Setup
`git clone https://github.com/KM6IAU/diy-repeater-guy.git`  
`cd diy-repeater-guy`  
`python3 fetch_and_extract.py`


## Usage example
Say "this is a test":  
`python3 say.py this is a test`  

## Notes
[vocabulary.json](https://github.com/KM6IAU/diy-repeater-guy/blob/main/vocabulary.json) is a JSON dict based on the
vocabulary tables beginning on page 471 of the [S-COM 7330 User Manual](http://www.scomcontrollers.com/downloads/7330_UserMan_V1.8.pdf).
