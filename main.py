import pyttsx3
import speech_recognition as sr
import datetime, webbrowser
import random
import requests
from groq import Groq
from config import OPENWEATHER_API_KEY,GROQ_API_KEY

# ─── Configuration ────────────────────────────────────────────────────────────
WAKE_WORD    = "nova"           

groq_client = Groq(api_key=GROQ_API_KEY)


WAKE_RESPONSES = [
    "Ya?",
    "Yes!",
    "I'm here!",
    "How can I help you?"
]

SPECIAL_SITES = {
    "google"    : "https://www.google.com",
    "gmail"     : "https://mail.google.com",
    "youtube"   : "https://www.youtube.com",
    "github"    : "https://www.github.com",
    "instagram" : "https://www.instagram.com",
    "whatsapp"  : "https://web.whatsapp.com",
    "facebook"  : "https://www.facebook.com",
    "twitter"   : "https://www.twitter.com",
    "netflix"   : "https://www.netflix.com",
}

# ─── Speak ────────────────────────────────────────────────────────────────────
def speak(text):
    print(f"nova: {text}")
    e = pyttsx3.init()
    e.say(text)
    e.runAndWait()
    e.stop()

# ─── Listen ───────────────────────────────────────────────────────────────────
def listen(timeout=8, phrase_limit=6):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
        except sr.WaitTimeoutError:
            return ""
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower().strip()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Network error. Please check your connection.")
        return ""

# ─── Weather ──────────────────────────────────────────────────────────────────
def get_weather(city):
    try:
        url = (f"https://api.openweathermap.org/data/2.5/weather"
               f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric")
        data = requests.get(url).json()

        if data["cod"] == 200:
            temp        = data["main"]["temp"]
            feels_like  = data["main"]["feels_like"]
            humidity    = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            city_name   = data["name"]
            return (f"Weather in {city_name}: {description}, "
                    f"temperature is {temp} degrees Celsius, "
                    f"feels like {feels_like} degrees, "
                    f"humidity is {humidity} percent.")
        else:
            return "City not found. Please try again."
    except Exception:
        return "Sorry, I couldn't fetch the weather right now."
    
#------------------------------------Groq AI------------------------------------
def ask_ai(command):
    """Send command to Groq AI and get a smart response."""
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",  # fast & free
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful voice assistant named Google. "
                        "Give short, spoken-friendly answers (1-3 sentences max). "
                        "No markdown, no bullet points, just plain speech."
                    )
                },
                {"role": "user", "content": command}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return "Sorry, I couldn't reach the AI right now."

# ─── Commands ─────────────────────────────────────────────────────────────────
def handle_command(command):

    # Time
    if "time" in command:
        t = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {t}")

    # Date
    elif "date" in command:
        d = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {d}")

    # Weather
    elif "weather" in command:
        city = command.replace("weather in", "").replace("weather", "").strip()
        if city:
            speak(f"Fetching weather for {city}, please wait.")
            speak(get_weather(city))
        else:
            speak("Please tell me the city name. For example, say weather in Mumbai.")

    # Open website
    elif "open" in command:
        site = command.replace("open", "").strip()
        url  = SPECIAL_SITES.get(site, f"https://www.{site}.com")
        webbrowser.open(url)
        speak(f"Opening {site}")

    # Search
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")
        else:
            speak("What should I search for?")

    # Exit
    elif "exit" in command or "quit" in command or "bye" in command:
        speak("Goodbye! Have a great day.")
        exit()

    # 🤖 AI handles anything else!
    else:
        speak(ask_ai(command))

# ─── Main loop ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    speak(f"initializing Nova... Say '{WAKE_WORD}' to wake me up.")

    while True:
        print("Waiting for wake word...")
        wake = listen(timeout=5, phrase_limit=4)

        if WAKE_WORD in wake:
            response = random.choice(WAKE_RESPONSES)
            speak(response)
            print("Listening for command...")

            cmd = listen(timeout=7, phrase_limit=8)
            if cmd:
                handle_command(cmd)
            else:
                speak("I didn't hear anything. Going back to sleep.")
        print()