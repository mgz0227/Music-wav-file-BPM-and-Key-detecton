import librosa
import numpy as np
import argparse

def main(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Calculate tempo (BPM)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    # Compute the Chroma Short-Time Fourier Transform (chroma_stft)
    chromagram = librosa.feature.chroma_stft(y=y, sr=sr)

    # Calculate the mean chroma feature across time
    mean_chroma = np.mean(chromagram, axis=1)

    # Define the mapping of chroma features to keys
    chroma_to_key = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Find the key by selecting the maximum chroma feature
    estimated_key_index = np.argmax(mean_chroma)
    estimated_key = chroma_to_key[estimated_key_index]

    print("BPM:", tempo, "Musical Key:", estimated_key)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze audio file to find tempo and musical key.")
    parser.add_argument("audio_file", type=str, help="Path to the audio file")
    args = parser.parse_args()
    main(args.audio_file)
