import pandas as pd
datos = "https://github.com/Twoeme/Prueba2/raw/refs/heads/main/Supply_Food_Data_Descriptions.csv"
df = pd.read_csv(datos)
df.info()
