import RPi.GPIO as GPIO
import time
import os

# GPIOモードの設定
GPIO.setmode(GPIO.BCM)

# センサー1のGPIOピン
TRIG1 = 23
ECHO1 = 24

# センサー2のGPIOピン
TRIG2 = 17
ECHO2 = 27

# サーボモーターのGPIOピン
SERVO_PIN = 9

# GPIOピンの設定
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# サーボモーターのPWM設定
servo = GPIO.PWM(SERVO_PIN, 50)  # PWM周波数を50Hzに設定
servo.start(0)  # 初期位置を設定（0度）

# 録音が完了したかどうかを追跡するフラグ
recorded = False

def measure_distance(trig, echo):
    # トリガーをLOWにして安定化
    GPIO.output(trig, False)
    time.sleep(0.2)

    # トリガーをHIGHにしてパルスを送信
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    # Echo信号の開始時間と終了時間を記録
    while GPIO.input(echo) == 0:
        start_time = time.time()

    while GPIO.input(echo) == 1:
        stop_time = time.time()

    # 音波の往復時間を計算
    elapsed_time = stop_time - start_time

    # 距離を計算（音速343m/s）
    distance = (elapsed_time * 34300) / 2

    return distance

def record_audio():
    print("センサー1の距離が20cm以上になりました。録音を開始します...")
    os.system("arecord -D plughw:3,0 -f cd -t wav -d 5 output.wav")
    print("録音が完了しました。output.wav に保存されました。")

def move_servo(angle):
    """指定した角度にサーボモーターを動かす"""
    duty = 2.5 + (angle / 18)  # 角度からデューティサイクルを計算
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)  # モーターが動く時間を確保
    servo.ChangeDutyCycle(0)  # 信号を切って振動を防止

try:
    while True:
        # センサー1の距離を測定
        distance1 = measure_distance(TRIG1, ECHO1)
        print(f"センサー1の距離: {distance1:.2f} cm")

        # 距離が20cm以上の場合に録音開始（録音がまだ実行されていない場合のみ）
        if not recorded and distance1 >= 20.0:
            record_audio()
            recorded = True  # 録音済みフラグを設定

        # 録音が終わった後でセンサー2の処理を開始
        if recorded:
            # センサー2の距離を測定
            distance2 = measure_distance(TRIG2, ECHO2)
            print(f"センサー2の距離: {distance2:.2f} cm")

            # センサー2の距離が20cm以上の場合にサーボを動かす
            if distance2 >= 20.0:
                print("センサー2の距離が20cm以上になりました。サーボを動かします...")
                move_servo(60)  # サーボを60度に動かす
                time.sleep(1)  # 少し待機
                move_servo(110)  # サーボを110度に動かす

        # 短い待機を追加（必要に応じて調整可能）
        time.sleep(1)

except KeyboardInterrupt:
    print("プログラムを終了します")

finally:
    servo.stop()  # サーボモーターのPWMを停止
    GPIO.cleanup()
