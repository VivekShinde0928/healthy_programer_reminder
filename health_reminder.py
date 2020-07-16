# ***Healthy Programer***
import time
from pygame import mixer
from time import strftime

def water():
    while True:
        mixer.init()
        mixer.music.load("C:\\Users\HAPL\Desktop\project_MP3\Water.mp3")
        mixer.music.play(1000000)
        x=input("Enter 'Done'  to stop the alarm :")
        if x.lower()=='done':
            mixer.music.stop()
            break

def eyes():
    while True:
        mixer.init()
        mixer.music.load("C:\\Users\HAPL\Desktop\project_MP3\Eyes.mp3")
        mixer.music.play(10000000)
        x=input("Enter 'done'  to stop the alarm :")
        if x.lower()=='done':
            mixer.music.stop()
            break

def Activity():
    while True:
        mixer.init()
        mixer.music.load("C:\\Users\HAPL\Desktop\project_MP3\Activity.mp3")
        mixer.music.play(10000000)
        x=input("Enter 'done'  to stop the alarm :")
        if x.lower()=='done':
            mixer.music.stop()
            break

def log(msg):
    t = time.asctime()
    with open("my_logs.txt","a") as f:
        f.write(msg + " : " + t +'\n')

if __name__ == '__main__':
            print("\n***Healthy Programer***\n")
            office_strt_stop = strftime("%H:%M:%S")
            # print(office_strt_stop)
            initial_water_time=time.time() ##time.time() calculates current time in seconds
            initial_eye_time=time.time()
            initial_activity_time = time.time()
            water_sec=20
            eyes_sec=10
            activity_sec=30
            while office_strt_stop>'09:23:00' and office_strt_stop<'17:00:00':
                if time.time() - initial_water_time > water_sec:
                    print("\nTime to drink water")
                    water()
                    initial_water_time=time.time()
                    log("Water Checked")
                    office_strt_stop = time.strftime("%H:%M:%S")

                if time.time() - initial_eye_time > eyes_sec:
                    print("\nTime for eyes exercise")
                    eyes()
                    initial_eye_time = time.time()
                    log("Eyes Checked")
                    office_strt_stop = time.strftime("%H:%M:%S")

                if time.time() - initial_activity_time > activity_sec:
                    print("\nTime for some physical activity")
                    Activity()
                    initial_activity_time = time.time()
                    log("Activity checked")
                    office_strt_stop = time.strftime("%H:%M:%S")


















