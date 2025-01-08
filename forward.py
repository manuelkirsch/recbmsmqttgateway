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
recip = os.environ['REC_IP']

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
        # status message
        result = client.publish("recbms/status", jsonData["bms_array"])

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

        for index, slave in enumerate(jsonData["bms_array"]["slave"]):
            result = client.publish("recbms/bms_array/slave/"+str(index)+"/address", jsonData["bms_array"]["slave"][str(index)]["address"])
            result = client.publish("recbms/bms_array/slave/"+str(index)+"/st_temp", jsonData["bms_array"]["slave"][str(index)]["st_temp"])
            result = client.publish("recbms/bms_array/slave/"+str(index)+"/temp_bms", jsonData["bms_array"]["slave"][str(index)]["temp_bms"])
            result = client.publish("recbms/bms_array/slave/"+str(index)+"/st_celic", jsonData["bms_array"]["slave"][str(index)]["st_celic"])
            
            for tempindex, temp in enumerate(jsonData["bms_array"]["slave"][str(index)]["temp"]):
                result = client.publish("recbms/bms_array/slave/"+str(index)+"/temp/"+str(tempindex), jsonData["bms_array"]["slave"][str(index)]["temp"][str(tempindex)])

            for resindex, res in enumerate(jsonData["bms_array"]["slave"][str(index)]["res"]):
                result = client.publish("recbms/bms_array/slave/"+str(index)+"/res/"+str(resindex), jsonData["bms_array"]["slave"][str(index)]["res"][str(resindex)])

            for napindex, nap in enumerate(jsonData["bms_array"]["slave"][str(index)]["nap"]):
                result = client.publish("recbms/bms_array/slave/"+str(index)+"/nap/"+str(napindex), jsonData["bms_array"]["slave"][str(index)]["nap"][str(napindex)])

        status = result[0]
        if status != 0:
            print(f"Failed to send message to topic {topic}")
    #else:
        # settings message
        #print(f"Ignored settings message")

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
    ws = websocket.WebSocketApp("ws://"+recip+"/ws",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
    client.loop_stop()