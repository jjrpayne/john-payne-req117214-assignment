import mqtt_client

BROKER = 'test.mosquitto.org'
PORT = 1883

def main():
    mqttc = mqtt_client.initialize_client()
    mqttc.connect(BROKER, PORT, 60)
    mqttc.loop_forever()

if __name__ == '__main__':
    main()