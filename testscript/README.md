Install python3
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
python3 -V

Install pip3
sudo apt-get install python-pip3

Install selenium
sudo pip3 install -U selenium==3.8.1

Install java Version 8
sudo add-apt-repository ppa:webupd8team/java
sudo apt update; sudo apt install oracle-java8-installer
javac -version

Check google chrome version (should be 64.xx)
google-chrome --version

Install ChromeDriver v2.35
Download ChromeDriver from below URL
https://chromedriver.storage.googleapis.com/index.html?pate=<version_number>/
eg: https://chromedriver.storage.googleapis.com/index.html?pate=2.34/
Check for the compatible ChromeDriver for your google-chrome version in notes.txt on above link & install & download this version.
./chromedriver --version

Chnage the driverpath in the script testGmailLogin.py to the path where you have installed the ChromeDriver

run script:
python3 testGmailLogin.py