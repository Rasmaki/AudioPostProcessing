import numpy as np


def fade_in(samples, y):
    fade_in_factor = np.linspace(0., 1., y)

    for i in range(len(fade_in_factor)):
        samples[i] = samples[i] * fade_in_factor[i]

    return samples


def fade_out(samples, x):
    fade_out_factor = np.linspace(0., 1., x)

    for j in range(len(fade_out_factor)):
        index = len(samples)-1-j
        value = samples[index]*fade_out_factor[j]
        samples[index] = value

    return samples
