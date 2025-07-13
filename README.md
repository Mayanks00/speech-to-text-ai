🎙️ Mayank's AI Speech-to-Text App

A modern, multilingual AI-powered voice-to-text system built using **Python, Streamlit, OpenAI Whisper, and Android**.  
Users can upload audio and instantly get accurate transcriptions — in **Hindi, English, or any language**.

---

✨ Features

- ✅ Upload `.mp3`, `.wav`, `.m4a`, `.webm` audio
- 🌍 Auto-detect or manually choose spoken language
- 🧠 Powered by OpenAI Whisper for multilingual transcription
- 📜 Transcribes long audio files (up to 200MB)
- 💾 Download text results
- 🎨 Clean, branded UI (custom themes)
- 📁 Android App with file picker & WebView integration
- 🧪 Google Colab notebook for Whisper (Phase 1)
- 🔄 More powerful features planned!

---

📷 Screenshots & Demo

| Logo | QR Code to APK | Web App |
|------|----------------|---------|
| ![Logo](https://github.com/Mayanks00/speech-to-text-ai/blob/main/APP%20LOGO.png?raw=true) | ![QR](https://github.com/Mayanks00/speech-to-text-ai/blob/main/sppech%20text%20AI%20QR.png?raw=true) | ![WebApp](https://github.com/Mayanks00/speech-to-text-ai/blob/main/WEB%20APP%20PAGE.png?raw=true) |

🎬 **App Demo Video**  
[▶️ Watch Demo (MP4)](https://raw.githubusercontent.com/Mayanks00/speech-to-text-ai/main/video%20recording%20of%20speech%20to%20text%20ai%20app.mp4)

---

## 🛠️ Tech Stack

| Tool          | Purpose                          |
|---------------|----------------------------------|
| Python        | Backend logic & ML integration   |
| Streamlit     | Web UI and deployment            |
| Whisper       | Speech recognition model         |
| FFmpeg        | Audio conversion & handling      |
| Google Colab  | Testing Whisper in notebooks     |
| Android (Kotlin) | WebView + file picker support |

---

🌐 Live App

- 🔹 [**Web App (Streamlit)**](https://speech-to-text-ai-ahg9u7gwpkuuurmtaukxiq.streamlit.app/)
- 🔹 [**Download Android APK**](https://docs.google.com/uc?export=download&id=1NzeYVuIbq7bAnXzeRigo8q3dqhr3lMgs)

🧪 Tested on Android 10–14 ✅  
📁 File upload, back navigation, WebView fully supported!

---

📦 Project Structure:


📁 speech-to-text-ai
├── app.py                 # Streamlit web app
├── audio.ipynb            # Google Colab notebook (Phase 1)
├── requirements.txt       # Required Python packages
├── README.md              # Project overview
└── .streamlit/
    └── config.toml        # UI config for Streamlit

  
🚀 Run Locally:

Prerequisites: Python 3.9+ and pip

# Step 1: Clone the repo
git clone https://github.com/Mayanks00/speech-to-text-ai
cd speech-to-text-ai

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run the app
streamlit run app.py

App will open at:

📍 http://localhost:8501

📗 Phase 1: Google Colab Whisper Notebook:

*Install Whisper

*Upload audio files

*Transcribe into any language

*Download transcript

📎 File: audio.ipynb

📱 Android App (Phase 2):

🔗 Uses WebView to display web app

📂 File picker supported

⚙️ Lightweight, works offline after loading

✅ Compatible With:

*Android 10 to Android 14

*All modern devices with file access permissions

*Download via QR Code or Google Drive

*Enable “Install from unknown sources” before installing

📅 Future Plans:

🎙️ Real-time mic transcription

📁 Upload from recordings directly

🧠 NLP-based text cleaning and formatting

🌐 Offline speech recognition

📤 Save transcript to Google Drive

📊 Analytics on transcription time

☁️ Cloud sync and speech storage

📱 Publish to Google Play Store

📃 License:

MIT License — Free to use, modify, and share with credit.
© 2025 Mayank Pratap Singh

👨‍💻 Developed by:
Mayank Pratap Singh.






