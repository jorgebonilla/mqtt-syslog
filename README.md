# mqtt-syslog
Receives syslog messages and publish it on mqtt

1. Point your Syslog enabled device to the server where you are going to run this script
2. Replace the mqtt variables with the information from your MQTT server in the script
3. execute: `sudo python mqtt-syslog.py`


### For docker-heads:
1. `git clone https://github.com/jorgebonilla/mqtt-syslog.git`
2. `cd mqtt-syslog`
3. `vim ./mqtt-syslog.py`
4. Replace all the mqtt parameter with your values
5. `docker build . -t mqtt-syslog`
6. `docker run -it -p 514:514 mqtt-syslog`
