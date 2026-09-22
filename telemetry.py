import mmap
import ctypes
import time
import pandas as pd
import numpy as np
import matplotlib as plt
from ctypes import c_int32, c_float, c_wchar

df = pd.read_csv('samples.csv')

dflap2 = df[df['lap'] == 2]
dflap3 = df[df['lap'] == 3]

fixedGrid = np.linspace(start=0.000, stop=1.000, num=1000)

interpolated_speed2 = np.interp(fixedGrid, dflap2['position'], dflap2['speed_kmh'])
interpolated_speed3 = np.interp(fixedGrid, dflap3['position'], dflap3['speed_kmh'])



print(dflap2[['position']].head(10))
print(dflap2[['position']].tail(10))


# plt.plot(interpolated_speed2['x'], interpolated_speed2['y'])