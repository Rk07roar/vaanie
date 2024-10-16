import streamlit as st
import tempfile
import os
from audio_transcription import transcribe_audio
from transcription_correction import correct_transcription
from audio_generation import generate_audio
from audio_replacement import replace_audio

st.title("Video Audio Replacement with AI Voice")
video_file = st.file_uploader("Upload a Video File", type=["mp4", "mov", "avi", "mkv"])

if video_file:
    st.video(video_file)

if st.button("Process Video"):
    if video_file is not None:
        try:
            # Save the uploaded video file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
                temp_video.write(video_file.read())
                temp_video_path = temp_video.name

            # Transcribe the audio from the video
            transcript = transcribe_audio(temp_video_path)
            # Correct the transcription
            corrected_text = correct_transcription(transcript)
            # Generate audio from the corrected text
            generate_audio(corrected_text)

            # Provide a download button for the generated audio
            with open("output.mp3", "rb") as audio_file:
                st.download_button("Download Generated Audio", audio_file, file_name="generated_audio.mp3")

            # Replace the original video audio with the generated audio
            replace_audio(temp_video_path, "output.mp3")

            st.success("Video processed successfully! Download the final video.")
            st.video("final_video.mp4")  # Display the final video
            st.download_button("Download Final Video", "final_video.mp4")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        finally:
            # Clean up temporary files
            if os.path.exists(temp_video_path):
                os.remove(temp_video_path)
