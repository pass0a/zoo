# -*- coding: utf-8 -*-
import wave
import matplotlib.pyplot as pl
import numpy as np

fft_size = 512
# 打开WAV文档
f = wave.open(u"test2.wav", "rb")

# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

# 读取波形数据
str_data = f.readframes(nframes)
f.close()

# 将波形数据转换为数组
wave_data = np.frombuffer(str_data, dtype=np.int32)
time = np.arange(0, 2.0, (1.0 / framerate))

xs = wave_data[:fft_size]
xf = np.fft.rfft(xs) / fft_size
freqs = np.linspace(0, framerate / 2, fft_size // 2 + 1)
xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

pl.plot(freqs, xfp)
pl.show()