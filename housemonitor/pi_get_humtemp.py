from Adafruit_DHT import DHT22 as sensor
from Adafruit_DHT import read as dht_read

# specify the port connected to the sensor.
GPIO_port = 14


def get_humtemp():
    humidity, temp = dht_read(sensor, GPIO_port)
    return (temp, humidity)
