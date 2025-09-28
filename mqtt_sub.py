import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LIGHT=4
BUTTON=17
GPIO.setup(LIGHT,GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN)


MQTT_BROKER = 'mqtt-dashboard.com'  
MQTT_PORT = 1883
MQTT_TOPIC = '34asdw4g/66070030'

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic once connected
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, message):
    text = message.payload.decode()
    print(f"Received message '{text}' on topic '{message.topic}'")
    if text == "ON":
        GPIO.output(LIGHT,True)
    elif text == "OFF":
        GPIO.output(LIGHT,False)

# Create a new MQTT client instance
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the loop to process network traffic and dispatch callbacks
client.loop_start()

try:
    # Keep the script running
    while True:
        val=GPIO.input(BUTTON)
        if val == 1:
            client.publish(MQTT_TOPIC, "ON")
            time.sleep(1)
except KeyboardInterrupt:
    # Stop the loop and disconnect gracefully on keyboard interrupt
    client.loop_stop()
    client.disconnect()