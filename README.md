# raspberrypi

This repo contains the some of the Raspberry Pi codes.

hum_sensor.py is a code that tracks the temperature and humidity using SHT30 sensor. The code is written in Python. It reads the data from the sensor using System Management Bus (SMBus) protocol and writes the collected data in a specified directory as a csv file. The csv file contains the mac address of the device, date, time, temperature and humidity. One can track the temperature and humidity in an environment as a function of time. The read frequency can be changed by the read_freq parameter. It is 10 seconds by default.

<img width="552" alt="raspberry" src="https://user-images.githubusercontent.com/50638609/148169020-aaa01722-ca98-4f56-af8d-cedef5cdb5e0.png">
