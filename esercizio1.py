import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Generazione dei dati
x = np.arange(1, 11)

y1 = np.random.randint(10, 50, size=10)
y2 = np.random.randint(20, 60, size=10)
y3 = np.random.randint(5, 30, size=10)
y4 = np.random.randint(15, 40, size=10)

# Creazione della figura e della griglia 3x2
fig = plt.figure(figsize=(12, 8))
gs = fig.add_gridspec(3, 2)

# Primo grafico: prima riga, prima colonna
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(x, y1, color="blue", marker="o", label="y1")
ax1.set_title("Valori y1")
ax1.legend()

# Secondo grafico: prima riga, seconda colonna
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(
    x, y2,
    color="green",
    marker="s",
    linestyle="--",
    label="y2"
)
ax2.set_title("Valori y2")
ax2.legend()

# Terzo grafico: ultime due righe, prima colonna
ax3 = fig.add_subplot(gs[1:3, 0])
ax3.bar(x, y3, color="orange", label="y3")
ax3.set_title("Valori y3")
ax3.legend()

# Quarto grafico: seconda riga, seconda colonna
ax4 = fig.add_subplot(gs[1, 1])
ax4.scatter(x, y4, color="red", marker="^", label="y4")
ax4.set_title("Valori y4")
ax4.legend()

plt.tight_layout()
plt.show()