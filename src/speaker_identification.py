import numpy as np

def detect_gender(audio_features):
    """Estimates speaker gender based on pitch."""
    pitches = audio_features['pitches']
    median_pitch = np.median(pitches)
    if median_pitch < 165:
        return "Male"
    elif median_pitch > 180:
        return "Female"
    else:
        return "Unknown"

def identify_speakers_by_pitch(audio_path, segments):
    """Identifies speakers in segments using pitch features."""
    for segment in segments:
        segment['gender'] = detect_gender(segment)
        segment['speaker'] = f"{segment['gender']}_speaker"
    return segments
