import pandas as pd

# Charger les données
df = pd.read_csv(r'F:\Documents\GitHub\Water-Pollution-analysis\data\water_pollution_disease.csv')



# Voir les premières lignes
print("Aperçu des données :")
print(df.head())

# Connaitre les colonnes
print("\nColonnes disponibles :")
print(df.columns)

# 4. Moyenne du contaminant par région
print("\nMoyenne du contaminant par région :")
moy_region = df.groupby('Region')['Contaminant Level (ppm)'].mean()
print(moy_region)

# 5. Distribution des types de source d'eau
print("\nNombre de pays par type de source d'eau :")
dist_sources = df['Water Source Type'].value_counts()
print(dist_sources)

# 6. Corrélation entre contamination et PIB par habitant
corr = df['Contaminant Level (ppm)'].corr(df['GDP per Capita (USD)'])
print(f"\nCorrélation contamination vs PIB par habitant : {corr:.2f}")
