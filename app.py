import librosa
import librosa.display
import numpy as np
#import os
from processing_py import *
import tkinter as tk
from tkinter import filedialog

#Setup
audio_file=""
#Setup Processing Py Container
app = App(600,400) # create window: width, height
#Setup tkinter Container (open File Button)
root = tk.Tk()


#define comand for file drop
def doIt(audio_file):
   # check the audio file
   print("Selected file:", audio_file)
   
   #audio_file = 'I:/Archiv/Polle RenderedMusic/02_Trap_Polle_HillWizzard_48000s_24Bit.wav'
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

   while(True):
      app.background(255,0,0) # set background:  red, green, blue
      app.fill(255,255,0) # set color for objects: red, green, blue
     # app.ellipse(app.mouseX,app.mouseY,50,50) # draw a circle: center_x, center_y, size_x, size_y

      
      app.textSize(24)
      app.text("BPM:"+str(tempo)+" Musical Key:"+ str(estimated_key),50,50)
      app.redraw() # refresh the window

#define file selection open file dialog
def open_file_dialog():
    filepath = filedialog.askopenfilename()+''   
    doIt(filepath)
    print("Selected file:", filepath)
    root.exit()


button = tk.Button(root, text="Open File", command=open_file_dialog)
button.pack()
root.mainloop()



print("BPM:", tempo," Musical Key:", estimated_key)

 

 