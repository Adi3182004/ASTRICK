import os
import time

DEVICE = "192.168.1.8:5555"


def run_adb(cmd):
    full = f'adb -s {DEVICE} {cmd}'
    os.system(full)
    time.sleep(1)


def type_number_slow(number):
    number = str(number)
    for d in number:
        run_adb(f'shell input text {d}')
        time.sleep(0.25)


def type_message_slow(message):
    message = message.replace(" ", "%s")
    run_adb(f'shell input text "{message}"')


def send_sms(phone_number, message):
    run_adb('shell monkey -p com.transsion.smartmessage -c android.intent.category.LAUNCHER 1')
    time.sleep(2)

    run_adb('shell input tap 927 2170')
    time.sleep(2)

    type_number_slow(phone_number)
    time.sleep(2)

    run_adb('shell input tap 441 1453')
    time.sleep(1)

    type_message_slow(message)
    time.sleep(1)

    run_adb('shell input tap 960 1453')