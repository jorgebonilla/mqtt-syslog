FROM python:3.5.2-alpine
MAINTAINER Jorge Bonilla <jorge.luis.bonilla@gmail.com>

RUN pip install paho-mqtt
COPY ./mqtt-syslog.py /root/mqtt-syslog.py
EXPOSE 514
CMD ["python","/root/mqtt-syslog.py"]
