import os
from pathlib import Path
import subprocess
import demucs

os.environ["PATH"] += r";D:\ffmpeg\bin"


def separate_audio(audio_path: str, output_dir: str, device: str = "cpu") -> dict:
    """
    Розділяє аудіо на окремі треки за допомогою Demucs.
    
    Args:
        audio_path: шлях до .wav файлу
        output_dir: папка куди зберегти результат
        device: 'cpu' або 'cuda'
    
    Returns:
        dict з шляхами до треків: {'vocals': ..., 'no_vocals': ...}
    """
    result = subprocess.run([
        r"d:\anime_Sep\dubbing_separator\venv\Scripts\python.exe", "-m", "demucs",
        "--device", device,
        "--two-stems", "vocals",
        "--out", output_dir,
        audio_path
    ],text=True)

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    if result.returncode != 0:
        print(f"Demucs failed with code {result.returncode}")
        return {}

    stem_name = Path(audio_path).stem
    stems_dir = Path(output_dir) / "htdemucs" / stem_name

    tracks = {
        "vocals":    str(stems_dir / "vocals.wav"),
        "no_vocals": str(stems_dir / "no_vocals.wav"),
    }

    print(f"Separation done! Tracks saved to {stems_dir}")
    return tracks

separate_audio("D:/shed.wav", "D:/ttl_output")