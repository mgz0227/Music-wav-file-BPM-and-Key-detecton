import librosa
import librosa.display
import numpy as np

# Load the audio file
audio_file = 'I:/Archiv/Polle RenderedMusic/02_Trap_Polle_HillWizzard_48000s_24Bit.wav'
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
 

print("BPM:", tempo," Musical Key:", estimated_key)
