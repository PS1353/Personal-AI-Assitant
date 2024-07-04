import speech_recognition as sr
import pyttsx3 #Text to speech converter library
import os
import webbrowser
import datetime
from geminitest import api_key
import google.generativeai as genai

# Parameters for the model
parameters = {
    "max_output_tokens": 250,      # Limit the response length
    "temperature": 0,    # Make the response more deterministic
    "top_p": 0.9,          # Control the diversity of the response
}

def say(text):
    engine = pyttsx3.init(driverName= "sapi5")
    print(f"Assitant : {text}")
    engine.say(text) 
    engine.runAndWait()

def takeCommand(): 

    r = sr.Recognizer()	
    print("Listening..")
    
    with sr.Microphone() as source:	
        
        r.energy_threshold = 3000
        #r.pause_threshold = 1 
        r.adjust_for_ambient_noise(source, duration=0.2)
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio).lower()
            print(f"User said : {query}")
            return query
        
        except Exception as e:
             say("Sorry some error occurred. Please Try again")          

def greeting():
    say("Hello I am your Personal Assistant")

def open(query):
    site = query.split()[-1]
    siteUrl = f"https://www.{site}.com"
    say(f"Opening {site}")
    webbrowser.open(siteUrl)

def close(query):
    site = query.split()[-1]
    siteUrl = f"https://www.{site}.com"
    os.system("taskkill /im opera.exe /f")
    return say(f"Closing {site}")

def time():
    time = datetime.datetime.now().strftime("%H %M %S")
    say(f"The time is {time}")

def gemini(prompt,parameters):
    input_to_ai = prompt + "concisely"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
                                model_name='gemini-1.5-flash',
                                generation_config= parameters)
    response = model.generate_content(input_to_ai)
    return say(response.text)
 
greeting()

while True:
    userCommand = takeCommand()
    if userCommand == None:
       continue
    elif "exit" in userCommand:
        say("Exiting")
        exit()
    elif "open" in userCommand:
        open(userCommand)
        #exit()
    elif "the time" in userCommand:
        time()
        #exit()
    elif "close" in userCommand:
        close(userCommand)
        #exit()
    else:    
        gemini(prompt=userCommand,parameters=parameters)