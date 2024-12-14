import sys
import time
import smbus
from accl_record import record_audio, AcclRecord
from analyse_audio import AnalyseAudio
import RPi.GPIO as GPIO
import pygame  # 音声再生用

# サーボ制御用の関数（角度と速度を調整）
def move_servo(pin, angle, speed):
    pwm = GPIO.PWM(pin, 50)  # 50HzのPWM信号
    pwm.start(0)  # 初期化

    # 現在の角度から目標角度までゆっくり動かす
    current_angle = 60
    step = 1 if angle > current_angle else -1  # 角度の進む方向を決定
    for position in range(current_angle, angle + step, step):
        duty_cycle = (position / 180.0) * 10 + 2.5  # 角度をDuty比に変換
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(speed)  # スピードに応じて待機時間を調整

    pwm.stop()

# 音声再生用の関数
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # 再生が終了するまで待機
        time.sleep(0.1)

def main():
    # GPIOの設定
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(9, GPIO.OUT)  # サーボモーターのピン

    # センサーのI2Cアドレス
    SENSOR_1_ADDR_ACCL = 0x19  # 実物センサーの加速度アドレス
    SENSOR_2_ADDR_ACCL = 0x18  # 仮想センサーの加速度アドレス

    # I2Cバスのインスタンス
    bus_sensor_1 = smbus.SMBus(3)  # 実物センサーはバス3
    bus_sensor_2 = smbus.SMBus(1)  # 仮想センサーはバス1

    # センサーの初期化
    accl_record_1 = AcclRecord(bus_sensor_1, SENSOR_1_ADDR_ACCL)
    accl_record_2 = AcclRecord(bus_sensor_2, SENSOR_2_ADDR_ACCL)

    # 録音が完了したかのフラグ
    audio_recorded = False

    # 録音データの解析
    analyser = AnalyseAudio()
    analysis_result = None  # 解析結果を保持する変数

    while True:
        # 1つ目のセンサーからデータ取得
        x1, y1, z1 = accl_record_1.BMX055_Accl()
        print(f"Sensor 1 Accl= {x1:.2f}, {y1:.2f}, {z1:.2f}")

        # 2つ目のセンサーからデータ取得
        x2, y2, z2 = accl_record_2.BMX055_Accl()
        print(f"Sensor 2 Accl= {x2:.2f}, {y2:.2f}, {z2:.2f}")

        # 録音がまだで、z1が0.85未満なら録音を開始
        if not audio_recorded and z1 < 0.85:
            record_audio()
            audio_recorded = True  # 一度録音したのでフラグを立てる
            analysis_result = analyser.analyse('output.wav')
            print(f"Audio Analysis Result: {analysis_result}")

        # z2が0.70未満になったらサーボを動かす
        if audio_recorded and z2 < 0.70:
            if analysis_result is not None:
                intensity = analysis_result.intensity_of_emotion
                # 感情の強度に応じてサーボの角度と速度を調整
                if intensity <= 3:
                    angle =65   # 感情が弱い場合は5度
                    speed = 0.2  # ゆっくり動かす
                elif 4 <= intensity <= 6:
                    angle =85   # 中程度の感情の場合は25度
                    speed = 0.1  # 通常の速度
                else:
                    angle = 110  # 感情が強い場合は50度
                    speed = 0.05  # 早く動かす
                move_servo(9, angle, speed)
                print(f"Servo moved to {angle}° with speed {speed}s per step, based on emotion intensity {intensity}.")
                
                # 音声ファイルを再生
                play_audio("toilet_sound.wav")
            break  # 条件を満たしたらループ終了

        print("--------------------------------------")
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n終了中...")
        GPIO.cleanup()  # GPIOピンのクリーンアップ
