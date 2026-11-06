# Muhammad Farrel As Shafwan
# NIM: 2109106045
# 1A

import numpy as np

suhuCelcius = np.array([28.5, 30.0, 29.2, 31.5, 27.8, 28.0, 29.5, 30.2, 31.0, 28.9])
suhuFahrenheit = (suhuCelcius * 9 / 5) + 32

print(" CONVERSI SUHU (CELSIUS KE FAHRENHEIT) ")
for i in range(len(suhuCelcius)):
    print(f"Hari ke-{i + 1}: {suhuCelcius[i]} °C  ->  {suhuFahrenheit[i]:.2f} °F")