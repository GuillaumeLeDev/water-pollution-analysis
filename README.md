# Analyse pollution de l'eau

Ce projet analyse les données de pollution de l'eau et les maladies associées à l'aide de Python.

Lien vers la source du Dataset : https://www.kaggle.com/datasets/khushikyad001/water-pollution-and-disease

## Structure du projet

- data/ : Données sources
- src/ : Scripts Python d'analyse
- README.md : Présentation du projet
- requirements.txt : Librairies nécessaires



## ⚙️ Prérequis et installation

1. Cloner le dépôt :  
   ```bash
   git clone https://github.com/GuillaumeLeDev/water-pollution-analysis.git

cd water-pollution-analysis
pip install -r requirements.txt


## Execution

1.  Lancer le script d’analyse :
bash
python src/analyse.py

##  Résultats attendus 

    -Aperçu des données ( 5 premières lignes )
    -Moyenne du contaminant par région
    -Distribution des tupes de source d'eau
    -Corrélation contamination vs PIB par habitant

Exemple :

Moyenne du contaminant par région :
Region
East     2.34
North    3.12
South    1.87
West     2.45
Name: Contaminant Level (ppm), dtype: float64

Nombre de pays par type de source d'eau :
Well      45
Lake      30
River     25
Pond      10
Name: Water Source Type, dtype: int64

Corrélation contamination vs PIB par habitant : -0.12

