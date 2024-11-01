from moviepy.editor import VideoFileClip
import os

# Function to extract audio from video
def extract_audio(video_file, output_audio_file):
    # Load the video file
    video = VideoFileClip(video_file)
    
    # Extract the audio
    audio = video.audio
    
    # Write the audio to a file
    audio.write_audiofile(output_audio_file)
    
    # Close the files to free up resources
    audio.close()
    video.close()

# Example usage
video_path = "test_vid.mp4"
output_audio_path = "extracted_audio.mp3"
extract_audio(video_path, output_audio_path)