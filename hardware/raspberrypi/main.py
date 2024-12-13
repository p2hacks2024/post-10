import sys
import time

import smbus


from accl_record import record_audio, AcclRecord
from analyse_audio import AnalyseAudio


def main():
    # センサーのI2Cアドレス
    SENSOR_1_ADDR_ACCL = 0x19  # 実物センサーの加速度アドレス
    SENSOR_2_ADDR_ACCL = 0x18  # 仮想センサーの加速度アドレス

    # I2Cバスのインスタンス
    bus_sensor_1 = smbus.SMBus(1)  # 実物センサーはバス1
    bus_sensor_2 = smbus.SMBus(3)  # 仮想センサーはバス3

    # センサーの初期化
    accl_record_1 = AcclRecord(bus_sensor_1, SENSOR_1_ADDR_ACCL)
    accl_record_2 = AcclRecord(bus_sensor_2, SENSOR_2_ADDR_ACCL)

    # 録音データの解析
    analyser = AnalyseAudio()

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
            print(analyser.analyse('output.wav'))
            sys.exit(0)

        print("--------------------------------------")
        time.sleep(1)

if __name__ == "__main__":
    main()
