import paho.mqtt.client as mqtt
import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000


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


def ReadChannel(channel):
    adc = spi.xfer2([6 | (channel & 4) >> 2, (channel & 3) << 6, 0])
    data = ((adc[1] & 15) << 8) + adc[2]
    return data

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
        reading = ReadChannel(0)
        voltage = (reading * 3.3) / 4096
        percent = reading / 4096 * 100
        time.sleep(0.3)
        client.publish(MQTT_TOPIC, percent)
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the loop and disconnect gracefully on keyboard interrupt
    client.loop_stop()
    client.disconnect()