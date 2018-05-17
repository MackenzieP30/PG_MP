import win32com.client as winc1
import pyautogui as pg
import webbrowser as wb

speak = winc1.Dispatch("SAPI.SpVoice")

speak.Speak("What's your name?")

answer = pg.prompt("Enter what you are called")

speak.Speak("Hello " + answer + " what's your favorite food?")

food = pg.prompt("Enter whatever you think is tasty")

if food == "Electricty":
    speak.Speak("I love electricity as well. I consume it all every day.")

elif food == "Corn Bread":
        speak.Speak("EW! das nasty!")

else:
    speak.Speak("You like to eat " + food + " . What kind of foreign food is that?")

speak.Speak("What video would you like to watch today?")

video = pg.prompt("Enter you video below.")

speak.Speak("Okie Dokie, Let's look for " + video + " on Youtube and see what we find.")

wb.open("https://www.youtube.com/results?search_query=" + video)
