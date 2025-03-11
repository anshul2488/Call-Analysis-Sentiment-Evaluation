import librosa
import numpy as np

def extract_audio_features(audio_path):
    """Extracts audio features like pitch, MFCCs, and spectral contrast."""
    y, sr = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    return {
        'mfccs': mfccs,
        'contrast': contrast,
        'pitches': pitches
    }

def process_audio_segment(audio_path):
    """Processes an audio segment and extracts features."""
    features = extract_audio_features(audio_path)
    return features
