import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

print(london_data.head())
print(london_data.iloc[100:200])

print(len(london_data))

temp = london_data["TemperatureC"]
average_temp = np.mean(temp)
print(average_temp)

temperature_var = np.var(temp)
print(temperature_var)

temperature_standar_deviation = np.std(temp)
print(temperature_standar_deviation)

print(london_data.head())

june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
print(june)
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
print(july)

temp_mean = np.mean(pd.concat([june, july]))
print(temp_mean)
print("Temperatura media de Junio: " + str(np.mean(june)))
print("Temperatura media de Julio: " + str(np.mean(july)))

temp_std = np.std(pd.concat([june, july]))
print(temp_std)
print("Desviacion estandar de temperatura de Junio: " + str(np.std(june)))
print("Desviacion estandar de temperatura de Julio: " + str(np.std(july)))

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")


