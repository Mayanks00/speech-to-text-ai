import streamlit as st
import whisper
import tempfile
import os
import datetime
import subprocess

# Set custom page config
st.set_page_config(
    page_title="🧠 Mayank's AI Speech-to-Text App",
    layout="centered",
    initial_sidebar_state="auto"
)

# Updated CSS styling
custom_css = """
<style>
    body {
        background-color: #f3e5f5;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background-color: #f3e5f5;
        color: #1a237e;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #4a148c;
        font-weight: 600;
    }
    .stButton > button {
        background-color: #6a1b9a;
        color: white;
        border-radius: 6px;
        padding: 0.5em 1em;
    }
    .stFileUploader, .stTextArea {
        background-color: #ffffff !important;
    }
    .custom-box {
        background-color: #ffffff;
        color: #1a237e;
        padding: 1em;
        border-radius: 8px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        margin-top: 1em;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.title("🎙️ Mayank's AI-Powered Speech Recognition")
st.write("Upload audio in any language — it will auto-detect or let you choose.")

@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Language selector
language_map = {
    "Auto-detect": None,
    "English": "en",
    "Hindi": "hi",
    "Urdu": "ur",
    "Punjabi": "pa",
    "Gujarati": "gu",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Marathi": "mr",
    "Malayalam": "ml",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Arabic": "ar",
    "Chinese": "zh"
}

st.subheader("🌍 Select Language")
selected_language = st.selectbox("Choose spoken language", list(language_map.keys()))
language_code = language_map[selected_language]

def transcribe_audio(audio_path, language_code):
    try:
        if os.path.getsize(audio_path) == 0:
            return "[Error: Empty or corrupted audio file.]"
        if language_code:
            result = model.transcribe(audio_path, language=language_code)
        else:
            result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        return f"[Error during transcription: {str(e)}]"

# 📁 Upload section
st.subheader("📁 Upload Audio File (mp3, wav, m4a, webm)")
uploaded_file = st.file_uploader("Choose a file", type=["mp3", "wav", "m4a", "webm"])

if uploaded_file is not None:
    input_ext = os.path.splitext(uploaded_file.name)[1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=input_ext) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    if input_ext == ".webm":
        wav_path = temp_path.replace(".webm", ".wav")
        ffmpeg_cmd = ["ffmpeg", "-i", temp_path, wav_path]
        subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        audio_path = wav_path
    else:
        audio_path = temp_path

    st.audio(uploaded_file, format='audio/mpeg')

    if st.button("🔍 Transcribe File"):
        with st.spinner("Transcribing uploaded file..."):
            transcript = transcribe_audio(audio_path, language_code)
            st.subheader("📝 Transcribed Text")
            st.markdown(f"<div class='custom-box'>{transcript}</div>", unsafe_allow_html=True)

            filename = f"transcript_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(transcript)

            with open(filename, "rb") as f:
                st.download_button("💾 Download Transcript", f, filename, mime="text/plain")

        os.remove(temp_path)
        if input_ext == ".webm" and os.path.exists(wav_path):
            os.remove(wav_path)



