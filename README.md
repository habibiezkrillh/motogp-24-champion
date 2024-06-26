# Prediksi Juara Dunia MotoGP 2024

Skrip ini menggunakan pendekatan probabilistik sederhana untuk memprediksi siapa yang akan menjadi juara dunia MotoGP di tahun 2024 dari lima kandidat yang telah ditentukan. Kandidatnya adalah:

1. Francesco Bagnaia (Ducati Lenovo Team)
2. Jorge Martin (Pramac Ducati)
3. Marc Marquez (Gresini Ducati)
4. Pedro Acosta (Red Bull Tech 3 GasGas)
5. Enea Bastianini (Ducati Lenovo Team)

## Pendekatan

Prediksi ini dilakukan menggunakan simulasi Monte Carlo sederhana. Dengan menjalankan simulasi sebanyak 10.000 kali, skrip ini akan memilih pemenang secara acak dari daftar kandidat, dan menghitung berapa kali masing-masing kandidat terpilih sebagai pemenang.

## Cara Menggunakan

1. Pastikan Anda memiliki Python 3.x terinstal di sistem Anda.
2. Unduh atau salin skrip Python di bawah ini ke dalam file bernama `prediksi_motogp.py`.

```python
import random

# Daftar kandidat dengan nama dan tim mereka
kandidat = [
    "Francesco Bagnaia (Ducati Lenovo Team)",
    "Jorge Martin (Pramac Ducati)",
    "Marc Marquez (Gresini Ducati)",
    "Pedro Acosta (Red Bull Tech 3 GasGas)",
    "Enea Bastianini (Ducati Lenovo Team)"
]

# Jumlah simulasi
num_simulations = 10000

# Menghitung jumlah kemenangan untuk setiap kandidat
kemenangan = {kandidat[i]: 0 for i in range(len(kandidat))}

# Melakukan simulasi
for _ in range(num_simulations):
    pemenang = random.choice(kandidat)
    kemenangan[pemenang] += 1

# Menentukan kandidat dengan jumlah kemenangan terbanyak
prediksi_juara = max(kemenangan, key=kemenangan.get)

# Menampilkan hasil prediksi
print(f"Prediksi Juara Dunia MotoGP 2024 adalah: {prediksi_juara}")
print("\nRincian Jumlah Kemenangan:")
for k, v in kemenangan.items():
    print(f"{k}: {v} kemenangan")
```
 
 
