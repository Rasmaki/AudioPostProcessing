# -*- coding: utf-8 -*-
"""
created: 25-3-2020
Version: Anzeige von sin omega t und 
abspielen des Tons nach Speichern in Datei test.wav
ohne Aliasing
@author: e_wilk
"""

# import matplotlib.pyplot as plt
import numpy as np
import winsound
import Fade
import keyboard
# from scipy.io.wavfile import read
from scipy.io.wavfile import write

userInput = input("Welcome to your hearing test. Please Press 'Enter' to proceed.")
y = 1
Fs = 44100
y_dach = 10000
fs = 300
t = np.linspace(0., 1., Fs)

b = np.array(y, dtype=np.int16)
data = y * np.sin(2. * np.pi * fs * t)

for u in range(15):
    data = y * np.sin(2. * np.pi * fs * t)
    data_fade_in = Fade.fade_in(data, 20000)
    data_fade_in_out = Fade.fade_out(data_fade_in, 20000)
    write('test_fadeIN.wav', Fs, data_fade_in_out.astype(np.int16))
    winsound.PlaySound("test_FadeIN.wav", winsound.SND_FILENAME)
    y = 2*y
    input_u = input("Did you hear the sound (y/n)?")
    if input_u.lower() == "n":
        continue
    else:
        y_300 = y
        print("Loudness: ", y)
        break
