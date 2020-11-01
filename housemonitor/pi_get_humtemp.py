##

from Adafruit_DHT import read as dht_read
from Adafruit_DHT import DHT22 as sensor

# specify the port connected to the sensor.
GPIO_port = 14

humidity, temp = dht_read(sensor, GPIO_port)
print(f"Temperature = {str(temp)}")
print(f"Humidity = {str(humidity)}")
