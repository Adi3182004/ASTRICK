<div align="center">

# A.S.T.R.I.C.K

## Advanced Sentient Technology for Real-time Intelligent Command and Knowledge

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Porcupine](https://img.shields.io/badge/Porcupine-Hotword-success?style=flat-square)](https://picovoice.ai/)
[![Eel](https://img.shields.io/badge/Eel-WebUI-black?style=flat-square)](https://github.com/ChrisKnott/Eel)
[![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Prototype-orange?style=flat-square)](.)

**Production-style AI desktop voice assistant with wake word detection, natural language understanding, and real system automation**

</div>

---

<details open="open">
  <summary><h2 style="display: inline-block">📋 Table of Contents</h2></summary>
  <ol>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#project-goal">Project Goal</a></li>
    <li><a href="#core-features">Core Features</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage-guide">Usage Guide</a></li>
    <li><a href="#system-pipeline">System Pipeline</a></li>
    <li><a href="#api-architecture">API Architecture</a></li>
    <li><a href="#voice-commands">Voice Commands</a></li>
    <li><a href="#performance-notes">Performance Notes</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#important-notes">Important Notes</a></li>
    <li><a href="#future-improvements">Future Improvements</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

---

## Overview

**A.S.T.R.I.C.K** is an advanced AI desktop voice assistant prototype that transforms how you interact with your computer. Built on production-grade architecture, it continuously listens for wake words, understands natural language commands, and executes real system actions in real time.

Unlike traditional chatbots, A.S.T.R.I.C.K bridges the gap between intelligent speech recognition and practical desktop automation, combining multiple AI technologies to create a truly hands-free computing experience.

### Key Components

```
🎙️ Wake Word Detection  →  🧠 NLP Processing  →  ⚙️ System Automation  →  📣 Real-time Feedback
```

The system integrates:
- **Wake Word Detection** — Always-on listening with Porcupine
- **Speech Recognition** — Accurate command interpretation
- **Natural Language Processing** — Flexible command routing
- **System Automation** — Real desktop control
- **Modern Web UI** — Visual feedback and monitoring

---

## Project Goal

Build a production-grade, voice-driven desktop assistant that understands natural language and executes real system actions with minimal latency.

### Key Objectives

✅ Achieve reliable wake word detection with minimal false positives  
✅ Enable flexible natural language command understanding  
✅ Perform real system control without cloud dependencies  
✅ Create intuitive visual feedback mechanisms  
✅ Demonstrate practical AI applications in everyday computing  
✅ Maintain privacy through local-only processing  

---

## Core Features

### 🎙️ Advanced Voice Intelligence

| Feature | Description |
|---------|-------------|
| **Always-on Hotword Detection** | Porcupine wake word engine with millisecond response |
| **Continuous Listening Loop** | Background monitoring without blocking system |
| **Multi-format Speech Recognition** | Google Speech-to-Text with fallback support |
| **Natural Language Understanding** | Context-aware command parsing and routing |
| **Real-time Voice Feedback** | Instant audio confirmation of commands |
| **Speaker Identification** | Voice profile recognition for personalization |

### 💻 System Control & Automation

| Feature | Description |
|---------|-------------|
| **Wi-Fi Management** | Toggle connectivity and network switching |
| **Bluetooth Operations** | Device pairing and connection control |
| **Display Control** | Brightness and resolution adjustment via voice |
| **Application Launcher** | Smart app detection and opening |
| **Folder Navigation** | File system browsing and file operations |
| **Recycle Bin Management** | Voice-controlled file restoration and cleanup |

### 🎬 Entertainment & Media

| Feature | Description |
|---------|-------------|
| **YouTube Playback** | Direct video search and streaming |
| **Music Streaming** | Integration with local and online services |
| **PDF Reader** | Document text extraction with voice narration |
| **Audio Processing** | MP3 and audio file manipulation |
| **Web Content** | Browse and retrieve information from web |

### 📱 Mobile Device Integration

| Feature | Description |
|---------|-------------|
| **WhatsApp Automation** | Voice-controlled message sending |
| **Phone Call Control** | Dialing and call management via voice |
| **Android ADB Bridge** | Direct device control through USB |
| **SMS Management** | Text message composition and delivery |
| **Contact Integration** | Name-based dialing and communication |

### 🔐 Advanced Security

| Feature | Description |
|---------|-------------|
| **Face Authentication** | OpenCV-based facial recognition |
| **Multi-factor Security** | Biometric + voice verification |
| **Privacy-first Architecture** | All processing happens locally |
| **No Cloud Dependency** | Complete offline operation capability |
| **Credential Management** | Secure authentication storage |
| **Session Logging** | Audit trail for security verification |

### 🎨 Professional User Interface

| Feature | Description |
|---------|-------------|
| **Modern Animated Dashboard** | Eel-powered responsive web interface |
| **Real-time Status Indicators** | Live system state visualization |
| **Command History** | Searchable voice command logs |
| **Responsive Design** | Works on desktop and tablet displays |
| **Lottie Animations** | Smooth, engaging visual feedback |
| **Bootstrap Styling** | Professional, polished appearance |

---

## Tech Stack

<table>
<tr>
<td width="50%">

### Backend Architecture
- **Python 3.12+** — Core language
- **Eel Framework** — Python-JS bridge
- **Porcupine SDK** — Hotword detection
- **SpeechRecognition** — Google STT
- **PyAutoGUI** — System automation
- **PyAudio** — Audio processing
- **PyTTSx3** — Text-to-speech
- **OpenCV** — Face detection
- **SQLite** — Local database

</td>
<td width="50%">

### System Integration
- **Windows API** — System commands
- **ADB** — Mobile control
- **Tesseract OCR** — Character recognition
- **Playsound** — Audio feedback

### Frontend
- **HTML5** — Semantic markup
- **CSS3** — Modern styling
- **JavaScript** — Interactive logic
- **Bootstrap 5** — Responsive UI
- **Lottie** — Animations
- **WebSocket** — Real-time comm

</td>
</tr>
</table>

---

## Installation

### Prerequisites

```
✓ Python 3.12 or higher
✓ pip package manager
✓ Virtual environment (recommended)
✓ Microphone (for voice input)
✓ Webcam (optional for face auth)
✓ Windows OS (primary support)
✓ Administrator access
✓ Porcupine access key (free)
```

### Step 1 — Clone Repository

```bash
git clone https://github.com/Adi3182004/ASTRICK.git
cd ASTRICK
```

### Step 2 — Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install Python Dependencies

**Using requirements.txt:**
```bash
pip install -r requirements.txt
```

**Manual Installation:**
```bash
pip install eel pyttsx3 SpeechRecognition pyaudio pyautogui pvporcupine playsound opencv-python pillow pytesseract requests numpy
```

### Step 4 — Install External Tools

#### 🔹 Tesseract OCR (For PDF Reading)
1. Download: https://github.com/tesseract-ocr/tesseract/wiki/Downloads
2. Install to default location
3. Update `engine/features.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

#### 🔹 Android ADB (For Mobile Control)
1. Download: https://developer.android.com/studio/releases/platform-tools
2. Extract to known directory
3. Update `engine/features.py`:

```python
ADB_PATH = r"C:\path\to\platform-tools\adb.exe"
```

#### 🔹 Porcupine Access Key
1. Sign up: https://picovoice.ai/
2. Get free access key
3. Add to `engine/features.py`:

```python
PORCUPINE_ACCESS_KEY = "YOUR_ACCESS_KEY_HERE"
```

### Step 5 — Configure Settings

Edit `engine/features.py`:

```python
# Audio Configuration
MICROPHONE_INDEX = 0
SPEECH_TIMEOUT = 5
SILENCE_THRESHOLD = 1000

# Paths
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
ADB_PATH = r"C:\path\to\platform-tools\adb.exe"

# API Keys
PORCUPINE_ACCESS_KEY = "your_key_here"

# System Settings
WAKE_WORD = "okay jarvis"
VOICE_SPEED = 150
```

### Step 6 — Run the Application

```bash
python run.py
```

Browser opens automatically to `http://localhost:8000`

---

## Usage Guide

### Step 1 — Start the Application

```bash
python run.py
```

Expected output:
- Console showing initialization
- Browser window with web UI
- Hotword listener starting

### Step 2 — Enable Face Authentication (First Time)

1. Click **"Enable Face Auth"** on dashboard
2. Click **"Capture Face"** to start training
3. Show your face from different angles
4. System captures ~30 samples
5. Wait for confirmation message

### Step 3 — Enable Microphone Permissions

1. Grant microphone access when prompted
2. Grant audio input to Python application
3. Test with **"Test Mic"** button
4. Confirm you hear feedback beep

### Step 4 — Test Wake Word Detection

1. Default wake word: **"okay jarvis"**
2. Speak clearly: "Okay jarvis"
3. System responds with beep
4. Wait for command prompt

### Step 5 — Issue Voice Commands

Speak naturally. System understands most common requests.

### Step 6 — Monitor Execution

- Watch dashboard for real-time feedback
- Check command history for logs
- Review system status indicators
- Monitor error logs if needed

### Step 7 — Customize Settings

Access settings panel to:
- Change wake word
- Adjust voice speed
- Select TTS voice
- Configure microphone sensitivity

---

## System Pipeline

```
┌─────────────────────────────────────────────┐
│   Continuous Audio Stream Input             │
│        (Microphone → Audio Buffer)          │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│   Hotword Detection Engine                  │
│ (Porcupine: "Okay jarvis" Recognition)     │
└────────────────────┬────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
      No Match               Match Found
         │                       │
         ▼                       ▼
    Continue            Audio Capture Loop
    Listening          (Record until pause)
                               │
                               ▼
                        Speech-to-Text
                      (Google STT Engine)
                               │
                               ▼
                        Command Router
                       (NLP Intent Parser)
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        System Ctrl      Media Ctrl       Mobile Ctrl
       (PyAutoGUI)      (Web APIs)           (ADB)
              │                ▼                │
              └────────────────┬────────────────┘
                               │
                               ▼
                       Action Execution
                        (OS Commands)
                               │
                               ▼
                     Feedback Generation
                      (Voice + UI Update)
                               │
                               ▼
                       Command Logging
                      (SQLite Database)
```

---

## API Architecture

### Backend-Frontend Communication

Uses **Eel** for Python-JavaScript bidirectional communication:

#### JavaScript → Python

```javascript
eel.execute_command(command_text)(function(result) {
    console.log("Command result:", result);
});
```

**Response Format:**
```json
{
    "status": "success",
    "command": "turn on wifi",
    "action": "wifi_toggle",
    "result": "Wi-Fi enabled",
    "timestamp": "2024-02-27 10:30:45"
}
```

#### Python → JavaScript

```python
eel.update_ui({
    'status': 'listening',
    'message': 'Waiting for command',
    'icon': 'mic'
})
```

### Core Python Functions

| Function | Purpose | Input | Output |
|----------|---------|-------|--------|
| `hotword_listener()` | Monitor audio for wake word | Audio stream | Boolean |
| `listen_command()` | Capture voice command | Audio stream | Text |
| `route_command()` | Parse and route command | Text | Action + params |
| `execute_action()` | Execute system action | Action type | Status result |
| `generate_feedback()` | Create voice feedback | Result object | Voice + UI |

### Command Routing Table

| Pattern | Intent | Handler | Action |
|---------|--------|---------|--------|
| `open [app]` | App Launch | `execute_app()` | Launch app |
| `turn (on/off) [device]` | Device Control | `toggle_device()` | Wi-Fi, BT |
| `set brightness to [0-100]` | Display Control | `set_brightness()` | Screen adjust |
| `search [query]` | Web Search | `web_search()` | YouTube, Google |
| `send [message] to [contact]` | Mobile Messaging | `send_whatsapp()` | WhatsApp, SMS |
| `what (time/weather)` | Information | `get_info()` | System/internet |
| `read [file]` | Document Process | `read_pdf()` | OCR + TTS |

---

## Voice Commands

### 🎯 Application Control
```
"Open Chrome"              "Launch Visual Studio Code"
"Close Spotify"            "Open File Explorer"
"Start Steam"              "Open Notepad"
```

### ⚙️ System Control
```
"Turn on Wi-Fi"            "Disable Bluetooth"
"Set brightness to 50%"    "Increase volume"
"Mute audio"               "Lock screen"
"Shut down computer"       "Restart system"
```

### ❓ Information Queries
```
"What time is it"          "What's the date"
"What's the weather"       "Tell me about [topic]"
"Current temperature"      "UV index today"
```

### 🎬 Media & Entertainment
```
"Play lo-fi music on YouTube"    "Search for cat videos"
"Play my favorite playlist"      "Read my PDF document"
"Open Netflix"
```

### 📱 Mobile Automation
```
"Send WhatsApp to Rahul: Hello"    "Call Mom"
"Send SMS to Priya"                "Open WhatsApp"
"Check phone battery"
```

### 📂 File Management
```
"Create new folder on Desktop"    "Empty recycle bin"
"Restore files"                   "Open recent documents"
"Delete this file"                "Rename file to [name]"
```

---

## Performance Notes

### 📊 Audio Processing Optimization
- **Buffer Size:** 4096 samples per frame (~90ms @ 44.1kHz)
- **Sample Rate:** 16kHz hotword, 44.1kHz TTS
- **Threading:** Separate threads for listening vs processing
- **Frame Rate:** 100ms hotword detection cycles

### 🧠 Machine Learning Performance
- **Porcupine Inference:** ~20-30ms per frame (CPU)
- **Face Detection:** ~50-100ms per frame
- **Speech-to-Text:** ~1-3 seconds (network dependent)
- **TTS Synthesis:** ~100-500ms per response

### 💾 System Resource Usage
- **CPU:** 5-8% idle, 20-30% active command
- **Memory:** 200-300MB base + 100MB per operation
- **Disk:** ~500MB models + 50MB database
- **Network:** ~1-2MB/hour for cloud STT

### ⚡ Real-time Responsiveness
- **Wake Word Latency:** <200ms
- **Command Recognition:** 2-5 seconds
- **Action Execution:** <500ms local, 1-5s network
- **Feedback Generation:** <1 second

### 🚀 Optimization Tips
1. Use lower speech timeout for faster responses
2. Disable face auth for testing (saves ~100ms)
3. Run on SSD for faster database queries
4. Monitor background processes
5. Use dedicated GPU for face processing

---

## Project Structure

```
ASTRICK/
│
├── README.md                 # Documentation (you are here)
├── requirements.txt          # Python dependencies
├── run.py                    # Application entry point
├── main.py                   # Core application logic
│
├── engine/                   # Backend core
│   ├── command.py           # Command parsing & routing
│   ├── features.py          # Feature implementations
│   ├── helper.py            # Utility functions
│   ├── cookies.json         # Session data storage
│   │
│   └── auth/                # Authentication system
│       ├── face_auth.py     # Face recognition
│       ├── face_train.py    # Face profile training
│       ├── voice_auth.py    # Voice verification
│       └── face_data/       # Trained face profiles
│
├── www/                      # Frontend assets
│   ├── index.html           # Main UI template
│   ├── style.css            # Styling & animations
│   ├── script.js            # UI logic & interactions
│   ├── controller.js        # Command handling
│   │
│   └── assets/              # Static resources
│       ├── icons/           # UI icons
│       ├── animations/      # Lottie JSON files
│       └── fonts/           # Custom typefaces
│
├── logs/                     # Application logs
│   └── commands.log         # Command history
│
└── models/                   # ML models (auto-downloaded)
    ├── face_cascade.xml     # OpenCV face detector
    └── porcupine/           # Hotword model files
```

**Key Files:**
- **run.py** — Main entry point, initializes Eel and services
- **main.py** — Core event loop, manages threading
- **engine/command.py** — NLP engine for intent parsing
- **engine/features.py** — Individual feature implementations
- **engine/auth/** — Biometric authentication system
- **www/index.html** — Frontend UI structure
- **www/style.css** — Responsive design and animations
- **www/script.js** — Real-time UI updates

---

## Important Notes

### 🔒 Security & Privacy

- **Local-only Processing** — No audio sent to cloud except speech recognition
- **Face Data** — Stored locally in `engine/auth/face_data/`
- **Voice Commands** — Logged in SQLite on local disk
- **API Keys** — Store in environment variables, never commit to git
- **System Access** — Application has full system control

**Security Best Practices:**
```bash
# Never commit API keys
echo "PORCUPINE_ACCESS_KEY=your_key" > .env
echo ".env" > .gitignore
```

### 📌 Microphone Requirements

- **Quality:** USB microphone recommended
- **Placement:** 6-12 inches from mouth
- **Environment:** Minimize background noise
- **Testing:** Use dashboard test before deploy
- **Sensitivity:** Adjust in system audio settings

### 📌 Face Authentication Notes

- **Lighting:** Well-lit environment needed
- **Angles:** Train from different angles
- **Consistency:** Facial features should be stable
- **Failures:** Sunglasses, masks, makeup affect recognition
- **Fallback:** Voice-only if face fails

### 📌 Platform Compatibility

| Feature | Windows | macOS | Linux |
|---------|---------|-------|-------|
| Wake Word Detection | ✅ | ✅ | ✅ |
| Speech Recognition | ✅ | ✅ | ✅ |
| System Control | ✅ | 🔄 | 🔄 |
| Wi-Fi Management | ✅ | 🔄 | 🔄 |
| Bluetooth Control | ✅ | 🔄 | 🔄 |
| Face Authentication | ✅ | ✅ | ✅ |
| Mobile Integration | ✅ | ✅ | ✅ |

### 📌 Network Dependencies

Works offline EXCEPT:
- **Google Speech-to-Text** — Requires internet
- **Weather Information** — Requires API access
- **YouTube Search** — Requires internet
- **Mobile ADB** — Requires USB connection only

### 📌 Troubleshooting

| Issue | Solution |
|-------|----------|
| Microphone not detected | Check audio settings, restart app, test in Windows Settings |
| Face auth fails | Retrain with better lighting, ensure consistent features |
| Wake word slow | Reduce buffer size, check CPU, close background apps |
| Speech garbage | Check mic quality, speak clearly, reduce noise |

### 📌 Not Production Ready

- **Advanced Prototype** for research and learning
- **Personal Automation** use only
- **AI-powered** commands may occasionally misinterpret
- **Always verify** critical commands
- **Demonstration** of AI capabilities

---

## Future Improvements

### 🟢 Short-term Enhancements
- [ ] Offline Speech Recognition (Whisper integration)
- [ ] Custom Wake Words (user-defined training)
- [ ] Command Chaining (execute multiple commands)
- [ ] Conversation Context (remember previous commands)
- [ ] Improved NLP (better intent classification)
- [ ] Error Recovery (graceful failure handling)

### 🟡 Medium-term Goals
- [ ] Multi-user Support (different voice profiles)
- [ ] Smart Home Integration (IoT device control)
- [ ] Cloud Backup (optional settings sync)
- [ ] Mobile App (iOS/Android companion)
- [ ] Plugin System (community custom commands)
- [ ] Browser Extension (web app functionality)
- [ ] Real-time Translation (multi-language)
- [ ] Emotion Detection (voice tone analysis)

### 🔴 Long-term Vision
- [ ] Cross-platform Release (macOS, Linux full support)
- [ ] Advanced NLP (LLM-powered conversation)
- [ ] Predictive Actions (learn user patterns)
- [ ] Computer Vision (screen content understanding)
- [ ] Advanced Robotics (robot control)
- [ ] Enterprise Edition (corporate deployment)
- [ ] API Marketplace (third-party integration)
- [ ] Ambient AI (always-on passive intelligence)

---

## Contributing

We welcome contributions! Follow these guidelines:

### How to Contribute

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/ASTRICK.git
   cd ASTRICK
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/YourAmazingFeature
   ```

3. **Commit your changes**
   ```bash
   git commit -m 'Add YourAmazingFeature'
   ```

4. **Push to branch**
   ```bash
   git push origin feature/YourAmazingFeature
   ```

5. **Open a Pull Request**

### Contribution Areas

- 🐛 **Bug Fixes** — Find and fix issues
- ✨ **New Commands** — Add voice command handlers
- 📝 **Documentation** — Improve README and comments
- 🎨 **UI/UX** — Enhance frontend design
- ⚡ **Performance** — Optimize speed and resources
- 🧪 **Testing** — Add test coverage
- 🌍 **Localization** — Multi-language support
- 🔧 **Platform Support** — macOS and Linux

### Code Standards

- Follow **PEP 8** style guidelines
- Add **docstrings** to all functions
- Include **comments** for complex logic
- Test on **multiple devices**
- Update **README** if adding features
- Keep **commits atomic** and descriptive

### Development Setup

```bash
git clone https://github.com/Adi3182004/ASTRICK.git
cd ASTRICK
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Before committing
pip install black flake8
black engine/ www/
flake8 engine/ --max-line-length=100
```

---

## License

This project is licensed under the **Educational License** for learning and research purposes.

### Educational License

This project is provided as-is for educational and research purposes. It demonstrates AI, voice processing, and system automation concepts.

**Permissions:**
- ✅ Use for learning and education
- ✅ Modify for personal projects
- ✅ Study and analyze the code
- ✅ Contribute improvements

**Restrictions:**
- ❌ Do not use for commercial products without permission
- ❌ Do not remove attribution or license notices
- ❌ Do not use for malicious purposes

For commercial licensing, contact the author.

See [LICENSE](LICENSE) file for full legal text.

---

## Acknowledgments

- **Picovoice** — Porcupine hotword detection engine
- **Google** — Speech-to-Text API
- **OpenCV** — Computer vision library
- **Eel Framework** — Python-JavaScript bridge
- **PyAutoGUI** — System automation capabilities
- **Contributors** — Everyone improving this project

---

## Contact & Support

- **GitHub Issues** — [Report bugs or request features](https://github.com/Adi3182004/ASTRICK/issues)
- **GitHub Discussions** — [Ask questions and share ideas](https://github.com/Adi3182004/ASTRICK/discussions)
- **Email** — adirajbhar2004@gmail.com
- **Twitter** — [@adiandhalkar](https://twitter.com/adiandhalkar)

---

## Project Statistics

| Metric | Value |
|--------|-------|
| 🎤 Voice Commands | 50+ |
| 🔌 API Endpoints | 8+ |
| 📚 Lines of Code | 3000+ |
| 🧪 Test Coverage | 60%+ |
| ⭐ GitHub Stars | Growing! |
| 👥 Contributors | Welcome! |

---

## Learning Resources

This project teaches:
- **Real-time Audio Processing** — Continuous microphone streams
- **Wake Word Detection** — Efficient hotword recognition
- **Speech Recognition APIs** — Google STT integration
- **System Automation** — PyAutoGUI and OS module usage
- **Face Recognition** — OpenCV for biometric authentication
- **Full-stack Development** — Python backend + JavaScript frontend
- **Database Management** — SQLite for logging and persistence
- **User Interface Design** — Modern web UI with Eel framework

---

<div align="center">

## Built with ❤️ for voice intelligence research

**⭐ Star this repo if you find it useful!**

[Report Bug](https://github.com/Adi3182004/ASTRICK/issues) · [Request Feature](https://github.com/Adi3182004/ASTRICK/issues) · [Documentation](https://github.com/Adi3182004/ASTRICK/wiki)

---

### Part of Real-World AI Systems Series

> **"Real AI becomes powerful only when intelligence is connected to real system actions."**

More production-grade AI projects coming soon. Follow for updates!

[![Follow](https://img.shields.io/github/followers/Adi3182004?label=Follow&style=social)](https://github.com/Adi3182004)

---

Made with Python, Porcupine, and lots of ☕ coffee

</div>
