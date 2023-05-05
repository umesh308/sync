

import datetime
from tkinter import * 
from playsound import playsound

print("FOR SET THE ALARM CLOCK ")

alarmHour = int(input("Enter Hour for alarm: "))

alarmMin = int(input("Enter Minutes for alarm: "))

now = datetime.datetime.now().hour

while True:

  if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:

     print("Playing..")
    

     
     playsound('C:\\Users\\Asus\Desktop\\syntrc\\tasks\\Alarm Alarm Alarm.mp3') 

     break
  elif now>alarmHour:
     
     print('''You entered the 'WRONG' time 
              Please enter RIGHT time 
              ==>TIME IS EQUAL TO OR  GREATER THAN CURRENT TIME2
              ''')
     break


