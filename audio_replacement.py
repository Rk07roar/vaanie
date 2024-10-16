import moviepy.editor as mp
def replace_audio(video_file, audio_file):
    video = mp.VideoFileClip(video_file)
    audio = mp.AudioFileClip(audio_file)
    final_video = video.set_audio(audio)
    final_video.write_videofile("final_video.mp4", codec="libx264")
