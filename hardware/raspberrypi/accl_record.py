import smbus
import time
import os
import sys


class AcclRecord():
    def __init__(self, bus_sensor, sensor_addr):
        self.bus_sensor = bus_sensor
        self.sensor_addr = sensor_addr
        self.x = 0
        self.y = 0
        self.z = 0
        # センサーを初期化
        self._BMX055_Accl_Init()


    def BMX055_Accl(self):
        data = self._read_bytes(0x02, 6)
        xAccl = ((data[1] << 8) | (data[0] & 0xF0)) >> 4
        yAccl = ((data[3] << 8) | (data[2] & 0xF0)) >> 4
        zAccl = ((data[5] << 8) | (data[4] & 0xF0)) >> 4

        if xAccl > 2047: xAccl -= 4096
        if yAccl > 2047: yAccl -= 4096
        if zAccl > 2047: zAccl -= 4096
        
        xAccl, yAccl, zAccl = xAccl * 0.00098, yAccl * 0.00098, zAccl * 0.00098
        
        self.x = xAccl
        self.y = yAccl
        self.z = zAccl

        return xAccl, yAccl, zAccl


    def _BMX055_Accl_Init(self):
        # 加速度センサの初期化
        self._write_byte(0x0F, 0x03)  # Range = ±2g
        self._write_byte(0x10, 0x08)  # Bandwidth = 7.81Hz
        self._write_byte(0x11, 0x00)  # Normal mode


    def _write_byte(self, reg, value):
        self.bus_sensor.write_byte_data(self.sensor_addr, reg, value)
        time.sleep(0.1)


    def _read_bytes(self, reg, length):
        return self.bus_sensor.read_i2c_block_data(self.sensor_addr, reg, length)


def record_audio():
    print("Z-axis value is below 0.70. Starting recording...")
    os.system("arecord -D plughw:3,0 -f cd -t wav -d 5 output.wav")
    print("Recording saved to output.wav")

if __name__ == "__main__":
    # センサーのI2Cアドレス
    SENSOR_1_ADDR_ACCL = 0x19  # 実物センサーの加速度アドレス
    SENSOR_2_ADDR_ACCL = 0x18  # 仮想センサーの加速度アドレス

    # I2Cバスのインスタンス
    bus_sensor_1 = smbus.SMBus(1)  # 実物センサーはバス1
    bus_sensor_2 = smbus.SMBus(3)  # 仮想センサーはバス3

    accl_record_1 = AcclRecord(bus_sensor_1, SENSOR_1_ADDR_ACCL)
    accl_record_2 = AcclRecord(bus_sensor_2, SENSOR_2_ADDR_ACCL)

    while True:
        # 1つ目のセンサーからデータ取得
        x1, y1, z1 = accl_record_1.BMX055_Accl()
        print(f"Sensor 1 Accl= {x1:.2f}, {y1:.2f}, {z1:.2f}")

        # 2つ目のセンサーからデータ取得
        x2, y2, z2 = accl_record_2.BMX055_Accl()
        print(f"Sensor 2 Accl= {x2:.2f}, {y2:.2f}, {z2:.2f}")

        # 任意の条件で録音を開始
        if z1 < 0.70 or z2 < 0.70:
            record_audio()
            sys.exit(0)

        print("--------------------------------------")
        time.sleep(1)
