import mmap
import ctypes
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ctypes import c_int32, c_float, c_wchar

df = pd.read_csv('samples.csv')

dflap2 = df[df['lap'] == 2]
dflap3 = df[df['lap'] == 3]

fixedGrid = np.linspace(start=0.000, stop=1.000, num=1000)

interpolated_speed2 = np.interp(fixedGrid, dflap2['position'], dflap2['speed_kmh'])
interpolated_speed3 = np.interp(fixedGrid, dflap3['position'], dflap3['speed_kmh'])


delta = interpolated_speed2 - interpolated_speed3
plt.figure(figsize=(12,5))
plt.plot(fixedGrid, delta,color='tab:blue', linewidth=1)
plt.axhline(0, color='black', linewidth=0.8)  # zero-reference line
plt.fill_between(fixedGrid, delta, 0, where=(delta > 0), color='green', alpha=0.3, label='Lap 2 faster')
plt.fill_between(fixedGrid, delta, 0, where=(delta < 0), color='red', alpha=0.3, label='Lap 3 faster')
plt.xlabel('Normalized track position')
plt.ylabel('Speed delta (km/h)')
plt.title('Lap 2 vs Lap 3 — Speed Delta')
plt.legend()
plt.tight_layout()
plt.savefig('speed_delta.png')
plt.show()

# plt.plot(interpolated_speed2['x'], interpolated_speed2['y'])