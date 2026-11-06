# Muhammad Farrel As Shafwan
# NIM: 2109106045
# 1A

import numpy as np

np.random.seed(42) 
nilaiUjian = np.random.randint(50, 100, size=30)

print(" DATA NILAI UJIAN ASLI ")
print(nilaiUjian)

nilaiUrutDesc = np.sort(nilaiUjian)[::-1]

print("\n NILAI URUTAN DARI TERBESAR KE TERKECIL ")
print(nilaiUrutDesc)

topFive = nilaiUrutDesc[:5]

print("\n 5 NILAI TERBESAR ")
print(topFive)