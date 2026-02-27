markdown# 🔐 A.S.T.R.I.C.K — AI Desktop Voice Assistant

<div align="center">

**Advanced Sentient Technology for Real-time Intelligent Command and Knowledge**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge)](https://github.com/Adi3182004/ASTRICK)

A production-style, voice-driven AI desktop assistant that continuously listens for a wake word, understands natural language commands, and performs real system actions in real time.

Built as part of a **real-world AI systems series**, this project focuses on **practical automation + local AI intelligence**, not just chatbot responses.

[Features](#-key-features) • [Installation](#️-installation) • [Usage](#️-how-to-run) • [Commands](#-example-voice-commands)

</div>

---

## 🚀 Key Features

<table>
<tr>
<td width="50%">

- 🎙️ **Always-on wake word detection** (Porcupine)
- 🧠 **Natural language command routing**
- 💻 **Real system control** (Wi-Fi, Bluetooth, brightness)
- 📂 **Smart app and folder launcher**
- 📺 **Direct YouTube playback** via voice
- 🗑️ **Voice-controlled recycle bin management**

</td>
<td width="50%">

- 📞 **WhatsApp and mobile call automation**
- 📄 **PDF reader** with live voice narration
- 🌦️ **Real-time weather and rain insights**
- 🔐 **Face authentication** before access
- 🌐 **Modern animated web UI** via Eel
- 🔒 **Privacy-focused local architecture**

</td>
</tr>
</table>

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

<table>
<tr>
<td valign="top" width="50%">

### Backend
- ![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white) Python 3.12
- ![Eel](https://img.shields.io/badge/Eel-Framework-00ADD8) Eel (Python ↔ Web bridge)
- ![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite) SQLite
- PyAutoGUI
- SpeechRecognition
- PyTTSx3
- Porcupine Wake Word
- OpenCV (Face Auth)

</td>
<td valign="top" width="50%">

### Frontend
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) HTML5
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) CSS3
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black) JavaScript
- ![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white) Bootstrap
- Lottie Animations

</td>
</tr>
</table>

---

## 📁 Project Structure
```
ASTRICK/
│
├── 📂 engine/
│   ├── 🔐 auth/
│   ├── 📝 command.py
│   ├── ⚙️ features.py
│   ├── 🛠️ helper.py
│   └── 🍪 cookies.json
│
├── 📂 www/
│   ├── 📄 index.html
│   ├── 🎨 style.css
│   ├── ⚡ script.js
│   └── 🎮 controller.js
│
├── 🚀 main.py
├── ▶️ run.py
└── 🖥️ device.bat
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
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

**Manual Installation (if requirements.txt is missing):**
```bash
pip install eel pyttsx3 SpeechRecognition pyaudio pyautogui pvporcupine playsound winshell opencv-python
```

### 4️⃣ Install external tools ⚠️ IMPORTANT

<table>
<tr>
<th>Tool</th>
<th>Purpose</th>
<th>Download Link</th>
</tr>
<tr>
<td>✅ Tesseract OCR</td>
<td>PDF text extraction</td>
<td><a href="https://github.com/tesseract-ocr/tesseract">Download</a></td>
</tr>
<tr>
<td>✅ ADB</td>
<td>Android device control</td>
<td><a href="https://developer.android.com/studio/releases/platform-tools">Download</a></td>
</tr>
<tr>
<td>✅ Porcupine Key</td>
<td>Wake word detection</td>
<td><a href="https://picovoice.ai/">Get Key</a></td>
</tr>
<tr>
<td>✅ Microphone</td>
<td>Voice input</td>
<td>Hardware required</td>
</tr>
<tr>
<td>✅ Webcam</td>
<td>Face authentication</td>
<td>Hardware required</td>
</tr>
</table>

**Update paths in `engine/features.py`:**
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## ▶️ How to Run
```bash
python run.py
```

**This initializes:**
- 🔹 Eel web UI
- 🔹 Hotword listener
- 🔹 Face authentication
- 🔹 Voice command engine

---

## 🎤 Example Voice Commands
```plaintext
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

<div align="center">

| Feature | Status |
|---------|--------|
| 🏠 Runs Locally | ✅ |
| ☁️ No Cloud Dependency | ✅ |
| 🔐 Face Authentication | ✅ |
| 🛡️ Privacy-Focused | ✅ |

</div>

---

## 🚧 Current Status

> ⚠️ **This is an advanced prototype**

### 📋 Planned Improvements

- [ ] Better NLP intent engine
- [ ] Multi-user voice profiles
- [ ] Cross-platform support (macOS, Linux)
- [ ] Smarter context memory
- [ ] Plugin system for extensibility

---

## 🧠 What I Learned

Building A.S.T.R.I.C.K reinforced an important lesson:

> **"Real AI becomes powerful only when intelligence is connected to real system actions."**

---

## 👨‍💻 Author

<div align="center">

**Aditya Andhalkar**

[![GitHub](https://img.shields.io/badge/GitHub-Adi3182004-181717?style=for-the-badge&logo=github)](https://github.com/Adi3182004)

If you found this project interesting, consider starring ⭐ the repository!

</div>

---

## 📜 License

This project is for **educational and research purposes**.

---

## 🔥 Part of Real-World AI Systems Series

<div align="center">

More production-style AI builds coming soon. **Stay tuned!**

[![Follow](https://img.shields.io/github/followers/Adi3182004?label=Follow&style=social)](https://github.com/Adi3182004)

</div>
