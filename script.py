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
