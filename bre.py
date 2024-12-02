import paho.mqtt.client as mqtt
import json
import os
from dotenv import load_dotenv

load_dotenv()

BROKER = 'test.mosquitto.org'
PORT = 1883
TOPIC_ID = os.getenv('TOPIC_ID')

INPUT_TOPIC = 'BRE/calculateWinterSupplementInput/' + TOPIC_ID
OUTPUT_TOPIC = 'BRE/calculateWinterSupplementOutput/' + TOPIC_ID

def eligibility_calculator(in_data):
    id = in_data['id']
    is_eligible = in_data['familyUnitInPayForDecember']
    if not is_eligible:
        base_amount = children_amount = supplement_amount = 0.0
    else:
        if in_data['familyComposition'] == 'single':
            base_amount = 60.0
        elif in_data['familyComposition'] == 'couple':
            base_amount = 120.0
        else:
            raise Exception("Invalid familyComposition value")
        children_amount = in_data['numberOfChildren']*20.0
        supplement_amount = base_amount + children_amount

    return {
        'id': id,
        'isEligible': is_eligible,
        'baseAmount': base_amount,
        'childrenAmount': children_amount,
        'supplementAmount': supplement_amount
    }
        
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(INPUT_TOPIC)

def on_message(client, userdata, msg):
    in_data = json.loads(msg.payload)
    print(f"Input data recieved: {in_data}")
    out_data = eligibility_calculator(in_data)
    print(f"Results: {out_data}")
    client.publish(OUTPUT_TOPIC, json.dumps(out_data))


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

def main():
    mqttc.connect(BROKER, PORT, 60)
    mqttc.loop_forever()


if __name__ == '__main__':
    main()