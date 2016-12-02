from socket import *
import paho.mqtt.client as mqtt
import syslog

#MQTT Parameters
mqtt_server = "<<INSERT YOUR MQTT Server HERE>>"
mqtt_port = <<INSERT YOUR MQTT PORT HERE>>
mqtt_client_id = "<<INSERT YOUR CLIENT_ID  HERE>>"
mqtt_username = "<<INSERT YOUR USERNAME  HERE>>"
mqtt_password = "<<INSERT YOUR PASSWORD  HERE>>"
mqtt_topic = "<<INSERT YOUR TOPIC  HERE>>"

#Syslog Parameters
#Insert IP of server listener. 0.0.0.0 for any
server = "0.0.0.0"
#syslog port
port = 514
buf = 8192*4
addr = (server,port)

#Open Syslog Socket
syslog.syslog('Opening syslog socket: %s/%s' % (server,port))
TCPSock = socket(AF_INET,SOCK_DGRAM)
TCPSock.bind(addr)
if TCPSock.bind:
    syslog.syslog('Opened syslog socket: %s/%s' % (server,port))

#MQTT client
syslog.syslog('Opening MQTT socket: %s/%s' % (mqtt_server,mqtt_port))
mqttclient = mqtt.Client(client_id=mqtt_client_id, clean_session=True,protocol="MQTTv311")
mqttclient.username_pw_set(mqtt_username,mqtt_password)
mqttclient.connect(mqtt_server,mqtt_port,keepalive=60)
if mqttclient:
    syslog.syslog('Opened MQTT socket: %s/%s' % (mqtt_server,mqtt_port))

#enable if you want local logging.
#db=open("receive.log", "w")

while 1:
    data,addr = TCPSock.recvfrom(buf)
    if not data:
        print ("No response from systems!")
        break
    else:
        mqttclient.publish(mqtt_topic,payload=data,qos=0,retain=True)
        syslog.syslog('New Syslog -> sent to mqtt server: %s' % (data))
		#print ("Message: ", data, file=db, flush=True)

TCPSock.close()
