import pandas as pd

df = pd.read_csv('samples.csv')

dflap2= df[df['lap'] == 2]


print(dflap2[dflap2['speed_kmh'] < 10])
print(dflap2['position'].diff().describe())