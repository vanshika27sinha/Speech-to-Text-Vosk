A lightweight and efficient Speech-to-Text (STT) web application built using Python (Flask) for backend processing and HTML, CSS, and JavaScript for the frontend. The app records your voice, saves it as an audio file, and converts it into text automatically.

🚀 Features

🎧 Record audio directly through the browser

🧠 Converts speech into text using the backend

💾 Saves recorded audio in .wav format

⚙️ Integrated backend and frontend (Flask + Node.js)

🖥️ Simple, clean web interface

🗂️ Project Structure
Speech-To-Text-App/
│
├── backend/
│   ├── record_audio.py        # Script for local voice recording
│   ├── server.py              # Flask backend handling transcription
│   ├── requirements.txt       # Backend dependencies
│
├── frontend/
│   ├── index.html             # Main web interface
│   ├── style.css              # Styling for the UI
│   ├── script.js              # Logic for recording/sending audio
│   ├── server.js              # Node.js server hosting the frontend
│
└── README.md

⚙️ Setup Instructions
🧩 Step 1 — Clone the Repository
git clone https://github.com/yourusername/speech-to-text-app.git
cd speech-to-text-app

🐍 Step 2 — Setup the Python Backend

Create and activate a virtual environment (recommended):

conda create -n speechtext python=3.10 -y
conda activate speechtext


Install dependencies:

pip install -r backend/requirements.txt


Run the Flask backend:

cd backend
python server.py


✅ Backend will start at:
http://127.0.0.1:5000

💻 Step 3 — Setup and Run the Frontend

Go to the frontend folder:

cd ../frontend


Run the Node.js frontend server:

node server.js


✅ Frontend will run at:
http://127.0.0.1:3000

🎤 Step 4 — Record Audio Locally (Optional)

You can record short clips using the command below:

cd backend
python record_audio.py


It records a 5-second audio clip and saves it as test_audio.wav.

🧪 API Endpoint
Endpoint	Method	Description
/transcribe	POST	Upload audio and receive the transcribed text

Example curl request:

curl -X POST -F "file=@test_audio.wav" http://127.0.0.1:5000/transcribe

🛠️ Technologies Used

Python 3.10

Flask

SoundDevice & SciPy

HTML5, CSS3, JavaScript (Fetch API)

Node.js with Express.js

📦 Requirements
Flask
sounddevice
scipy

📸 Screenshots
Recording Interface	Transcription Output

	
💡 Future Enhancements

🌐 Real-time speech streaming

🗣️ Multi-language support

☁️ Integration with Google / Whisper APIs

🔊 Audio history and playback

🤝 Contribution

Contributions are always welcome!
If you’d like to improve this project, open an issue or a pull request on GitHub.
