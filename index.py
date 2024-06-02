import random

kandidat = [
    "Francesco Bagnaia (Ducati Lenovo Team)",
    "Jorge Martin (Pramac Ducati)",
    "Marc Marquez (Gresini Ducati)",
    "Pedro Acosta (Red Bull Tech 3 GasGas)",
    "Enea Bastianini (Ducati Lenovo Team)"
]

num_simulations = 10000

kemenangan = {kandidat[i]: 0 for i in range(len(kandidat))}

for _ in range(num_simulations):
    pemenang = random.choice(kandidat)
    kemenangan[pemenang] += 1

prediksi_juara = max(kemenangan, key=kemenangan.get)

print(f"Prediksi Juara Dunia MotoGP 2024 adalah: {prediksi_juara}")
print("\nRincian Jumlah Kemenangan:")
for k, v in kemenangan.items():
    print(f"{k}: {v} kemenangan")