🎙️ Mayank's AI Speech-to-Text App

A modern, multilingual AI-powered voice-to-text system built using **Python, Streamlit, and OpenAI Whisper**.  
Users can upload speech audio and instantly get highly accurate transcriptions — in any language.

---

✨ Features

✅ Upload audio files (`.mp3`, `.wav`, `.m4a`, `.webm`)  
🌍 Auto language detection or manual language selection  
📜 Transcribes long audio files up to **200MB**  
💾 Download the transcribed text  
🎨 Custom branding and clean UI design  
📁 Google Colab notebook included (Phase 1)  
🧠 Powered by OpenAI’s Whisper model
💻 Use directly in browser or on Android 📱

---

🛠️ Tech Stack

| Tool          | Purpose                          |
|---------------|----------------------------------|
| Python        | Backend logic & ML integration   |
| Streamlit     | Interactive frontend web UI      |
| Whisper       | Speech-to-text AI model          |
| FFmpeg        | Audio conversion and handling    |
| Google Colab  | Prototyping and model testing    |
| Android       | building android app using kotlin|

---

🧪 Project Structure


📁 speech-to-text-ai
├── app.py # Streamlit web app
├── audio.ipynb # Google Colab notebook (Phase 1)
├── requirements.txt # Required Python packages
├── README.md # This project file
└── .streamlit/
└── config.toml # UI theme settings


---

🚀 How to Run Locally

> Prerequisites: Python 3.9+ and `pip` installed

🔹 1. Clone the Repository-

git clone https://github.com/Mayanks00/speech-to-text-ai
cd speech-to-text-ai

🔹 2. Install Required Packages-

pip install -r requirements.txt 

🔹 3. Launch the App-

streamlit run app.py


The app will open in your browser at

http://localhost:8501

📲 Android App is Now Available!

📦 **Download APK:**  

[Click here to install the Android version](https://drive.google.com/file/d/1NzeYVuIbq7bAnXzeRigo8q3dqhr3lMgs/view?usp=drive_link) ⚠️ Note: You may need to enable "Install from unknown sources" in your phone settings.

🌐 Try the Live App-

Hosted on Streamlit Cloud — no setup needed!

👉 [https://speech-to-text-ai-ahg9u7gwpkuuurmtaukxiq.streamlit.app](https://speech-to-text-ai-ahg9u7gwpkuuurmtaukxiq.streamlit.app)


📗 Phase 1: Colab-Based Whisper Demo- 

If you're interested in learning how Whisper works or want to experiment with it in notebooks, check out the included audio.ipynb.

This walks through:

*Installing Whisper and dependencies

*Uploading audio files

*Transcribing and saving text

🌐 Deployment-

This app is easily deployable using:

🔹 Streamlit Cloud

🔹 Render / Hugging Face / Vercel (Advanced)


📱 Future Plan-

🎙️ Real-time microphone transcription (coming soon)
🌐 In-app browser fallback handling
🗣️ Multi-language accuracy tuning
💡 Cleaner UI + offline capabilities
🗂️ TO Add backend support with MongoDB for saving history
📱 **Publishing to Google Play Store**
☁️ Cloud sync or export-to-Google Drive
📊 Analytics for transcription usage


📃 License-

This project is licensed under the MIT License.
Free to use, modify, and share with credits.


👨‍💻 Developed By-

Mayank Pratap Singh(SELF-TAUGHT LEARNER)











