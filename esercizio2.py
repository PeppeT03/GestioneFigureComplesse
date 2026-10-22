import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

np.random.seed(42)

# Generazione dei dati
x = np.arange(1, 21)
y_main = np.random.randint(50, 150, size=20)
y_sub1 = np.random.randint(10, 50, size=20)
y_sub2 = np.random.randint(20, 80, size=20)

# Troviamo l'indice del picco massimo
max_idx = np.argmax(y_main)

# Creazione della figura e della griglia
fig = plt.figure(figsize=(12, 8))

gs = GridSpec(
    2, 2,
    height_ratios=[2, 1],
    width_ratios=[2, 1],
    hspace=0.4,
    wspace=0.3
)

# Grafico principale
ax_main = fig.add_subplot(gs[0, :])

ax_main.plot(
    x, y_main,
    color="blue",
    marker="o",
    label="Traffico principale"
)

ax_main.set_title("Grafico principale")
ax_main.set_ylabel("Valore")
ax_main.legend()

# Inset: ingrandimento della zona del picco
ax_inset = ax_main.inset_axes([0.6, 0.5, 0.3, 0.3])

ax_inset.plot(
    x, y_main,
    color="blue",
    marker="o"
)

# Limiti dello zoom
ax_inset.set_xlim(9, 13)
ax_inset.set_ylim(65, 155)

# Evidenziamo il massimo con un punto rosso
ax_inset.plot(
    x[max_idx],
    y_main[max_idx],
    color="red",
    marker="o",
    markersize=10
)

ax_inset.set_title("Zoom del picco", fontsize=8)

# Grafico secondario a barre
ax_sub1 = fig.add_subplot(gs[1, 0])

ax_sub1.bar(
    x, y_sub1,
    color="orange",
    label="Sub1"
)

ax_sub1.set_title("Grafico secondario 1")
ax_sub1.legend()

# Grafico secondario a punti
ax_sub2 = fig.add_subplot(gs[1, 1])

ax_sub2.scatter(
    x, y_sub2,
    color="green",
    s=50,
    label="Sub2"
)

ax_sub2.set_title("Grafico secondario 2")
ax_sub2.legend()

plt.tight_layout()
plt.show()