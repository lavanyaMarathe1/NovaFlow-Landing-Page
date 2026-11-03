import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Sorry, there is a problem with the speech service.")
            return ""


def main():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = listen()

        if "hello" in command or "hi" in command:
            speak("Hello! Nice to meet you.")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        elif "search" in command:
            query = command.replace("search", "").strip()

            if query:
                speak("Searching for " + query)
                webbrowser.open(
                    "https://www.google.com/search?q=" + query
                )
            else:
                speak("What would you like me to search?")

        elif "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye! Have a nice day.")
            break

        elif command:
            speak("Sorry, I don't know that command yet.")


if __name__ == "__main__":
    main()