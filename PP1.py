import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import winsound
y, data = read("Datei_C.wav")
data_len = len(data)


def static_print():
    print("Abtastwerte:", data)
    print("Energiewerte:", calc_energy_signal(data))
    print("Abtastfrequenz:", y)
    print("Anzahl der Abtastwerte:", data_len)
    print("Energiepegel bei -20, -40, -60 dB:", amp_to_db(calc_energy_signal(data))[0])
    print("Indexe der Werte:", amp_to_db(data)[1])
    energy_sgl = calc_energy_signal(data)
    db_calc20 = amp_to_db(energy_sgl)[0][0]
    db_calc40 = amp_to_db(energy_sgl)[0][1]
    t_calc20 = amp_to_db(energy_sgl)[1][0]
    t_calc40 = amp_to_db(energy_sgl)[1][1]
    print("Verringerung des Energiepegels bei -20 dB:", db_calc20)
    print("Verringerung des Energiepegels bei -40 dB:", db_calc40)
    print("Index des Abtastwerts bei -20 dB:", t_calc20)
    print("Index des Abtastwerts bei -40 dB:", t_calc40)
    tn_calc = calc_tn(db_calc40, db_calc20, t_calc40, t_calc20)
    print(tn_calc/y)


def calc_energy_signal(amplitude):
    energy_signal = np.zeros(len(amplitude))
    for i in range(len(amplitude)):
        energy_signal[i] = amplitude[i]**2
    return energy_signal


def amp_to_db(amplitude):
    max_amp = max(abs(amplitude))
    t_array = np.zeros(3)
    index_array = np.zeros(3)
    db_data = np.zeros(len(amplitude))
    for i in range(len(amplitude)):
        db_data[i] = 20*np.log10(abs(amplitude[i])/max_amp)
        if db_data[i] - 20 == 0:
            t_array[0] = abs(amplitude[i])
            index_array[0] = i
        if db_data[i] - 40 == 0:
            t_array[1] = abs(amplitude[i])
            index_array[1] = i
        if db_data[i] - 60 == 0:
            t_array[2] = abs(amplitude[i])
            index_array[2] = i
    return t_array, index_array, db_data


def calc_tn(l2, l1, t2, t1):
    t_n = 0.163*(t2-t1/l2-l1)
    return t_n


static_print()
winsound.PlaySound("Datei_C.wav", winsound.SND_FILENAME)
plt.subplot(131)
plt.plot(data)
plt.subplot(132)
plt.plot(amp_to_db(calc_energy_signal(data))[2])
plt.subplot(133)
plt.plot()
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()
