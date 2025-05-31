from listen import listen_command
from commands import execute_command
import time
from speak import speak_text


def main():
    speak_text("Hello bro! How can i help you today?")
    while True:
        print("What's Up Brother..")
        
        command=listen_command()

        if command:
            if "exit" in command or "quit" in command or "stop" in command or "please stop " in command:
                print(f"You said: {command}")
                speak_text("See you soon bro!")
                break
            else :
                print(f"You said: {command}")
                execute_command(command.lower())


        time.sleep(1)
if __name__=="__main__":
    main()