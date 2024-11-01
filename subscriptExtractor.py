import moviepy.editor as mp
import os

def split_video_into_intervals(video_path, output_file, interval=2):
    """
    Splits the video into intervals of the given duration (in seconds)
    and saves each interval into the same file, overwriting the previous one.
    """
    # Load the video
    video = mp.VideoFileClip(video_path)
    total_duration = int(video.duration)

    # Iterate over the video in 2-second intervals
    for start in range(0, total_duration, interval):
        end = min(start + interval, total_duration)
        
        # Extract the subclip
        subclip = video.subclip(start, end)
        
        # Overwrite the same output file for each interval
        subclip.write_videofile(output_file, codec="libx264", audio_codec="aac")
        print(f"Saved new clip: {output_file}")


video_path = "test_vid.mp4" 
output_file = "output_clip.mp4"  
split_video_into_intervals(video_path,output_file)