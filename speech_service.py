from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from vosk import Model, KaldiRecognizer
import wave
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # ✅ Allow frontend (port 5000) to connect

# Path to your Vosk model
MODEL_PATH = "vosk-model-small-en-in-0.4"

# ✅ Load model once at startup
if not os.path.exists(MODEL_PATH):
    print("❌ Model not found! Please download and place it in the folder.")
    model = None
else:
    model = Model(MODEL_PATH)
    print("✅ Model loaded successfully!")

# ✅ Serve index.html (since it's in the same folder)
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# ✅ Transcription endpoint
@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    audio_path = "temp.wav"
    audio_file.save(audio_path)

    wf = wave.open(audio_path, "rb")

    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        wf.close()
        os.remove(audio_path)
        return jsonify({"error": "Audio file must be WAV format mono PCM"}), 400

    rec = KaldiRecognizer(model, wf.getframerate())
    transcript = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            transcript += result.get("text", "") + " "

    final_result = json.loads(rec.FinalResult())
    transcript += final_result.get("text", "")

    wf.close()
    os.remove(audio_path)

    return jsonify({"transcript": transcript.strip()})

if __name__ == "__main__":
    print("✅ Speech-to-Text backend is running at http://127.0.0.1:8000")
    app.run(debug=False, port=8000)
