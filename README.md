# Nova AI Voice Assistant 🎙️🤖
A smart, voice-activated AI assistant built with Python that listens for a wake word and responds to your commands — from checking the weather to answering anything with the power of Groq AI!

## 🔊 How It Works
- Say **"Nova"** to wake the assistant up
- Nova responds and listens for your command
- Give a command like **"What's the time?"**, **"Open YouTube"**, or **"Search Python tutorials"**
- For anything else, Nova uses **Groq AI (LLaMA 3)** to give you a smart spoken answer!

## 📋 Features
- Wake word detection — always listening for **"Nova"**
- Real-time **speech recognition** via Google Speech API
- **Text-to-speech** responses using pyttsx3
- **Live weather updates** for any city (OpenWeatherMap API)
- Opens popular websites instantly (YouTube, Gmail, GitHub, Instagram & more)
- Google search directly by voice
- **AI-powered answers** for anything else via Groq (LLaMA 3.1)
- Friendly random wake responses for a natural feel

## 🚀 How to Run

1. Clone the repository
```bash
git clone https://github.com/ayush-raj-prakash/nova-ai-voice-assistant.git
```

2. Navigate into the project folder
```bash
cd nova-ai-voice-assistant
```

3. Install the required libraries
```bash
pip install pyttsx3 SpeechRecognition requests groq
```

4. Add your API keys in `config.py`
```python
OPENWEATHER_API_KEY = "your_openweather_api_key"
GROQ_API_KEY        = "your_groq_api_key"
```

5. Run the assistant
```bash
python main.py
```

> 🎤 Make sure your microphone is connected and working!

## 📁 Project Structure
nova-ai-voice-assistant/ <br>
│ <br>
├── main.py        # Core assistant logic <br>
└── config.py      # API keys configuration <br>

## 🛠️ Technologies Used
- Python 3.x
- `pyttsx3` — Text-to-speech engine
- `SpeechRecognition` — Voice input via Google Speech API
- `requests` — HTTP calls for weather data
- `groq` — Groq AI client (LLaMA 3.1 8B model)
- `webbrowser` — Opens URLs in the browser
- `datetime` & `random` — Built-in Python modules

## 🌐 Supported Voice Commands

| Command | Example |
|---|---|
| Time | *"What's the time?"* |
| Date | *"What's today's date?"* |
| Weather | *"Weather in Mumbai"* |
| Open site | *"Open YouTube"* |
| Search | *"Search Python tutorials"* |
| Exit | *"Bye"* / *"Quit"* / *"Exit"* |
| Anything else | *"Who invented the internet?"* |

## 📌 Future Improvements
- [ ] Add memory — remember user preferences across sessions
- [ ] Support for music playback commands
- [ ] Add a GUI dashboard with real-time voice waveform
- [ ] Multi-language support for voice recognition
- [ ] Custom wake word training instead of keyword matching
- [ ] Add news headlines and reminders feature

## 👨‍💻 Developer
**Ayush Raj Prakash**
GitHub: [@ayush-raj-prakash](https://github.com/ayush-raj-prakash)
