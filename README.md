# Proyecto Python: Análisis de Variabilidad Climática y Métricas de Dispersión con Pandas

Este repositorio contiene un proyecto práctico desarrollado en Python utilizando las librerías **Pandas** y **NumPy** enfocado en la auditoría y análisis estadístico descriptivo de un conjunto de datos climáticos masivo con más de 39,000 registros meteorológicos de la ciudad de Londres. El script implementa filtros indexados para aislar ventanas temporales específicas, calcula medidas de tendencia central y de dispersión global, y automatiza mediante estructuras iterativas la segmentación mensual para cuantificar la variabilidad y estabilidad térmica a lo largo del año.

---

## Código Python del Proyecto

El programa realiza la ingesta de las series cronológicas climáticas, calcula las variaciones térmicas globales y desglosa las desviaciones mensuales de forma iterativa:

```python
import pandas as pd
import numpy as np
from weather_data import london_data

# --- 1. Exploración Inicial del Dataset ---
print(london_data.head())
print("Volumen de registros meteorológicos analizados: " + str(len(london_data)))

# --- 2. Análisis Estadístico Descriptivo Global ---
temp = london_data["TemperatureC"]
average_temp = np.mean(temp)
temperature_var = np.var(temp)
temperature_std = np.std(temp)

print(f"Temperatura Media Global: {round(average_temp, 2)} °C")
print(f"Varianza Global: {round(temperature_var, 2)}")
print(f"Desviación Estándar Global: {round(temperature_std, 2)}")

# --- 3. Análisis Comparativo Estacional (Junio vs Julio) ---
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]

print("\n--- Métricas Estacionales Comparativas ---")
print("Temperatura media de Junio: " + str(round(np.mean(june), 2)) + " °C")
print("Temperatura media de Julio: " + str(round(np.mean(july), 2)) + " °C")
print("Desviación estándar de Junio: " + str(round(np.std(june), 2)))
print("Desviación estándar de Julio: " + str(round(np.std(july), 2)))

# --- 4. Pipeline de Automatización Mensual de Variabilidad ---
print("\n--- Desglose Mensual Automatizado (Ciclo Anual) ---")
for i in range(1, 13):
    month = london_data.loc[london_data["month"] == i]["TemperatureC"]
    mean_m = np.mean(month)
    std_m = np.std(month)
    print(f"Mes {i} -> Temperatura Media: {round(mean_m, 2)} °C | Desviación Estándar: {round(std_m, 2)}")

```

---

## Análisis y Hallazgos del Comportamiento Climático

El procesamiento de las variables térmicas permite extraer conclusiones analíticas directas sobre los patrones estacionales y la estabilidad meteorológica regional:

### 1. Dinámica Térmica de Verano (Junio vs Julio)

Al contrastar las series temporales de los meses centrales del verano europeo mediante concatenaciones y filtros, se observan los siguientes comportamientos en consola:

* **Temperatura Media:** Julio registra un promedio térmico superior en comparación con Junio, marcando el pico de la curva climática estacional.
* **Desviación Estándar (Dispersión):** Junio presenta una desviación estándar ligeramente mayor. En ciencia de datos, una mayor desviación estándar denota que los datos están más dispersos respecto a su media, lo que se traduce en un mes con mayor inestabilidad climática (días muy fríos intercalados con días muy cálidos), mientras que Julio muestra un comportamiento térmico más compacto y consistente.

### 2. Estructura de Control Iterativo Anual

El bucle recorre de forma secuencial las doce posiciones del calendario. La desviación estándar actúa como un **indicador de predictibilidad**: los meses invernales suelen registrar desviaciones elevadas debido al paso de frentes ciclónicos inestables, mientras que las estaciones de transición reflejan distribuciones más homogéneas.

---

## Conceptos Técnicos Aplicados

* **Desviación Estándar ($\sigma$) como Índice de Variabilidad**: Métrica que cuantifica el promedio de las desviaciones de los puntos de datos respecto a su media aritmética. En análisis climático, actúa como el indicador directo para medir la predictibilidad o volatilidad de un estado del tiempo.
* **Filtros Condicionales Indexados (`.loc[]`)**: Método de Pandas utilizado para acceder a un grupo de filas y columnas mediante etiquetas o vectores booleanos. Permite aislar registros atómicos basándose en criterios de segmentación numéricos (como `month == i`) de forma eficiente en memoria.
* **Optimización Analítica por Bucles**: El uso de un ciclo `for` parametrizado por el rango numérico de meses evita la redundancia de código (principio DRY), automatizando la extracción de porciones de datos y el cálculo de matrices de dispersión en una sola estructura lógica compacta.

