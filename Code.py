import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_audio_to_wav(input_audio_path):
    if input_audio_path.endswith(".mp3"):
        audio = AudioSegment.from_mp3(input_audio_path)
        wav_path = input_audio_path.replace(".mp3", ".wav")
        audio.export(wav_path, format="wav")
        return wav_path
    elif input_audio_path.endswith(".wav"):
        return input_audio_path
    else:
        raise ValueError("Unsupported file format. Use .wav or .mp3")

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand the audio."
        except sr.RequestError as e:
            return f"Error with the recognition service: {e}"

if __name__ == "__main__":
    input_file = "sample_audio.mp3"  # Replace with your audio file
    wav_file = convert_audio_to_wav(input_file)
    transcription = transcribe_audio(wav_file)
    print("Transcribed Text:\n", transcription)
