
# 1d) 50 ms verwischungsstelle
import winsound
import numpy as np
import scipy
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


def delay(l_data, r_data, shift):
    shift = shift * y / 1000
    if shift < 0:
        delayed_r = scipy.ndimage.shift(r_data, abs(shift), mode='constant')
        return l_data, delayed_r
    elif shift >= 0:
        delayed_l = scipy.ndimage.shift(l_data, abs(shift), mode='constant')
        return delayed_l, r_data


def gain_diff(l_data, r_data, amp):
    if amp < 0:
        r_out = r_data * 10**(amp/20)
        return l_data, r_out
    elif amp >= 0:
        l_out = l_data / (10**(amp/20))
        return l_out, r_data


def stack(ch_l, ch_r):
    return np.asarray(list(zip(ch_l, ch_r)))


ch_split = detect_channels(data)[0], detect_channels(data)[1]
ch_delayed = delay(ch_split[0], ch_split[1], 4)
ch_delayed_stacked = stack(ch_delayed[0], ch_delayed[1])
ch_weak = gain_diff(ch_split[0], ch_split[1], -10)
ch_weak_stacked = stack(ch_weak[0], ch_weak[1])


write('Delayed_test.wav', 44100, ch_delayed_stacked)
winsound.PlaySound("Delayed_test.wav", winsound.SND_FILENAME)
