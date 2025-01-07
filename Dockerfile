# Dockerfile, Image, Container
FROM python:3.9.18-slim-bullseye

ADD forward.py .

# websocket-client is used for websocket communication with rec bms
# rel is used for automatic reconnection to websocket server
# paho-mqtt is used for sending results to mqtt server

RUN pip install websocket-client rel paho-mqtt

CMD ["python", "./forward.py"]

# build image with: docker build -t python-magichome .