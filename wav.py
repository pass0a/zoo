# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pl
import wave

sampling_rate = 44100

t = np.arange(0, 2.0, 1.0 / sampling_rate)
x = 0.5 * np.sin((2 * np.pi * 100) * t)
x = (x * 32767).astype(np.short)
print(type(t[0]), type(x[1]))
fo = wave.open(u"test.wav", "wb")  # type: wave.Wave_write
fo.setnchannels(1)
fo.setsampwidth(2)
fo.setframerate(sampling_rate)
fo.writeframes(x.tostring())
fo.close()

pl.plot(t, x)
pl.savefig("tmp.jpg")
pl.show()
