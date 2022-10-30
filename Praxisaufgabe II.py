# Bibliotheken importieren
import wave
import soundfile as sf
import numpy as np
from pygame import mixer


def choose_audio_file():
    """Importiert Audio-Dateien. Der Nutzer kann sich die Datei anhören oder sie analysieren lassen.

    :return
    """
    sound_file = input("Put the filename here: ")
    print("\nWhat do you want to do? \nPress [1] to analyze" + "\nPress [2] to listen")
    file_choice = str(input("\nYour choice: "))
    if file_choice == str(2):
        print("...sound is playing...")
        mixer.music.load(sound_file)
        mixer.music.play()
        print("\nPress [s] to stop:")
        action_choice = input(" ")
        if action_choice == "s":
            mixer.music.stop()
            print("...sound stopped...")
    elif file_choice == str(1):
        initialize(sound_file)


def initialize(input_sound):
    """Prüft nach anzahl der Kanälen und teilt diese bei 2 Kanälen zu jeweils einer Liste auf

    :param input_sound: Übergibt den Namen/Speicherort des Songs, sodass er von wave.open verarbeitet werden kann
    :type input_sound: str
    :return
    """
    obj = wave.open(input_sound, 'r')
    data, fs = sf.read(input_sound, dtype="float32")
    output(input_sound)
    t = obj.getframerate()
    if obj.getnchannels() == 1:
        print("...Calculating single channel...")
        value_calc(data, t)
    elif obj.getnchannels() == 2:
        print("...Calculating two channels...")
        left, right = zip(*data)
        # Linker Stereo-Kanal
        print("\nLeft Channel: ")
        left_array = np.asarray(left)
        value_calc(left_array, t)
        # Linker Stereo-Kanal
        print("\nRight Channel: ")
        right_array = np.asarray(right)
        value_calc(right_array, t)


def value_calc(process_data, t):
    """Berechnet anhand der gegebenen Samples die gefrageten Werte

    :param process_data: Liste der Abtastwerte
    :param t: Zeitparameter, berechnet in initialise()
    :return:
    """
    # Scheitelwert
    monoMax = max(process_data)
    monoMin = min(process_data)
    print("Maximum:\t\t\t\t" + str(monoMax))
    print("Minimum:\t\t\t\t" + str(monoMin))
    # Arithmetischer Mittelwert
    median = (np.sum(process_data) / t)
    print("arithm. Mittelwert:\t\t" + str(median))
    # Gleichrichtwert
    rectifiedValue = (np.sum(abs(process_data)) / t)
    print("Gleichrichtwert:\t\t" + str(rectifiedValue))
    # Effektivwert
    effectiveValue = np.sqrt(np.sum(process_data ** 2) / t)
    print("Effektivwert:\t\t\t" + str(effectiveValue))
    # Crest-Faktor
    crestFactor = monoMax / effectiveValue
    print("Crest-Faktor:\t\t\t" + str(crestFactor))
    # Formfaktor
    formFactor = effectiveValue / rectifiedValue
    print("Form-Faktor:\t\t\t" + str(formFactor))


def output(sound_file):
    """Zeigt wichtige Parameter des gewählten Songs

    :param sound_file: Eingegebene Sound-Datei zum Auslesen durch wave-funktion
    :return
    """
    # Parameter-Ausgabe der ausgewählten Audio-File
    obj = wave.open(sound_file, 'r')
    print("\nNumber of channels:\t\t", obj.getnchannels())
    print("Frame-Rate:\t\t\t\t", obj.getframerate(), "Hz")
    print("Number of frames:\t\t", obj.getnframes())
    secDuration = round((obj.getnframes() / obj.getframerate()), 2)
    minDur = int(secDuration // 60)
    sec = round(secDuration % 60)
    print("Duration:\t\t\t\t", str(minDur) + ":" + str(sec) + "s")


mixer.init()
choose_audio_file()
