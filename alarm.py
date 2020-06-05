import time
import playsound

def alarm():
    hh, mm, ss =map(int, input("Enter hh mm ss:").split())

    total_second = hh * 60*60 + mm *60 + ss
    time.sleep(total_second)
    for times in range(2):
       playsound.playsound('analog-watch-alarm_daniel-simion.mp3')


alarm()