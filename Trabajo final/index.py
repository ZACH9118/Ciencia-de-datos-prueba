import pandas as pd
datos = "https://github.com/ZACH9118/Ciencia-de-datos-prueba/raw/refs/heads/main/layoffs.csv"
df = pd.read_csv(datos)
df.info()
