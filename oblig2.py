import numpy as np
import matplotlib.pyplot as plt

# Funksjonen
def f(x):
    return np.exp(-x / 4) * np.arctan(x)

# Likningen som bestemmer toppunktet
def g(x):
    return np.arctan(x) - 4 / (x**2 + 1)

# Derivert av g(x)
def g_derivert(x):
    return 1 / (x**2 + 1) + (8 * x) / (x**2 + 1)**2

# Newtons metode
x = 1.5  # startverdi

for i in range(10):
    x = x - g(x) / g_derivert(x)

x_topp = x
y_topp = f(x_topp)

print(f"Toppunktets x-verdi: {x_topp:.10f}")
print(f"Toppunktets y-verdi: {y_topp:.10f}")
print(f"Toppunkt med fire desimaler: ({x_topp:.4f}, {y_topp:.4f})")

# Plott funksjonen
x_vals = np.linspace(-4, 8, 1000)
y_vals = f(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=r"$f(x)=e^{-x/4}\arctan(x)$")
plt.plot(x_topp, y_topp, 'ro', label="Toppunkt")
plt.annotate(f"({x_topp:.4f}, {y_topp:.4f})",
             (x_topp, y_topp),
             textcoords="offset points",
             xytext=(10, 10))

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title(r"Plot av $f(x)=e^{-x/4}\arctan(x)$")
plt.grid(True)
plt.legend()
plt.savefig("oblig2_plot.png", dpi=150)
plt.show()