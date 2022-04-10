import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("robot: I'm listening")
    audio = robot_ear.record(mic,duration=5)

try :
    you = robot_ear.recognize_google(audio)
except:
    you=""

print(you)

you="Hello"
if you=="":
    robot_brain =" i can't hear you, try again"
elif you == "Hello":
    robot_brain ="Hello Myto"
elif you=="today":
    robot_brain ="thu 3"
elif you=="how are you":  
    robot_brain ="I'm fine, thank you and you?"

print(robot_brain)
import pyttsx3

robot_brain ="I can't hear you, try again"
robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()