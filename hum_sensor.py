from smbus2 import SMBus
from time import sleep
from datetime import datetime
from uuid import getnode as get_mac
from csv import writer


class HumSensor:
    def __init__(self, read_freq=10, save_directory='humidity_data.csv'):
        self.mac = get_mac()  # mac id of the raspberry
        self.read_freq = read_freq  # how often sensor read data and save
        self.save_directory = save_directory  # directory to save data
        self.time, self.cTemp, self.humidity = None, None, None  # placeholders for the data that will be read

    def read_sensor(self):
        bus = SMBus(1)
        bus.write_i2c_block_data(0x44, 0x2C, [0x06])
        sleep(0.5)  # wait for sensor to settle
        data = bus.read_i2c_block_data(0x44, 0x00, 6)

        # convert raw data to readable format
        self.cTemp = int(((((data[0] * 256.0) + data[1]) * 175) / 65535.0) - 45)
        self.humidity = int(100 * (data[3] * 256 + data[4]) / 65535.0)
        now = datetime.now()
        self.time = now.strftime("%d/%m/%Y %H:%M:%S")

        bus.close()

    def save_data(self):
        with open(self.save_directory, mode='a') as f:
            f = writer(f, delimiter=';', lineterminator='\n')
            f.writerow([self.mac, self.time, self.cTemp, self.humidity])

    def run(self):
        while True:
            try:
                humsensor.read_sensor()
                humsensor.save_data()
                sleep(self.read_freq)
            except KeyboardInterrupt:
                print("Iteration Interrupted by User")
                break

if __name__ == "__main__":
    humsensor = HumSensor()
    humsensor.run()

