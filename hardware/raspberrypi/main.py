import sys
import time


from accl_record import record_audio, BMX055_Accl_Init, BMX055_Accl


def main():
    BMX055_Accl_Init()
    while True:
        BMX055_Accl()
        
        # Z軸が0.70未満なら録音を開始
        if zAccl < 0.70:
            record_audio()
            sys.exit(0)
        
        print("--------------------------------------")
        time.sleep(1)


if __name__ == "__main__":
    main()
