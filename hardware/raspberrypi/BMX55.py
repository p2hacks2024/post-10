import smbus
import time

# I2Cアドレス設定
BMX055_ACCEL_ADDR = 0x18
BMX055_GYRO_ADDR = 0x68
BMX055_MAG_ADDR = 0x10

# レジスタ設定
ACCEL_X_LSB = 0x02
GYRO_X_LSB = 0x02
MAG_X_LSB = 0x42

# I2Cバス番号
I2C_BUS = 1

# I2Cインスタンス
bus = smbus.SMBus(I2C_BUS)

# 初期化関数
def initialize_bmx055():
    # 加速度センサー初期化
    bus.write_byte_data(BMX055_ACCEL_ADDR, 0x0F, 0x03)  # Range = ±2g
    bus.write_byte_data(BMX055_ACCEL_ADDR, 0x10, 0x08)  # Bandwidth = 7.81 Hz
    bus.write_byte_data(BMX055_ACCEL_ADDR, 0x11, 0x00)  # Normal mode, sleep duration = 0.5ms

    # ジャイロスコープ初期化
    bus.write_byte_data(BMX055_GYRO_ADDR, 0x0F, 0x04)  # Range = ±125°/s
    bus.write_byte_data(BMX055_GYRO_ADDR, 0x10, 0x07)  # Bandwidth = 32 Hz
    bus.write_byte_data(BMX055_GYRO_ADDR, 0x11, 0x00)  # Normal mode, sleep duration = 2ms

    # 地磁気センサー初期化
    bus.write_byte_data(BMX055_MAG_ADDR, 0x4B, 0x83)  # Soft reset
    time.sleep(0.1)
    bus.write_byte_data(BMX055_MAG_ADDR, 0x4B, 0x01)  # Normal mode
    bus.write_byte_data(BMX055_MAG_ADDR, 0x4C, 0x00)  # Data rate = 10Hz
    bus.write_byte_data(BMX055_MAG_ADDR, 0x4E, 0x84)  # X/Y axes powered
    bus.write_byte_data(BMX055_MAG_ADDR, 0x51, 0x04)  # Z axis powered
    bus.write_byte_data(BMX055_MAG_ADDR, 0x52, 0x16)  # Regular preset

# データ取得関数
def read_sensor_data(addr, lsb_reg):
    data = bus.read_i2c_block_data(addr, lsb_reg, 6)  # 6バイト読み取り
    x = (data[1] << 8) | data[0]
    y = (data[3] << 8) | data[2]
    z = (data[5] << 8) | data[4]

    # 2の補数を処理
    if x & 0x8000:
        x -= 1 << 16
    if y & 0x8000:
        y -= 1 << 16
    if z & 0x8000:
        z -= 1 << 16

    return x, y, z

# メイン処理
def main():
    initialize_bmx055()

    while True:
        # 加速度データ取得
        accel_x, accel_y, accel_z = read_sensor_data(BMX055_ACCEL_ADDR, ACCEL_X_LSB)
        print(f"Accelerometer: X={accel_x}, Y={accel_y}, Z={accel_z}")

        # ジャイロデータ取得
        gyro_x, gyro_y, gyro_z = read_sensor_data(BMX055_GYRO_ADDR, GYRO_X_LSB)
        print(f"Gyroscope: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")

        # 地磁気データ取得
        mag_x, mag_y, mag_z = read_sensor_data(BMX055_MAG_ADDR, MAG_X_LSB)
        print(f"Magnetometer: X={mag_x}, Y={mag_y}, Z={mag_z}")

        print("-" * 50)
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n終了中...")
