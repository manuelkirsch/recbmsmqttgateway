import websocket
import _thread
import time
import rel
import random
import time
import json
import os

username = os.environ['MY_USER']
password = os.environ['MY_PASS']
broker = os.environ['MY_BROKER']
port = int(os.environ['MY_PORT'])

from paho.mqtt import client as mqtt_client

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
    
FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code: %s", rc)
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        print("Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            print("Reconnected successfully!")
            return
        except Exception as err:
            print("%s. Reconnect failed. Retrying...", err)

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
    print("Reconnect failed after %s attempts. Exiting...", reconnect_count)

def on_message(ws, message):
    jsonData = json.loads(message)
    if jsonData["type"] == 'status':
        result = client.publish("rec/bms/soc", jsonData["bms_array"]["master"]["soc"])
        result = client.publish("rec/bms/ibat", jsonData["bms_array"]["master"]["ibat"])
        result = client.publish("rec/bms/vbat", jsonData["bms_array"]["master"]["vbat"])

        result = client.publish("recbms/bms_array/master/time_remaining", jsonData["bms_array"]["master"]["time_remaining"])
        result = client.publish("recbms/bms_array/master/st_naprav", jsonData["bms_array"]["master"]["st_naprav"])
        result = client.publish("recbms/bms_array/master/time", jsonData["bms_array"]["master"]["time"])
        result = client.publish("recbms/bms_array/master/date", jsonData["bms_array"]["master"]["date"])
        result = client.publish("recbms/bms_array/master/mincell", jsonData["bms_array"]["master"]["mincell"])
        result = client.publish("recbms/bms_array/master/maxcell", jsonData["bms_array"]["master"]["maxcell"])
        result = client.publish("recbms/bms_array/master/ibat", jsonData["bms_array"]["master"]["ibat"])
        result = client.publish("recbms/bms_array/master/tmax", jsonData["bms_array"]["master"]["tmax"])
        result = client.publish("recbms/bms_array/master/vbat", jsonData["bms_array"]["master"]["vbat"])
        result = client.publish("recbms/bms_array/master/soc", jsonData["bms_array"]["master"]["soc"])
        result = client.publish("recbms/bms_array/master/soh", jsonData["bms_array"]["master"]["soh"])


        # slave 0
        result = client.publish("recbms/bms_array/slave/0/address", jsonData["bms_array"]["slave"]["0"]["address"])
        result = client.publish("recbms/bms_array/slave/0/st_temp", jsonData["bms_array"]["slave"]["0"]["st_temp"])
        result = client.publish("recbms/bms_array/slave/0/temp_bms", jsonData["bms_array"]["slave"]["0"]["temp_bms"])
        result = client.publish("recbms/bms_array/slave/0/st_celic", jsonData["bms_array"]["slave"]["0"]["st_celic"])
        result = client.publish("recbms/bms_array/slave/0/temp", jsonData["bms_array"]["slave"]["0"]["temp"][0])

        result = client.publish("recbms/bms_array/slave/0/res/0", jsonData["bms_array"]["slave"]["0"]["res"][0])
        result = client.publish("recbms/bms_array/slave/0/res/1", jsonData["bms_array"]["slave"]["0"]["res"][1])
        result = client.publish("recbms/bms_array/slave/0/res/2", jsonData["bms_array"]["slave"]["0"]["res"][2])
        result = client.publish("recbms/bms_array/slave/0/res/3", jsonData["bms_array"]["slave"]["0"]["res"][3])
        result = client.publish("recbms/bms_array/slave/0/res/4", jsonData["bms_array"]["slave"]["0"]["res"][4])
        result = client.publish("recbms/bms_array/slave/0/res/5", jsonData["bms_array"]["slave"]["0"]["res"][5])
        result = client.publish("recbms/bms_array/slave/0/res/6", jsonData["bms_array"]["slave"]["0"]["res"][6])
        result = client.publish("recbms/bms_array/slave/0/res/7", jsonData["bms_array"]["slave"]["0"]["res"][7])
        result = client.publish("recbms/bms_array/slave/0/res/8", jsonData["bms_array"]["slave"]["0"]["res"][8])
        result = client.publish("recbms/bms_array/slave/0/res/9", jsonData["bms_array"]["slave"]["0"]["res"][9])
        result = client.publish("recbms/bms_array/slave/0/res/10", jsonData["bms_array"]["slave"]["0"]["res"][10])
        result = client.publish("recbms/bms_array/slave/0/res/11", jsonData["bms_array"]["slave"]["0"]["res"][11])

        result = client.publish("recbms/bms_array/slave/0/nap/0", jsonData["bms_array"]["slave"]["0"]["nap"][0])
        result = client.publish("recbms/bms_array/slave/0/nap/1", jsonData["bms_array"]["slave"]["0"]["nap"][1])
        result = client.publish("recbms/bms_array/slave/0/nap/2", jsonData["bms_array"]["slave"]["0"]["nap"][2])
        result = client.publish("recbms/bms_array/slave/0/nap/3", jsonData["bms_array"]["slave"]["0"]["nap"][3])
        result = client.publish("recbms/bms_array/slave/0/nap/4", jsonData["bms_array"]["slave"]["0"]["nap"][4])
        result = client.publish("recbms/bms_array/slave/0/nap/5", jsonData["bms_array"]["slave"]["0"]["nap"][5])
        result = client.publish("recbms/bms_array/slave/0/nap/6", jsonData["bms_array"]["slave"]["0"]["nap"][6])
        result = client.publish("recbms/bms_array/slave/0/nap/7", jsonData["bms_array"]["slave"]["0"]["nap"][7])
        result = client.publish("recbms/bms_array/slave/0/nap/8", jsonData["bms_array"]["slave"]["0"]["nap"][8])
        result = client.publish("recbms/bms_array/slave/0/nap/9", jsonData["bms_array"]["slave"]["0"]["nap"][9])
        result = client.publish("recbms/bms_array/slave/0/nap/10", jsonData["bms_array"]["slave"]["0"]["nap"][10])
        result = client.publish("recbms/bms_array/slave/0/nap/11", jsonData["bms_array"]["slave"]["0"]["nap"][11])

        # slave 1
        result = client.publish("recbms/bms_array/slave/1/address", jsonData["bms_array"]["slave"]["0"]["address"])
        result = client.publish("recbms/bms_array/slave/1/st_temp", jsonData["bms_array"]["slave"]["0"]["st_temp"])
        result = client.publish("recbms/bms_array/slave/1/temp_bms", jsonData["bms_array"]["slave"]["0"]["temp_bms"])
        result = client.publish("recbms/bms_array/slave/1/st_celic", jsonData["bms_array"]["slave"]["0"]["st_celic"])
        result = client.publish("recbms/bms_array/slave/1/temp", jsonData["bms_array"]["slave"]["0"]["temp"][0])

        result = client.publish("recbms/bms_array/slave/1/res/0", jsonData["bms_array"]["slave"]["0"]["res"][0])
        result = client.publish("recbms/bms_array/slave/1/res/1", jsonData["bms_array"]["slave"]["0"]["res"][1])
        result = client.publish("recbms/bms_array/slave/1/res/2", jsonData["bms_array"]["slave"]["0"]["res"][2])
        result = client.publish("recbms/bms_array/slave/1/res/3", jsonData["bms_array"]["slave"]["0"]["res"][3])
        result = client.publish("recbms/bms_array/slave/1/res/4", jsonData["bms_array"]["slave"]["0"]["res"][4])
        result = client.publish("recbms/bms_array/slave/1/res/5", jsonData["bms_array"]["slave"]["0"]["res"][5])
        result = client.publish("recbms/bms_array/slave/1/res/6", jsonData["bms_array"]["slave"]["0"]["res"][6])
        result = client.publish("recbms/bms_array/slave/1/res/7", jsonData["bms_array"]["slave"]["0"]["res"][7])
        result = client.publish("recbms/bms_array/slave/1/res/8", jsonData["bms_array"]["slave"]["0"]["res"][8])
        result = client.publish("recbms/bms_array/slave/1/res/9", jsonData["bms_array"]["slave"]["0"]["res"][9])
        result = client.publish("recbms/bms_array/slave/1/res/10", jsonData["bms_array"]["slave"]["0"]["res"][10])
        result = client.publish("recbms/bms_array/slave/1/res/11", jsonData["bms_array"]["slave"]["0"]["res"][11])

        result = client.publish("recbms/bms_array/slave/1/nap/0", jsonData["bms_array"]["slave"]["0"]["nap"][0])
        result = client.publish("recbms/bms_array/slave/1/nap/1", jsonData["bms_array"]["slave"]["0"]["nap"][1])
        result = client.publish("recbms/bms_array/slave/1/nap/2", jsonData["bms_array"]["slave"]["0"]["nap"][2])
        result = client.publish("recbms/bms_array/slave/1/nap/3", jsonData["bms_array"]["slave"]["0"]["nap"][3])
        result = client.publish("recbms/bms_array/slave/1/nap/4", jsonData["bms_array"]["slave"]["0"]["nap"][4])
        result = client.publish("recbms/bms_array/slave/1/nap/5", jsonData["bms_array"]["slave"]["0"]["nap"][5])
        result = client.publish("recbms/bms_array/slave/1/nap/6", jsonData["bms_array"]["slave"]["0"]["nap"][6])
        result = client.publish("recbms/bms_array/slave/1/nap/7", jsonData["bms_array"]["slave"]["0"]["nap"][7])
        result = client.publish("recbms/bms_array/slave/1/nap/8", jsonData["bms_array"]["slave"]["0"]["nap"][8])
        result = client.publish("recbms/bms_array/slave/1/nap/9", jsonData["bms_array"]["slave"]["0"]["nap"][9])
        result = client.publish("recbms/bms_array/slave/1/nap/10", jsonData["bms_array"]["slave"]["0"]["nap"][10])
        result = client.publish("recbms/bms_array/slave/1/nap/11", jsonData["bms_array"]["slave"]["0"]["nap"][11])

        # slave 2
        result = client.publish("recbms/bms_array/slave/2/address", jsonData["bms_array"]["slave"]["0"]["address"])
        result = client.publish("recbms/bms_array/slave/2/st_temp", jsonData["bms_array"]["slave"]["0"]["st_temp"])
        result = client.publish("recbms/bms_array/slave/2/temp_bms", jsonData["bms_array"]["slave"]["0"]["temp_bms"])
        result = client.publish("recbms/bms_array/slave/2/st_celic", jsonData["bms_array"]["slave"]["0"]["st_celic"])
        result = client.publish("recbms/bms_array/slave/2/temp", jsonData["bms_array"]["slave"]["0"]["temp"][0])

        result = client.publish("recbms/bms_array/slave/2/res/0", jsonData["bms_array"]["slave"]["0"]["res"][0])
        result = client.publish("recbms/bms_array/slave/2/res/1", jsonData["bms_array"]["slave"]["0"]["res"][1])
        result = client.publish("recbms/bms_array/slave/2/res/2", jsonData["bms_array"]["slave"]["0"]["res"][2])
        result = client.publish("recbms/bms_array/slave/2/res/3", jsonData["bms_array"]["slave"]["0"]["res"][3])
        result = client.publish("recbms/bms_array/slave/2/res/4", jsonData["bms_array"]["slave"]["0"]["res"][4])
        result = client.publish("recbms/bms_array/slave/2/res/5", jsonData["bms_array"]["slave"]["0"]["res"][5])
        result = client.publish("recbms/bms_array/slave/2/res/6", jsonData["bms_array"]["slave"]["0"]["res"][6])
        result = client.publish("recbms/bms_array/slave/2/res/7", jsonData["bms_array"]["slave"]["0"]["res"][7])
        result = client.publish("recbms/bms_array/slave/2/res/8", jsonData["bms_array"]["slave"]["0"]["res"][8])
        result = client.publish("recbms/bms_array/slave/2/res/9", jsonData["bms_array"]["slave"]["0"]["res"][9])
        result = client.publish("recbms/bms_array/slave/2/res/10", jsonData["bms_array"]["slave"]["0"]["res"][10])
        result = client.publish("recbms/bms_array/slave/2/res/11", jsonData["bms_array"]["slave"]["0"]["res"][11])

        result = client.publish("recbms/bms_array/slave/2/nap/0", jsonData["bms_array"]["slave"]["0"]["nap"][0])
        result = client.publish("recbms/bms_array/slave/2/nap/1", jsonData["bms_array"]["slave"]["0"]["nap"][1])
        result = client.publish("recbms/bms_array/slave/2/nap/2", jsonData["bms_array"]["slave"]["0"]["nap"][2])
        result = client.publish("recbms/bms_array/slave/2/nap/3", jsonData["bms_array"]["slave"]["0"]["nap"][3])
        result = client.publish("recbms/bms_array/slave/2/nap/4", jsonData["bms_array"]["slave"]["0"]["nap"][4])
        result = client.publish("recbms/bms_array/slave/2/nap/5", jsonData["bms_array"]["slave"]["0"]["nap"][5])
        result = client.publish("recbms/bms_array/slave/2/nap/6", jsonData["bms_array"]["slave"]["0"]["nap"][6])
        result = client.publish("recbms/bms_array/slave/2/nap/7", jsonData["bms_array"]["slave"]["0"]["nap"][7])
        result = client.publish("recbms/bms_array/slave/2/nap/8", jsonData["bms_array"]["slave"]["0"]["nap"][8])
        result = client.publish("recbms/bms_array/slave/2/nap/9", jsonData["bms_array"]["slave"]["0"]["nap"][9])
        result = client.publish("recbms/bms_array/slave/2/nap/10", jsonData["bms_array"]["slave"]["0"]["nap"][10])
        result = client.publish("recbms/bms_array/slave/2/nap/11", jsonData["bms_array"]["slave"]["0"]["nap"][11])

        # slave 3
        result = client.publish("recbms/bms_array/slave/3/address", jsonData["bms_array"]["slave"]["0"]["address"])
        result = client.publish("recbms/bms_array/slave/3/st_temp", jsonData["bms_array"]["slave"]["0"]["st_temp"])
        result = client.publish("recbms/bms_array/slave/3/temp_bms", jsonData["bms_array"]["slave"]["0"]["temp_bms"])
        result = client.publish("recbms/bms_array/slave/3/st_celic", jsonData["bms_array"]["slave"]["0"]["st_celic"])
        result = client.publish("recbms/bms_array/slave/3/temp", jsonData["bms_array"]["slave"]["0"]["temp"][0])

        result = client.publish("recbms/bms_array/slave/3/res/0", jsonData["bms_array"]["slave"]["0"]["res"][0])
        result = client.publish("recbms/bms_array/slave/3/res/1", jsonData["bms_array"]["slave"]["0"]["res"][1])
        result = client.publish("recbms/bms_array/slave/3/res/2", jsonData["bms_array"]["slave"]["0"]["res"][2])
        result = client.publish("recbms/bms_array/slave/3/res/3", jsonData["bms_array"]["slave"]["0"]["res"][3])
        result = client.publish("recbms/bms_array/slave/3/res/4", jsonData["bms_array"]["slave"]["0"]["res"][4])
        result = client.publish("recbms/bms_array/slave/3/res/5", jsonData["bms_array"]["slave"]["0"]["res"][5])
        result = client.publish("recbms/bms_array/slave/3/res/6", jsonData["bms_array"]["slave"]["0"]["res"][6])
        result = client.publish("recbms/bms_array/slave/3/res/7", jsonData["bms_array"]["slave"]["0"]["res"][7])
        result = client.publish("recbms/bms_array/slave/3/res/8", jsonData["bms_array"]["slave"]["0"]["res"][8])
        result = client.publish("recbms/bms_array/slave/3/res/9", jsonData["bms_array"]["slave"]["0"]["res"][9])
        result = client.publish("recbms/bms_array/slave/3/res/10", jsonData["bms_array"]["slave"]["0"]["res"][10])
        result = client.publish("recbms/bms_array/slave/3/res/11", jsonData["bms_array"]["slave"]["0"]["res"][11])

        result = client.publish("recbms/bms_array/slave/3/nap/0", jsonData["bms_array"]["slave"]["0"]["nap"][0])
        result = client.publish("recbms/bms_array/slave/3/nap/1", jsonData["bms_array"]["slave"]["0"]["nap"][1])
        result = client.publish("recbms/bms_array/slave/3/nap/2", jsonData["bms_array"]["slave"]["0"]["nap"][2])
        result = client.publish("recbms/bms_array/slave/3/nap/3", jsonData["bms_array"]["slave"]["0"]["nap"][3])
        result = client.publish("recbms/bms_array/slave/3/nap/4", jsonData["bms_array"]["slave"]["0"]["nap"][4])
        result = client.publish("recbms/bms_array/slave/3/nap/5", jsonData["bms_array"]["slave"]["0"]["nap"][5])
        result = client.publish("recbms/bms_array/slave/3/nap/6", jsonData["bms_array"]["slave"]["0"]["nap"][6])
        result = client.publish("recbms/bms_array/slave/3/nap/7", jsonData["bms_array"]["slave"]["0"]["nap"][7])
        result = client.publish("recbms/bms_array/slave/3/nap/8", jsonData["bms_array"]["slave"]["0"]["nap"][8])
        result = client.publish("recbms/bms_array/slave/3/nap/9", jsonData["bms_array"]["slave"]["0"]["nap"][9])
        result = client.publish("recbms/bms_array/slave/3/nap/10", jsonData["bms_array"]["slave"]["0"]["nap"][10])
        result = client.publish("recbms/bms_array/slave/3/nap/11", jsonData["bms_array"]["slave"]["0"]["nap"][11])

        # slave 4
        result = client.publish("recbms/bms_array/slave/4/address", jsonData["bms_array"]["slave"]["0"]["address"])
        result = client.publish("recbms/bms_array/slave/4/st_temp", jsonData["bms_array"]["slave"]["0"]["st_temp"])
        result = client.publish("recbms/bms_array/slave/4/temp_bms", jsonData["bms_array"]["slave"]["0"]["temp_bms"])
        result = client.publish("recbms/bms_array/slave/4/st_celic", jsonData["bms_array"]["slave"]["0"]["st_celic"])
        result = client.publish("recbms/bms_array/slave/4/temp", jsonData["bms_array"]["slave"]["0"]["temp"][0])

        result = client.publish("recbms/bms_array/slave/4/res/0", jsonData["bms_array"]["slave"]["0"]["res"][0])
        result = client.publish("recbms/bms_array/slave/4/res/1", jsonData["bms_array"]["slave"]["0"]["res"][1])
        result = client.publish("recbms/bms_array/slave/4/res/2", jsonData["bms_array"]["slave"]["0"]["res"][2])
        result = client.publish("recbms/bms_array/slave/4/res/3", jsonData["bms_array"]["slave"]["0"]["res"][3])
        result = client.publish("recbms/bms_array/slave/4/res/4", jsonData["bms_array"]["slave"]["0"]["res"][4])
        result = client.publish("recbms/bms_array/slave/4/res/5", jsonData["bms_array"]["slave"]["0"]["res"][5])
        result = client.publish("recbms/bms_array/slave/4/res/6", jsonData["bms_array"]["slave"]["0"]["res"][6])
        result = client.publish("recbms/bms_array/slave/4/res/7", jsonData["bms_array"]["slave"]["0"]["res"][7])
        result = client.publish("recbms/bms_array/slave/4/res/8", jsonData["bms_array"]["slave"]["0"]["res"][8])
        result = client.publish("recbms/bms_array/slave/4/res/9", jsonData["bms_array"]["slave"]["0"]["res"][9])
        result = client.publish("recbms/bms_array/slave/4/res/10", jsonData["bms_array"]["slave"]["0"]["res"][10])
        result = client.publish("recbms/bms_array/slave/4/res/11", jsonData["bms_array"]["slave"]["0"]["res"][11])

        result = client.publish("recbms/bms_array/slave/4/nap/0", jsonData["bms_array"]["slave"]["0"]["nap"][0])
        result = client.publish("recbms/bms_array/slave/4/nap/1", jsonData["bms_array"]["slave"]["0"]["nap"][1])
        result = client.publish("recbms/bms_array/slave/4/nap/2", jsonData["bms_array"]["slave"]["0"]["nap"][2])
        result = client.publish("recbms/bms_array/slave/4/nap/3", jsonData["bms_array"]["slave"]["0"]["nap"][3])
        result = client.publish("recbms/bms_array/slave/4/nap/4", jsonData["bms_array"]["slave"]["0"]["nap"][4])
        result = client.publish("recbms/bms_array/slave/4/nap/5", jsonData["bms_array"]["slave"]["0"]["nap"][5])
        result = client.publish("recbms/bms_array/slave/4/nap/6", jsonData["bms_array"]["slave"]["0"]["nap"][6])
        result = client.publish("recbms/bms_array/slave/4/nap/7", jsonData["bms_array"]["slave"]["0"]["nap"][7])
        result = client.publish("recbms/bms_array/slave/4/nap/8", jsonData["bms_array"]["slave"]["0"]["nap"][8])
        result = client.publish("recbms/bms_array/slave/4/nap/9", jsonData["bms_array"]["slave"]["0"]["nap"][9])
        result = client.publish("recbms/bms_array/slave/4/nap/10", jsonData["bms_array"]["slave"]["0"]["nap"][10])
        result = client.publish("recbms/bms_array/slave/4/nap/11", jsonData["bms_array"]["slave"]["0"]["nap"][11])

        # slave 5
        result = client.publish("recbms/bms_array/slave/5/address", jsonData["bms_array"]["slave"]["0"]["address"])
        result = client.publish("recbms/bms_array/slave/5/st_temp", jsonData["bms_array"]["slave"]["0"]["st_temp"])
        result = client.publish("recbms/bms_array/slave/5/temp_bms", jsonData["bms_array"]["slave"]["0"]["temp_bms"])
        result = client.publish("recbms/bms_array/slave/5/st_celic", jsonData["bms_array"]["slave"]["0"]["st_celic"])
        result = client.publish("recbms/bms_array/slave/5/temp", jsonData["bms_array"]["slave"]["0"]["temp"][0])

        result = client.publish("recbms/bms_array/slave/5/res/0", jsonData["bms_array"]["slave"]["0"]["res"][0])
        result = client.publish("recbms/bms_array/slave/5/res/1", jsonData["bms_array"]["slave"]["0"]["res"][1])
        result = client.publish("recbms/bms_array/slave/5/res/2", jsonData["bms_array"]["slave"]["0"]["res"][2])
        result = client.publish("recbms/bms_array/slave/5/res/3", jsonData["bms_array"]["slave"]["0"]["res"][3])
        result = client.publish("recbms/bms_array/slave/5/res/4", jsonData["bms_array"]["slave"]["0"]["res"][4])
        result = client.publish("recbms/bms_array/slave/5/res/5", jsonData["bms_array"]["slave"]["0"]["res"][5])
        result = client.publish("recbms/bms_array/slave/5/res/6", jsonData["bms_array"]["slave"]["0"]["res"][6])
        result = client.publish("recbms/bms_array/slave/5/res/7", jsonData["bms_array"]["slave"]["0"]["res"][7])
        result = client.publish("recbms/bms_array/slave/5/res/8", jsonData["bms_array"]["slave"]["0"]["res"][8])
        result = client.publish("recbms/bms_array/slave/5/res/9", jsonData["bms_array"]["slave"]["0"]["res"][9])
        result = client.publish("recbms/bms_array/slave/5/res/10", jsonData["bms_array"]["slave"]["0"]["res"][10])
        result = client.publish("recbms/bms_array/slave/5/res/11", jsonData["bms_array"]["slave"]["0"]["res"][11])

        result = client.publish("recbms/bms_array/slave/5/nap/0", jsonData["bms_array"]["slave"]["0"]["nap"][0])
        result = client.publish("recbms/bms_array/slave/5/nap/1", jsonData["bms_array"]["slave"]["0"]["nap"][1])
        result = client.publish("recbms/bms_array/slave/5/nap/2", jsonData["bms_array"]["slave"]["0"]["nap"][2])
        result = client.publish("recbms/bms_array/slave/5/nap/3", jsonData["bms_array"]["slave"]["0"]["nap"][3])
        result = client.publish("recbms/bms_array/slave/5/nap/4", jsonData["bms_array"]["slave"]["0"]["nap"][4])
        result = client.publish("recbms/bms_array/slave/5/nap/5", jsonData["bms_array"]["slave"]["0"]["nap"][5])
        result = client.publish("recbms/bms_array/slave/5/nap/6", jsonData["bms_array"]["slave"]["0"]["nap"][6])
        result = client.publish("recbms/bms_array/slave/5/nap/7", jsonData["bms_array"]["slave"]["0"]["nap"][7])
        result = client.publish("recbms/bms_array/slave/5/nap/8", jsonData["bms_array"]["slave"]["0"]["nap"][8])
        result = client.publish("recbms/bms_array/slave/5/nap/9", jsonData["bms_array"]["slave"]["0"]["nap"][9])
        result = client.publish("recbms/bms_array/slave/5/nap/10", jsonData["bms_array"]["slave"]["0"]["nap"][10])
        result = client.publish("recbms/bms_array/slave/5/nap/11", jsonData["bms_array"]["slave"]["0"]["nap"][11])

        # slave 6
        result = client.publish("recbms/bms_array/slave/6/address", jsonData["bms_array"]["slave"]["0"]["address"])
        result = client.publish("recbms/bms_array/slave/6/st_temp", jsonData["bms_array"]["slave"]["0"]["st_temp"])
        result = client.publish("recbms/bms_array/slave/6/temp_bms", jsonData["bms_array"]["slave"]["0"]["temp_bms"])
        result = client.publish("recbms/bms_array/slave/6/st_celic", jsonData["bms_array"]["slave"]["0"]["st_celic"])
        result = client.publish("recbms/bms_array/slave/6/temp", jsonData["bms_array"]["slave"]["0"]["temp"][0])

        result = client.publish("recbms/bms_array/slave/6/res/0", jsonData["bms_array"]["slave"]["0"]["res"][0])
        result = client.publish("recbms/bms_array/slave/6/res/1", jsonData["bms_array"]["slave"]["0"]["res"][1])
        result = client.publish("recbms/bms_array/slave/6/res/2", jsonData["bms_array"]["slave"]["0"]["res"][2])
        result = client.publish("recbms/bms_array/slave/6/res/3", jsonData["bms_array"]["slave"]["0"]["res"][3])
        result = client.publish("recbms/bms_array/slave/6/res/4", jsonData["bms_array"]["slave"]["0"]["res"][4])
        result = client.publish("recbms/bms_array/slave/6/res/5", jsonData["bms_array"]["slave"]["0"]["res"][5])
        result = client.publish("recbms/bms_array/slave/6/res/6", jsonData["bms_array"]["slave"]["0"]["res"][6])
        result = client.publish("recbms/bms_array/slave/6/res/7", jsonData["bms_array"]["slave"]["0"]["res"][7])
        result = client.publish("recbms/bms_array/slave/6/res/8", jsonData["bms_array"]["slave"]["0"]["res"][8])
        result = client.publish("recbms/bms_array/slave/6/res/9", jsonData["bms_array"]["slave"]["0"]["res"][9])
        result = client.publish("recbms/bms_array/slave/6/res/10", jsonData["bms_array"]["slave"]["0"]["res"][10])
        result = client.publish("recbms/bms_array/slave/6/res/11", jsonData["bms_array"]["slave"]["0"]["res"][11])

        result = client.publish("recbms/bms_array/slave/6/nap/0", jsonData["bms_array"]["slave"]["0"]["nap"][0])
        result = client.publish("recbms/bms_array/slave/6/nap/1", jsonData["bms_array"]["slave"]["0"]["nap"][1])
        result = client.publish("recbms/bms_array/slave/6/nap/2", jsonData["bms_array"]["slave"]["0"]["nap"][2])
        result = client.publish("recbms/bms_array/slave/6/nap/3", jsonData["bms_array"]["slave"]["0"]["nap"][3])
        result = client.publish("recbms/bms_array/slave/6/nap/4", jsonData["bms_array"]["slave"]["0"]["nap"][4])
        result = client.publish("recbms/bms_array/slave/6/nap/5", jsonData["bms_array"]["slave"]["0"]["nap"][5])
        result = client.publish("recbms/bms_array/slave/6/nap/6", jsonData["bms_array"]["slave"]["0"]["nap"][6])
        result = client.publish("recbms/bms_array/slave/6/nap/7", jsonData["bms_array"]["slave"]["0"]["nap"][7])
        result = client.publish("recbms/bms_array/slave/6/nap/8", jsonData["bms_array"]["slave"]["0"]["nap"][8])
        result = client.publish("recbms/bms_array/slave/6/nap/9", jsonData["bms_array"]["slave"]["0"]["nap"][9])
        result = client.publish("recbms/bms_array/slave/6/nap/10", jsonData["bms_array"]["slave"]["0"]["nap"][10])
        result = client.publish("recbms/bms_array/slave/6/nap/11", jsonData["bms_array"]["slave"]["0"]["nap"][11])

        # slave 7
        result = client.publish("recbms/bms_array/slave/7/address", jsonData["bms_array"]["slave"]["0"]["address"])
        result = client.publish("recbms/bms_array/slave/7/st_temp", jsonData["bms_array"]["slave"]["0"]["st_temp"])
        result = client.publish("recbms/bms_array/slave/7/temp_bms", jsonData["bms_array"]["slave"]["0"]["temp_bms"])
        result = client.publish("recbms/bms_array/slave/7/st_celic", jsonData["bms_array"]["slave"]["0"]["st_celic"])
        result = client.publish("recbms/bms_array/slave/7/temp", jsonData["bms_array"]["slave"]["0"]["temp"][0])

        result = client.publish("recbms/bms_array/slave/7/res/0", jsonData["bms_array"]["slave"]["0"]["res"][0])
        result = client.publish("recbms/bms_array/slave/7/res/1", jsonData["bms_array"]["slave"]["0"]["res"][1])
        result = client.publish("recbms/bms_array/slave/7/res/2", jsonData["bms_array"]["slave"]["0"]["res"][2])
        result = client.publish("recbms/bms_array/slave/7/res/3", jsonData["bms_array"]["slave"]["0"]["res"][3])
        result = client.publish("recbms/bms_array/slave/7/res/4", jsonData["bms_array"]["slave"]["0"]["res"][4])
        result = client.publish("recbms/bms_array/slave/7/res/5", jsonData["bms_array"]["slave"]["0"]["res"][5])
        result = client.publish("recbms/bms_array/slave/7/res/6", jsonData["bms_array"]["slave"]["0"]["res"][6])
        result = client.publish("recbms/bms_array/slave/7/res/7", jsonData["bms_array"]["slave"]["0"]["res"][7])
        result = client.publish("recbms/bms_array/slave/7/res/8", jsonData["bms_array"]["slave"]["0"]["res"][8])
        result = client.publish("recbms/bms_array/slave/7/res/9", jsonData["bms_array"]["slave"]["0"]["res"][9])
        result = client.publish("recbms/bms_array/slave/7/res/10", jsonData["bms_array"]["slave"]["0"]["res"][10])
        result = client.publish("recbms/bms_array/slave/7/res/11", jsonData["bms_array"]["slave"]["0"]["res"][11])

        result = client.publish("recbms/bms_array/slave/7/nap/0", jsonData["bms_array"]["slave"]["0"]["nap"][0])
        result = client.publish("recbms/bms_array/slave/7/nap/1", jsonData["bms_array"]["slave"]["0"]["nap"][1])
        result = client.publish("recbms/bms_array/slave/7/nap/2", jsonData["bms_array"]["slave"]["0"]["nap"][2])
        result = client.publish("recbms/bms_array/slave/7/nap/3", jsonData["bms_array"]["slave"]["0"]["nap"][3])
        result = client.publish("recbms/bms_array/slave/7/nap/4", jsonData["bms_array"]["slave"]["0"]["nap"][4])
        result = client.publish("recbms/bms_array/slave/7/nap/5", jsonData["bms_array"]["slave"]["0"]["nap"][5])
        result = client.publish("recbms/bms_array/slave/7/nap/6", jsonData["bms_array"]["slave"]["0"]["nap"][6])
        result = client.publish("recbms/bms_array/slave/7/nap/7", jsonData["bms_array"]["slave"]["0"]["nap"][7])
        result = client.publish("recbms/bms_array/slave/7/nap/8", jsonData["bms_array"]["slave"]["0"]["nap"][8])
        result = client.publish("recbms/bms_array/slave/7/nap/9", jsonData["bms_array"]["slave"]["0"]["nap"][9])
        result = client.publish("recbms/bms_array/slave/7/nap/10", jsonData["bms_array"]["slave"]["0"]["nap"][10])
        result = client.publish("recbms/bms_array/slave/7/nap/11", jsonData["bms_array"]["slave"]["0"]["nap"][11])

        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send status message to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
    else:
        print(f"Ignored settings message")

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

if __name__ == "__main__":
    # mqtt setup:
    client_id = f'rec-bms-{random.randint(0, 1000)}'
    
    client = connect_mqtt()
    client.loop_start()
    
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://10.0.0.95/ws",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
    client.loop_stop()