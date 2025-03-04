# mosfet-ptype-simulatior
Este script simula la relación ID-VDS en un MOSFET para distintos VGS, usando ecuaciones fundamentales para calcular la capacitancia del óxido, movilidad, voltaje de umbral y corriente. Permite modificar parámetros como dopaje, espesor del óxido y movilidad. Incluye gráficos de referencia para selección de valores.

Requisitos

Este script requiere las siguientes bibliotecas de Python:

numpy para los cálculos matemáticos.

matplotlib para la generación de gráficos.

Se pueden instalar ejecutando:

pip install numpy matplotlib

Funcionamiento

El script define tres funciones principales:

calcular_k(mu0, T, ε0, εr, tox): Calcula la constante k del MOSFET a partir de la movilidad del portador y la capacitancia del óxido.

calcular_vt(Φm, Φs, Qss, Na, ni, tox, εox, εs): Calcula el voltaje de umbral (Vt) a partir de parámetros físicos y el dopaje del semiconductor.

calcular_id(vgs, vds, kp, W, L, Vt, lambda_): Calcula la corriente ID para un MOSFET según el modelo de la ecuación cuadrática.


El usuario puede modificar los siguientes parámetros:

W: Ancho del canal del MOSFET.

L: Largo del canal del MOSFET.

tox: Espesor del óxido.

mu0: Movilidad del portador en condiciones normales.

Na: Concentración de dopaje.

Φm, Φs: Funciones de trabajo del metal y del semiconductor.

Qss: Carga superficial.

T: Temperatura del sistema.

λ: Coeficiente de modulación del canal.

Referencias Gráficas

Para la correcta selección de los valores de entrada en la simulación, se incluyen las siguientes imágenes de referencia:

Movilidad vs. Concentración de impurezas:

Esta gráfica muestra la relación entre la movilidad del portador y la concentración de impurezas para distintos materiales semiconductores (Silicio, Germanio y Arseniuro de Galio) a 300K.

Permite seleccionar un valor de mu0 acorde al material y nivel de dopaje utilizado en la simulación.



Función de trabajo de distintos materiales:

Esta tabla gráfica presenta los valores típicos de la función de trabajo para distintos materiales.

Es útil para seleccionar Φm y Φs de acuerdo con los materiales usados en la compuerta y el semiconductor.



Uso

Se establecen los valores de los parámetros físicos del MOSFET.

Se calculan la constante kp y el voltaje de umbral Vt.

Se generan valores de VDS entre 0 y 2 V y se evalúa ID para distintos VGS.

Se grafica ID vs. VDS mostrando las curvas características del MOSFET.

Resultado

El script genera una gráfica donde se observa la variación de ID en función de VDS para diferentes valores de VGS, permitiendo visualizar el comportamiento del MOSFET en sus distintas regiones de operación.

Aplicaciones

Este código es útil para:

Entender el funcionamiento de un MOSFET y sus ecuaciones fundamentales.

Simular curvas de corriente en un MOSFET con diferentes condiciones.

Comparar resultados experimentales con simulaciones teóricas.

Autor

Este código fue desarrollado como parte de un proyecto para la simulación del comportamiento de transistores MOSFET en Python.

