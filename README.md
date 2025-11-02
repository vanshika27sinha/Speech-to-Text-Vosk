

Speech-to-Text (Vosk)

A lightweight and efficient Speech-to-Text (STT) web application built using Python (Flask) for backend processing and HTML, CSS, and JavaScript for the frontend.
The app records your voice (or accepts .wav input), sends it to the backend for processing using Vosk Offline Speech Recognition, and returns the transcribed text instantly.

🚀 Features

🎧 Record or upload audio directly through the browser
🧠 Converts speech into text using Vosk (Offline Speech Recognition)
💾 Saves recorded audio in .wav format
⚙️ Integrated backend (Flask) and frontend (Node.js + HTML/JS)
🖥️ Simple, clean, and responsive web interface

🗂️ Project Structure
Speech-To-Text-Vosk/
│
├── record_audio.py          # Script for local voice recording
├── speech_service.py        # Flask backend using Vosk for speech recognition
├── server.js                # Node.js server hosting the frontend
├── index.html               # Frontend interface
├── package.json             # Frontend dependencies
├── requirements.txt         # Python dependencies
├── test_audio.wav           # Sample audio file
└── README.md

⚙️ Setup Instructions
🧩 Step 1 — Clone the Repository
git clone https://github.com/vanshika27sinha/Speech-to-Text-Vosk.git
cd Speech-to-Text-Vosk

🐍 Step 2 — Setup the Python Backend

Create and activate a virtual environment (recommended):

conda create -n speechtext python=3.10 -y
conda activate speechtext


Install dependencies:

pip install -r requirements.txt


Run the Flask backend:

python speech_service.py


✅ Backend will start at:
👉 http://127.0.0.1:8000/

💻 Step 3 — Setup and Run the Frontend

Run the Node.js frontend server:

node server.js


✅ Frontend will run at:
👉 http://127.0.0.1:5000/

🎤 Step 4 — Record Audio Locally (Optional)

You can record short clips using the command below:

python record_audio.py


It records a 5-second audio clip and saves it as test_audio.wav.

🧪 API Endpoint
Endpoint	Method	Description
/transcribe	POST	Upload audio and receive the transcribed text

Example curl request:

curl -X POST -F "file=@test_audio.wav" http://127.0.0.1:8000/transcribe

🛠️ Technologies Used

🐍 Python 3.10

⚙️ Flask

🧩 Vosk Speech Recognition

🎧 SoundDevice & SciPy

🌐 HTML5, CSS3, JavaScript (Fetch API)

💻 Node.js with Express.js

📦 Requirements
Flask
vosk
sounddevice
scipy

📸 Output Screenshot
🎯 Transcription Output

(Add the above image file in your repository root and rename it output_screenshot.png)

💡 Future Enhancements

🌐 Real-time speech streaming
🗣️ Multi-language recognition
☁️ Integration with Google / Whisper APIs
🔊 Audio history and playback
📱 Improved responsive design

🤝 Contribution

Contributions, issues, and feature requests are welcome!
Feel free to open a pull request 💬

✅ Developed by Vanshika Sinha
