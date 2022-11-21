import numpy as np
import pylab as p
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import winsound
y, data = read("Datei_C.wav")
data_len = len(data)


def static_print():
    print("Abtastwerte:", data)
    print("Abtastfrequenz:", y)
    print("Anzahl der Abtastwerte:", data_len)
    print("Index-Array:", amp_to_db(data)[1])
    print("T-Array:", amp_to_db(data)[0])
    print("Max-Amp:", amp_to_db(data)[3])
    print("Energie:", calc_energy_signal(data))


def calc_energy_signal(amplitude):
    energy_amp = np.zeros(len(amplitude))
    energy_amp_log = np.zeros(len(amplitude))
    # max_energy = max(amplitude**2)
    for i in range(len(amplitude)):
        energy_amp[i] = abs(amplitude[i])**2
        energy_amp_log[i] = 20*np.log10(energy_amp[i])
    return energy_amp, energy_amp_log


def amp_to_db(amplitude):
    max_amp = max(abs(amplitude))
    max_amp_db = 10 * np.log10(abs(max_amp))
    t_array = np.zeros(3)
    index_array = np.zeros(3)
    db_data = np.zeros(len(amplitude))
    for i in range(len(amplitude)):
        if amplitude[i] != 0:
            db_data[i] = 20 * np.log10(abs(amplitude[i]))
            if round(max_amp_db-db_data[i]) == 20:
                t_array[0] = abs(amplitude[i])
                index_array[0] = i
            if round(max_amp_db-db_data[i]) == 40:
                t_array[1] = abs(amplitude[i])
                index_array[1] = i
            if round(max_amp_db-db_data[i]) == 60:
                t_array[2] = abs(amplitude[i])
                index_array[2] = i
    return t_array, index_array, db_data, max_amp


static_print()
#winsound.PlaySound("Datei_C.wav", winsound.SND_FILENAME)
plt.subplot(131)
plt.plot(data)
plt.subplot(132)
plt.plot(calc_energy_signal(data)[0])
plt.subplot(133)
plt.plot(calc_energy_signal(data)[1])
plt.show()
