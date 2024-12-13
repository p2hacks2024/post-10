import smbus
import time
import os
import sys
import RPi.GPIO as GPIO
from time import sleep

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

def move_servo(pwm_servo):
    # サーボの動作（PWM制御で90°動かす）
    print("Z2 is below 0.70. Moving servo on GPIO 9...")

    # 90度に設定するためのDuty Cycle
    pwm_servo.ChangeDutyCycle(7)  # Duty Cycle 7%でサーボを90度に動かす
    time.sleep(1)  # 1秒間待機（サーボが動く時間）
    
    # サーボを戻す（-90度に戻す）
    pwm_servo.ChangeDutyCycle(5)  # Duty Cycle 5%でサーボを戻す
    time.sleep(1)  # 1秒間待機

    # 再度90度に動かす
    pwm_servo.ChangeDutyCycle(7)  # 90度に設定
    time.sleep(1)
    
    # サーボを戻す
    pwm_servo.ChangeDutyCycle(5)  # 戻す
    time.sleep(1)

if __name__ == "__main__":
    # GPIOの設定
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(9, GPIO.OUT)

    # PWM設定
    pwm_servo = GPIO.PWM(9, 50)  # PWM周波数50Hz
    pwm_servo.start(0)  # 初期Duty Cycleは0%

    # センサーのI2Cアドレス
    SENSOR_1_ADDR_ACCL = 0x19  # 実物センサーの加速度アドレス
    SENSOR_2_ADDR_ACCL = 0x18  # 仮想センサーの加速度アドレス

    # I2Cバスのインスタンス
    bus_sensor_1 = smbus.SMBus(3)  # 実物センサーはバス3
    bus_sensor_2 = smbus.SMBus(1)  # 仮想センサーはバス1

    accl_record_1 = AcclRecord(bus_sensor_1, SENSOR_1_ADDR_ACCL)
    accl_record_2 = AcclRecord(bus_sensor_2, SENSOR_2_ADDR_ACCL)

    # 録音が完了したかのフラグ
    audio_recorded = False

    while True:
        # 1つ目のセンサーからデータ取得
        x1, y1, z1 = accl_record_1.BMX055_Accl()
        print(f"Sensor 1 Accl= {x1:.2f}, {y1:.2f}, {z1:.2f}")

        # 2つ目のセンサーからデータ取得
        x2, y2, z2 = accl_record_2.BMX055_Accl()
        print(f"Sensor 2 Accl= {x2:.2f}, {y2:.2f}, {z2:.2f}")

        # 録音がまだで、z1が0.70未満なら録音を開始
        if not audio_recorded and z1 < 0.70:
            record_audio()
            audio_recorded = True  # 一度録音したのでフラグを立てる

        # z2が0.70未満になったらサーボを動かす
        if z2 < 0.70:
            move_servo(pwm_servo)

        print("--------------------------------------")
        time.sleep(1)

    pwm_servo.stop()  # 最後にPWMを停止
    GPIO.cleanup()  # GPIOのクリーンアップ
