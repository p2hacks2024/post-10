import smbus
import time
import os
import sys

# センサーのI2Cアドレス
SENSOR_1_ADDR_ACCL = 0x19  # 実物センサーの加速度アドレス
SENSOR_2_ADDR_ACCL = 0x18  # 仮想センサーの加速度アドレス

# I2Cバスのインスタンス
bus_sensor_1 = smbus.SMBus(1)  # 実物センサーはバス1
bus_sensor_2 = smbus.SMBus(3)  # 仮想センサーはバス3

def write_byte(bus, addr, reg, value):
    bus.write_byte_data(addr, reg, value)
    time.sleep(0.1)

def read_bytes(bus, addr, reg, length):
    return bus.read_i2c_block_data(addr, reg, length)

def BMX055_Accl_Init(bus, addr):
    # 加速度センサの初期化
    write_byte(bus, addr, 0x0F, 0x03)  # Range = ±2g
    write_byte(bus, addr, 0x10, 0x08)  # Bandwidth = 7.81Hz
    write_byte(bus, addr, 0x11, 0x00)  # Normal mode

def BMX055_Accl(bus, addr):
    data = read_bytes(bus, addr, 0x02, 6)
    xAccl = ((data[1] << 8) | (data[0] & 0xF0)) >> 4
    yAccl = ((data[3] << 8) | (data[2] & 0xF0)) >> 4
    zAccl = ((data[5] << 8) | (data[4] & 0xF0)) >> 4
    if xAccl > 2047: xAccl -= 4096
    if yAccl > 2047: yAccl -= 4096
    if zAccl > 2047: zAccl -= 4096
    xAccl, yAccl, zAccl = xAccl * 0.00098, yAccl * 0.00098, zAccl * 0.00098
    return xAccl, yAccl, zAccl

def record_audio():
    print("Z-axis value is below 0.70. Starting recording...")
    os.system("arecord -D plughw:3,0 -f cd -t wav -d 5 output.wav")
    print("Recording saved to output.wav")

if __name__ == "__main__":
    # 両方のセンサーを初期化
    BMX055_Accl_Init(bus_sensor_1, SENSOR_1_ADDR_ACCL)
    BMX055_Accl_Init(bus_sensor_2, SENSOR_2_ADDR_ACCL)

    while True:
        # 1つ目のセンサーからデータ取得
        x1, y1, z1 = BMX055_Accl(bus_sensor_1, SENSOR_1_ADDR_ACCL)
        print(f"Sensor 1 Accl= {x1:.2f}, {y1:.2f}, {z1:.2f}")

        # 2つ目のセンサーからデータ取得
        x2, y2, z2 = BMX055_Accl(bus_sensor_2, SENSOR_2_ADDR_ACCL)
        print(f"Sensor 2 Accl= {x2:.2f}, {y2:.2f}, {z2:.2f}")

        # 任意の条件で録音を開始
        if z1 < 0.70 or z2 < 0.70:
            record_audio()
            sys.exit(0)

        print("--------------------------------------")
        time.sleep(1)
