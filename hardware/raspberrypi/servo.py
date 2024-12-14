import RPi.GPIO as GPIO
import time

# GPIO設定
SERVO_PIN = 9  # サーボモーターを接続したGPIOピン
GPIO.setmode(GPIO.BCM)  # GPIO番号の指定方法をBCMに設定
GPIO.setup(SERVO_PIN, GPIO.OUT)  # サーボ用ピンを出力モードに設定

# サーボ制御用PWMの設定
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50HzのPWM信号（サーボ用）
pwm.start(0)  # PWM信号を開始（初期値は0）

def set_angle(angle):
    """
    サーボを指定した角度に動かす関数
    :param angle: サーボの目標角度（0〜180度）
    """
    duty = (angle / 18.0) + 2.5  # 角度をDuty比に変換
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)  # サーボが動くのを待機
    pwm.ChangeDutyCycle(0)  # 信号を停止してサーボのバズ音を防ぐ

try:
    while True:
        # サーボを0度に動かす
        print("Moving to 0 degrees")
        set_angle(60)
        time.sleep(1)

        # サーボを90度に動かす
        print("Moving to 90 degrees")
        set_angle(110)
        time.sleep(1)

        # サーボを180度に動かす
        print("Moving to 180 degrees")
        set_angle(120)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nプログラム終了中...")

finally:
    pwm.stop()  # PWMを停止
    GPIO.cleanup()  # GPIOピンをリセット
