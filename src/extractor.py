import ffmpeg
from pathlib import Path
import os
os.environ["PATH"] += r";D:\ffmpeg\bin"

def extract_audio(video_path: Path, output_path: Path):
    try:
        (
            ffmpeg
            .input(str(video_path))
            .output(str(output_path), format='mp3', acodec='libmp3lame', ac=2, ar='44100')
            .run(overwrite_output=True)
        )
        print(f"Audio extracted successfully to {output_path}")
    except ffmpeg.Error as e:
        print(f"An error occurred while extracting audio: {e.stderr.decode()}")

extract_audio(Path("D:/naruto.mp4"), Path("D:/naruto.wav"))