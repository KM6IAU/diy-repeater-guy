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

### Information about [fetch_and_extract.py](https://github.com/KM6IAU/diy-repeater-guy/blob/main/fetch_and_extract.py)
fetch_and_extract.py will first get the binary source file at http://www.scomcontrollers.com/downloads/SpLibEng_1.3.bin.

Then it will create two folders:

- **`c`**: companded (compressed and expanded) audio, bytewise exactly as it is stored in the binary source file.   These will sound like they are clipping without de-emphasis applied.

- **`d`**: the aforementioned files, except that they have been de-companded using inverse function provided at https://en.wikipedia.org/wiki/%CE%9C-law_algorithm .  These are the ones that will sound "right", in most cases.

Use the companded or de-companded audio files depending on if your output is considered to be pre-emphasized or not.

If you're transmitting from your  personal radio,  you want the  de-companded audio.  Your radio will emphasize, the repeater will hear your pre-emphasized audio and re-transmit it  "as-is"  on a different freq.  The listener's radio will de-emphasize.

If you are the repeater,  remember that the listener will de-emphasize, so if you're playing a local file,  it needs to be emphasized.   Use the  companded audio for this.

## Usage example
Say "this is a test":  
`python3 say.py this is a test`  
