import smbus
import time
import os  # 録音のために使用
import sys  # プログラムを終了させるために使用

# BMX055センサのI2Cアドレス
Addr_Accl = 0x19

# I2Cバスの初期化
bus = smbus.SMBus(1)  # Raspberry PiではI2Cバス1を使用

# グローバル変数
xAccl, yAccl, zAccl = 0, 0, 0

def write_byte(addr, reg, value):
    bus.write_byte_data(addr, reg, value)
    time.sleep(0.1)

def read_bytes(addr, reg, length):
    return bus.read_i2c_block_data(addr, reg, length)

def BMX055_Accl_Init():
    # 加速度センサの初期化
    write_byte(Addr_Accl, 0x0F, 0x03)  # Range = ±2g
    write_byte(Addr_Accl, 0x10, 0x08)  # Bandwidth = 7.81Hz
    write_byte(Addr_Accl, 0x11, 0x00)  # Normal mode

def BMX055_Accl():
    global xAccl, yAccl, zAccl
    data = read_bytes(Addr_Accl, 0x02, 6)
    xAccl = ((data[1] << 8) | (data[0] & 0xF0)) >> 4
    yAccl = ((data[3] << 8) | (data[2] & 0xF0)) >> 4
    zAccl = ((data[5] << 8) | (data[4] & 0xF0)) >> 4
    if xAccl > 2047: xAccl -= 4096
    if yAccl > 2047: yAccl -= 4096
    if zAccl > 2047: zAccl -= 4096
    xAccl, yAccl, zAccl = xAccl * 0.00098, yAccl * 0.00098, zAccl * 0.00098

def record_audio():
    print("Z-axis value is below 0.70. Starting recording...")
    os.system("arecord -D plughw:3,0 -f cd -t wav -d 5 output.wav")
    print("Recording saved to output.wav")

if __name__ == "__main__":
    BMX055_Accl_Init()
    while True:
        BMX055_Accl()
        print(f"Accl= {xAccl:.2f}, {yAccl:.2f}, {zAccl:.2f}")
        
        # Z軸が0.70未満なら録音を開始
        if zAccl < 0.70:
            record_audio()
            sys.exit(0)
        
        print("--------------------------------------")
        time.sleep(1)
