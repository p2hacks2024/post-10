#include <Servo.h>

int sensorPin = 2;  // 人感センサの出力ピンをデジタルピン2に接続
int sensorValue = 0;
Servo myServo;  // サーボオブジェクト

void setup() {
  pinMode(sensorPin, INPUT);  // センサを入力モードに設定
  myServo.attach(9);  // サーボモーターをピン9に接続
  Serial.begin(9600);  // シリアルモニタの初期化
}

void loop() {
  sensorValue = digitalRead(sensorPin);  // センサの状態を読み取る
  if (sensorValue == HIGH) {
    Serial.println("人を検出しました！");
    myServo.write(90);  // サーボを90度回転
  } else {
    Serial.println("人を検出していません");
    //myServo.write(0);  // サーボを0度に戻す
  }
  delay(500);  // 0.5秒ごとにチェック
}
