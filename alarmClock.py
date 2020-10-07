import datetime
import time


def alarm(set_alarm_time, set_alarm_date):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        if now == set_alarm_time and date == set_alarm_date:
            print("Time to Wake up")
        # SOUND should be here
        break


def actual_time():
    set_alarm_time = input("Set alarm time in hour:min format:")
    set_alarm_date = input("Set alarm datw in day/month/year format:")
    alarm(set_alarm_time, set_alarm_date)


if __name__ == '__main__':
    pass
