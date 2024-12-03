import paho.mqtt.client as mqtt
import json
import os
from dotenv import load_dotenv
import supplement_calculator

load_dotenv()

TOPIC_ID = os.getenv('TOPIC_ID')
INPUT_TOPIC = 'BRE/calculateWinterSupplementInput/' + TOPIC_ID
OUTPUT_TOPIC = 'BRE/calculateWinterSupplementOutput/' + TOPIC_ID
        
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(INPUT_TOPIC)

def on_message(client, userdata, msg):
    in_data = json.loads(msg.payload)
    print(f"Input data recieved: {in_data}")
    try:
        out_data = supplement_calculator.calculate(in_data)
        print(f"Results: {out_data}")
        client.publish(OUTPUT_TOPIC, json.dumps(out_data))
    except Exception as e:
        print(e)

def initialize_client():
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    return mqttc