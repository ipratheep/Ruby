import getpass
import pyjokes
import pyttsx3
import subprocess
import speech_recognition as sr
import pywhatkit
import phonenumbers
from phonenumber import location
import webbrowser
from track_img import img_meta


def code_red():
    user = getpass.getuser()
    path = "/home/"+user+"/tmp/test"
    subprocess.call(['rm', '-r', path])


def track():
    speak("please enter phone number sir")
    if location() == "empty":
        speak("api key is missing")
    else:
        webbrowser.open("file:///home/" + getpass.getuser() + "/Ruby/location.html")


def image_track():
    # img_meta()
    if img_meta() == "empty":
        speak("unable to track this image")
    else:
        speak("tracking gps coordinates start")
        webbrowser.open("file:///home/"+getpass.getuser()+"/Ruby/img_location.html")


def speak(text):
    engine = pyttsx3.init()
    voice = engine.getProperty("voices")
    engine.setProperty('voice', 'english+f4')
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


def r():
    try:
        t = sr.Recognizer()
        with sr.Microphone() as source:
            print("I am Listening . . . . . .")
            audio = t.listen(source, phrase_time_limit=5)
            text = t.recognize_google(audio, language='en-in')
            text = text.lower()
            return text

    except Exception as e:
        print(e)
        text = "say something"
        return text


def run_ruby():
    text = r()
    if "ruby" in text:
        text = text.replace("ruby", "")
        speak(text)
    elif "say" in text:
        print("I am Listening . . . . . .")
    elif "song" in text:
        pywhatkit.playonyt(text)
    elif "code red" in text:
        code_red()
        speak("file deleted successfully")
    elif "joke" in text:
        joke = pyjokes.get_joke()
        speak(joke)
    elif "pass" in text:
        pywhatkit.sendwhatmsg("(Enter phone number)", "(Enter message)", 18, 30)
        speak("meassage sent succesfully")
    elif "track" in text:
        speak("tracking")
        track()
    elif "image" in text:
        speak("enter the path to image")
        image_track()


while True:
    run_ruby()

