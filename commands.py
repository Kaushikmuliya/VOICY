import os
import datetime
from speak import speak_text
from music import play_music_by_language

def execute_command(command):
    if "open brave" in command:
        speak_text("Opening brave")
        os.system("start brave")

    elif "play music" in command:
        play_music_by_language()
    
    elif "What is time" in command or "tell me the time" in command or "time" in command:
        now=datetime.datetime.now().strftime("%I:%M %p")  #formats time to speak
        speak_text(f"The time is {now}")
    
    elif "shutdown" in command:
        speak_text("Shutting down")
        os.system("shutdown /s /t 30")

    else:
        speak_text("Command not recognized.")
    
