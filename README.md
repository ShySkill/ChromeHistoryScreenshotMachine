# Chrome History Screenshot Machine <img src="chromelogo.png" alt="Chrome logo" width="50" height="50">

The Chrome History Screenshot Machine is a script that will open chrome from a users device, take as many screenshots as desired of the history page (chrome://history), and send to a discord webhook through a byte stream, aswell as send other diagnostic and statistical data about the machine. You can make an exe version with pyinstaller, but I would not recommend it as this is not intended for malicious purposes, and the exe will be too slow.

## How to use

To run, install the required packages, and follow the steps below.

### Installation
Firstly, make sure you have python installed.
To install this project, all you need to do is download the requirements.txt file with all of the required packages and imports.
WARNING: Make sure that you put a valid discord webhook URL when prompted, or the project will not function as intended.

#### Commands
To install, run this command in the terminal
```shell
pip install -r requirements.txt
```
Then, you can run the file with
```shell
python main.py
```

Dm shyskill on discord for specifications
