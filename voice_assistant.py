import speech_recognition as sr
import pyttsx3
import requests
import datetime
import webbrowser
import os
import time

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Could not request results from Google Speech Recognition service.")
            return ""

# Function to get the weather
def get_weather(city):
    api_key = 'YOUR_OPENWEATHER_API_KEY'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        description = weather["description"]
        weather_report = f"The temperature in {city} is {temperature}°C with {description}."
        speak(weather_report)
    else:
        speak("City not found.")

# Function to set a reminder
def set_reminder(task, time_in_minutes):
    speak(f"Setting a reminder for {task} in {time_in_minutes} minutes.")
    time.sleep(time_in_minutes * 60)
    speak(f"Reminder: {task}")

# Function to play music on YouTube
def play_music(song):
    speak(f"Playing {song} on YouTube.")
    query = song.replace(' ', '+')
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    # Optionally, use a web scraping library to click the first video link

# Main loop to continuously listen for commands
if __name__ == "__main__":
    while True:
        command = listen()

        if 'weather' in command:
            speak("Which city?")
            city = listen()
            get_weather(city)

        elif 'remind me to' in command:
            task = command.replace('remind me to', '').strip()
            speak("In how many minutes?")
            time_in_minutes = int(listen())
            set_reminder(task, time_in_minutes)

        elif 'play music' in command:
            song = command.replace('play music', '').strip()
            play_music(song)

        elif 'stop listening' in command or 'goodbye' in command:
            speak("Goodbye!")
            break

        else:
            speak("I can help with weather, reminders, and playing music. What else can I do for you?")
