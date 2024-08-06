"""convert mp4 to mp3"""

from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(mp4_path, mp3_path):
    """
    Convert an MP4 file to an MP3 file.

    Parameters:
    mp4_path (str): The path to the input MP4 file.
    mp3_path (str): The path to the output MP3 file.
    """
    try:
        # Load the video file
        video = VideoFileClip(mp4_path)
        
        # Extract the audio
        audio = video.audio
        
        # Write the audio to an MP3 file
        audio.write_audiofile(mp3_path)
        
        # Close the video and audio clips
        audio.close()
        video.close()
        
        print(f"Successfully converted {mp4_path} to {mp3_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# convert_mp4_to_mp3("input_video.mp4", "output_audio.mp3")
