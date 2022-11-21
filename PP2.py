# np.roll oder ähnlich für laufzeit
# np.vstack().transpose()
# np.power(10, dB-left-minus-right/20) für dB unterschiede n array_right = array/proportion
# 1d) 50 ms verwischungsstelle
import winsound

import numpy as np
from scipy.io.wavfile import read
from scipy.io.wavfile import write

y, data = read("Acoustic.wav")


def detect_channels(unprocessed_data):
    if len(unprocessed_data.shape) == 1:
        l_data = unprocessed_data
        r_data = unprocessed_data
    else:
        l_data = unprocessed_data[:, 0]
        r_data = unprocessed_data[:, 1]
    return l_data, r_data


def delay(l_data, r_data):
    delayed_r = np.roll(r_data, 20)
    stacked_data = np.asarray(list(zip(l_data, delayed_r)))
    return stacked_data


write('Delayed_test.wav', 44100, delay(detect_channels(data)[0], detect_channels(data)[1]))
winsound.PlaySound("Delayed_test.wav", winsound.SND_FILENAME)
