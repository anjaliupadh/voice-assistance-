import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you repeat?")
            return listen()
        except sr.RequestError:
            speak("Sorry, I'm having trouble accessing the Google API. Please try again later.")
            return None

def assistant():
    speak("Hello! How can I assist you today?")
    while True:
        query = listen()

        if query is None:
            continue

        if "hello" in query:
            speak("Hello there!")

        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today is {current_date}")

        elif "search" in query:
            speak("What would you like me to search for?")
            search_query = listen()
            if search_query:
                search_url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(search_url)
                speak("Here are the search results.")

        elif "exit" in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    assistant()


