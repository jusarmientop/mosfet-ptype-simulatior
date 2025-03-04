import numpy as np
import matplotlib.pyplot as plt

def calcular_k(mu0, T, ε0, εr, tox):
    Cox = (ε0 * εr) / tox  # Capacitancia del óxido
    mu = mu0 * (T / 300) ** 2  # Movilidad del portador
    return mu * Cox  # Cálculo de k

def calcular_vt(Φm, Φs, Qss, Na, ni, tox, εox, εs, q=1.6e-19, k=1.38e-23, T=300):
    Vt_thermal = (k * T) / q  # Voltaje térmico
    Φms = Φm - Φs  # Diferencia de trabajo de función
    Vfb = Φms - (Qss / (εox / tox))  # Tensión de banda plana
    Φf = Vt_thermal * np.log(Na / ni)  # Potencial de Fermi
    QSD = np.sqrt(2 * q * εs * Na * 2 * Φf)  # Carga de la región de agotamiento
    Cox = εox / tox  # Capacitancia del óxido
    Vt = Vfb + 2 * Φf + (QSD + Qss) / Cox  # Voltaje de umbral
    return Vt

def calcular_id(vgs, vds, kp, W, L, Vt, lambda_):
    if vgs < Vt:
        return 0  # Región de corte
    elif vgs > Vt and vds < (vgs - Vt):
        return kp * (W / L) * ((vgs - Vt) * vds - (vds ** 2) / 2)  # Región lineal
    else:
        return 0.5*kp * (W / L) * ((vgs - Vt) ** 2) * (1 + lambda_ * vds)  # Región de saturación

# Parámetros físicos
ε0 = 8.85e-12  # Permitividad del vacío (F/m)
εr = 3.9  # Permitividad relativa del óxido
mu0 = 600e-4  # Movilidad del portador en condiciones normales (m^2/Vs)
T = 298.15  # Temperatura (K)

# Parámetros del MOSFET
W = 10e-6   # Ancho del canal (m)
L = 1e-6    # Largo del canal (m)
lambda_ = 0.02  # Coeficiente de modulación de canal

# Parámetros para el cálculo de Vt
Φm = 4.1  # Función de trabajo del metal (V)
Φs = 4.05  # Función de trabajo del semiconductor (V)
Qss = 1e-8  # Carga superficial (C/m^2)
Na = 1e22  # Concentración de dopaje (m^-3)
ni = 1.5e16  # Concentración intrínseca (m^-3)
tox = 5e-9  # Espesor del óxido (m)
εox = ε0 * εr  # Permitividad del óxido (F/m)
εs = 1.05e-10  # Permitividad del semiconductor (F/m)

# Cálculo de k y Vt
kp = calcular_k(mu0, T, ε0, εr, tox)
Vt = calcular_vt(Φm, Φs, Qss, Na, ni, tox, εox, εs)

# Rango de voltajes
VDS_vals = np.linspace(0, 2, 100)
VGS_vals = [1.2, 1.5]  # Diferentes valores de VGS

plt.figure(figsize=(8, 6))

for VGS in VGS_vals:
    ID_vals = [calcular_id(VGS, VDS, kp, W, L, Vt, lambda_) for VDS in VDS_vals]
    plt.plot(VDS_vals, ID_vals, label=f'VGS = {VGS} V')

plt.xlabel("VDS (V)")
plt.ylabel("ID (A)")
plt.title("Curva ID vs VDS para diferentes VGS")
plt.legend()
plt.grid()
plt.show()
