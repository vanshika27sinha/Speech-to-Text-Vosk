import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import os

def record_audio(filename="test_audio.wav", fs=16000):
    try:
        # Ask user for recording duration
        duration = input("Enter recording duration in seconds (default 5): ")
        duration = int(duration) if duration.strip() else 5

        print(f"\nRecording for {duration} seconds... 🎤")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished

        # Normalize and save
        audio = np.int16(audio / np.max(np.abs(audio)) * 32767)
        write(filename, fs, audio)

        print(f"✅ Recording complete! Saved as '{filename}' ({fs/1000:.0f} kHz, {duration}s)")

    except Exception as e:
        print(f"❌ Error during recording: {e}")

if __name__ == "__main__":
    record_audio()
