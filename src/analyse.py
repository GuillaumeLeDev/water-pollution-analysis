import pandas as pd

# Charger les données
df = pd.read_csv(r'F:\Documents\GitHub\Water-Pollution-analysis\data\water_pollution_disease.csv')



# Voir les premières lignes
print("Aperçu des données :")
print(df.head())

# Connaitre les colonnes
print("\nColonnes disponibles :")
print(df.columns)
