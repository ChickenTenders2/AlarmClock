from playsound import playsound #pip3 install wheel, then pip3 install playsound 
import time

CLEAR = "\033[2J" #print(CLEAR) to clear terminal when it's ran
CLEAR_AND_RETURN = "\033[H" #print(CLEAR_AND_RETURN) to replace 00:05 with 00:04

def alarm(seconds):
    time_elasped = 0

    print(CLEAR)
    while time_elasped < seconds: #if its not the alarm's time yet
        time.sleep(1) #wait 1 second
        time_elasped += 1 #how much time its been since the timer started

        time_left = seconds - time_elasped
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}") #02d: display minutes and seconds with 2 digits each (eg. 9 becomes 09)

    playsound("mitsuha's alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)