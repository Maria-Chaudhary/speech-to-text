# 🎤 Speech to Text Transcriber

A **multilingual speech-to-text web application** powered by **OpenAI Whisper**.  
Upload or record audio in multiple languages, and get accurate transcriptions instantly.  

This app supports **Dark/Light theme toggle** and displays the detected language clearly.

---

## 🌟 Features

- Record audio directly via microphone or upload audio files (`.wav`, `.mp3`, `.m4a`)  
- Automatic **language detection**  
- **Multilingual transcription**: Urdu, English, Hindi, Japanese (more supported by Whisper)  
- **Dark/Light theme toggle**  
- Real-time transcription status messages  
- Stylish, responsive UI with clear instructions and info boxes  

---

## 🖥️ Demo

You can launch the app locally or deploy on [Hugging Face Spaces](https://huggingface.co/):

```bash
gradio app.py

---

## Installation

Follow these steps to set up the Speech-to-Text Transcriber app on your local machine:

### 1. Clone the repository
```bash
git clone https://github.com/your-username/speech-to-text.git
cd speech-to-text
2. Create a virtual environment (recommended)
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run the app
python app.py
5. Access the app
Open the link shown in the terminal (usually http://127.0.0.1:7860) in your browser.

💡 Tip: For best results, use Python 3.10 or above and ensure your microphone works properly.**
