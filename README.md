# DIY Repeater Guy
This project, while perhaps not so aptly named, attempts to establish a framework and toolkit to construct phrases based on the voice used on the [S-COM 7330 repeater controller](http://www.scomcontrollers.com/7330) (and perhaps other S-COM repeater controllers).  The voice is that of professional voiceover talent, [Sean Caldwell](https://www.seancaldwell.com/).

## Disclaimer
This project is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.  
  
This project is provided for educational purposes.  S-COM has generously publicly provided the resources upon which the project draws.  The project maintainer's goal is to respectfully contribute to the amateur radio hobby without harm to any party.

## Observations and Notes
[vocabulary.json](https://github.com/KM6IAU/diy-repeater-guy/blob/main/vocabulary.json) is a JSON dict based on the
vocabulary tables beginning on page 471 of the [S-COM 7330 User Manual](http://www.scomcontrollers.com/downloads/7330_UserMan_V1.8.pdf).

See additional notes in [NOTE.md](https://github.com/KM6IAU/diy-repeater-guy/blob/main/NOTE.md).  

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
