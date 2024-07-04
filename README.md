# Python Voice Assistant

This Python script implements a voice assistant similar to Alexa, capable of performing tasks like fetching weather information, setting reminders, and playing music from YouTube.

## Features

- **Speech Recognition**: Converts spoken commands into text using the `speech_recognition` library.
- **Text-to-Speech**: Converts text responses into spoken words using the `pyttsx3` library.
- **Weather Information**: Retrieves current weather details for any city using the OpenWeatherMap API.
- **Reminders**: Sets reminders for tasks that alert after a specified duration.
- **Music Player**: Searches and plays music from YouTube based on user commands.

## Setup

1. **Installation**

   - Clone the repository:
     ```bash
     git clone https://github.com/Amlakie-T/Python-Voice-Assistant.git
     cd Python-Voice-Assistant
     ```

   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **API Keys**

   - Sign up at [OpenWeatherMap](https://openweathermap.org/) to get an API key.
   - Replace `YOUR_OPENWEATHER_API_KEY` in `voice_assistant.py` with your actual API key.

3. **Usage**

   - Run the script:
     ```bash
     python voice_assistant.py
     ```

   - Start the voice assistant and speak commands like:
     - "What's the weather in London?"
     - "Remind me to call John in 30 minutes."
     - "Play music Despacito."

4. **Author**

   - Developed by [Your Name](https://github.com/Amlakie-T)

---

This project is a Python voice assistant developed to handle various tasks through voice commands. Feel free to explore and contribute!
