# 🔐 A.S.T.R.I.C.K — AI Desktop Voice Assistant

**Advanced Sentient Technology for Real-time Intelligent Command and Knowledge**

A.S.T.R.I.C.K is a production-style, voice-driven AI desktop assistant that continuously listens for a wake word, understands natural language commands, and performs real system actions in real time.

Built as part of a real-world AI systems series, this project focuses on **practical automation + local AI intelligence**, not just chatbot responses.

---

## 🚀 Key Features

- 🎙️ **Always-on wake word detection** (Porcupine)
- 🧠 **Natural language command routing**
- 💻 **Real system control** (Wi-Fi, Bluetooth, brightness)
- 📂 **Smart app and folder launcher**
- 📺 **Direct YouTube playback** via voice
- 🗑️ **Voice-controlled recycle bin management**
- 📞 **WhatsApp and mobile call automation**
- 📄 **PDF reader** with live voice narration
- 🌦️ **Real-time weather and rain insights**
- 🔐 **Face authentication** before access
- 🌐 **Modern animated web UI** via Eel

---

## 🏗️ System Architecture
```
Hotword Engine (Porcupine)
         ↓
  Speech Recognition
         ↓
    Command Router
         ↓
Action Engine (OS / Web / Mobile)
         ↓
  Voice + Visual Feedback
```

---

## 🧠 Tech Stack

### Backend
- Python 3.12
- Eel (Python ↔ Web bridge)
- SQLite
- PyAutoGUI
- SpeechRecognition
- PyTTSx3
- Porcupine Wake Word
- OpenCV (Face Auth)

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Lottie Animations

---

## 📁 Project Structure
```
ASTRICK/
│
├── engine/
│   ├── auth/
│   ├── command.py
│   ├── features.py
│   ├── helper.py
│   └── cookies.json
│
├── www/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── controller.js
│
├── main.py
├── run.py
└── device.bat
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Adi3182004/ASTRICK.git
cd ASTRICK
```

### 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:
```bash
pip install eel pyttsx3 SpeechRecognition pyaudio pyautogui pvporcupine playsound winshell opencv-python
```

### 4️⃣ Install external tools (IMPORTANT)

You must install:
- ✅ **Tesseract OCR** - [Download here](https://github.com/tesseract-ocr/tesseract)
- ✅ **ADB (Android Debug Bridge)** - [Download here](https://developer.android.com/studio/releases/platform-tools)
- ✅ **Porcupine access key** - [Get key here](https://picovoice.ai/)
- ✅ **Working microphone**
- ✅ **Webcam** for face authentication

Update paths inside `engine/features.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## ▶️ How to Run

Main command:
```bash
python run.py
```

This starts:
- 🔹 Eel web UI
- 🔹 Hotword listener
- 🔹 Face authentication
- 🔹 Voice command engine

---

## 🎤 Example Voice Commands
```
"Open Chrome"
"What time is it"
"Turn on Wi-Fi"
"Set brightness to 60 percent"
"Play lo-fi music on YouTube"
"Restore files from recycle bin"
"Send WhatsApp message to Rahul"
```

---

## 🔐 Security Note

This assistant is designed as a **local-first system**:
- ✅ Runs locally
- ✅ No cloud dependency for core features
- ✅ Face authentication gate
- ✅ Privacy-focused architecture

---

## 🚧 Current Status

⚠️ This is an advanced prototype

### Planned improvements:
- Better NLP intent engine
- Multi-user voice profiles
- Cross-platform support (macOS, Linux)
- Smarter context memory
- Plugin system for extensibility

---

## 🧠 What I Learned

Building A.S.T.R.I.C.K reinforced an important lesson:

> **Real AI becomes powerful only when intelligence is connected to real system actions.**

---

## 👨‍💻 Author

**Aditya Andhalkar**

If you found this project interesting, consider starring ⭐ the repository!

---

## 📜 License

This project is for educational and research purposes.

---

## 🔥 Part of Real-World AI Systems Series

More production-style AI builds coming soon. Stay tuned!
