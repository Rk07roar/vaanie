from google.cloud import speech
import io
import moviepy.editor as mp
def transcribe_audio(video_file):
    # Extract audio from video
    clip = mp.VideoFileClip(video_file)
    audio_file = "temp.wav"
    clip.audio.write_audiofile(audio_file)
    client = speech.SpeechClient()
    with io.open(audio_file, "rb") as audio:
        content = audio.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    transcript = " ".join([result.alternatives[0].transcript for result in response.results])
    return transcript