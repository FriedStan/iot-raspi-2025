import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ledpin = 12
GPIO.setup(ledpin, GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin, 1000)
pi_pwm.start(0)


MQTT_BROKER = 'mqtt-dashboard.com'  
MQTT_PORT = 1883
MQTT_TOPIC = '66070030/as3sfe'

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic once connected
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, message):
    text = message.payload.decode()
    print(f"Received message '{text}' on topic '{message.topic}'")
    if text == "on":
        pi_pwm.ChangeDutyCycle(100)
    elif text == "off":
        pi_pwm.ChangeDutyCycle(0)
    elif str(text).isdigit():
        pi_pwm.ChangeDutyCycle(int(text))

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
        pass
except KeyboardInterrupt:
    # Stop the loop and disconnect gracefully on keyboard interrupt
    client.loop_stop()
    client.disconnect()