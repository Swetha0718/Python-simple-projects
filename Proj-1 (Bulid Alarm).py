import datetime
from playsound import playsound

alarm_h = int(input("Enter hours: "))
alarm_m = int(input("Enter minutes: "))
am = input("AM/PM: ")
am = "am"  # Correcting the assignment

if am.lower() == "am":
    alarm_h %= 12
else:
    alarm_h += 12

while True:
    current_time_minutes = datetime.datetime.now().hour * 60 + datetime.datetime.now().minute
    alarm_time_minutes = alarm_h * 60 + alarm_m

    if current_time_minutes >= alarm_time_minutes:
        print("Wake up")
        playsound("alarm_s.mp3")
        break
