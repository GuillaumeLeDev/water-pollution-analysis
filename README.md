# 💧 Analyse simplifiée de la pollution de l'eau

Ce projet Streamlit analyse un ensemble de données mondial sur la qualité de l'eau et la santé publique. Il propose une interface claire et interactive pour visualiser des indicateurs clés environnementaux, sanitaires et socio-économiques.


Ce projet analyse les données de pollution de l'eau et les maladies associées à l'aide de Python.

Lien vers la source du Dataset : https://www.kaggle.com/datasets/khushikyad001/water-pollution-and-disease

## 📁 Structure du projet


- data/ : Données sources
- src/ : Scripts Python d'analyse
- README.md : Présentation du projet
- requirements.txt : Librairies nécessaires
- archive/ : première essaie de projet sans streamlit

## 🎯 Objectifs

- Centraliser des données liées à la pollution de l'eau et leur impact.
- Calculer un indice WQI (Water Quality Index) simplifié.
- Permettre une interprétation visuelle rapide grâce à des graphiques pertinents.
- Offrir une navigation accessible aux utilisateurs non techniques.

---

## 🧰 Technologies utilisées

- `Python 3.11+`
- `Streamlit`
- `pandas`
- `matplotlib`
- `seaborn`

---

## 📊 Fonctionnalités de l'application

### ✅ Indicateurs clés affichés
- Niveau moyen de contaminants (ppm)
- Taux d'accès à l'eau potable (% population)
- Taux de mortalité infantile
- Indice global de qualité de l'eau (WQI)

### 📍 Graphiques interactifs
- **Qualité moyenne de l’eau par région (WQI)** – avec régions traduites en français
- **Évolution du niveau de contaminants dans le temps**
- **Évolution de l'indice WQI dans le temps**
- **Corrélation entre le PIB par habitant et la pollution**
- **Répartition des sources d'eau**

---

## 🧠 Calcul du WQI simplifié

L’indice WQI est basé sur les 5 critères OMS les plus pertinents :

| Paramètre                   | Seuil OMS utilisé    |
|----------------------------|----------------------|
| pH                         | 6.5 – 8.5            |
| Turbidité                  | ≤ 5 NTU              |
| Oxygène dissous            | ≥ 6 mg/L             |
| Nitrate                    | ≤ 10 mg/L            |
| Plomb                      | ≤ 10 µg/L            |

Chaque critère est noté sur 100, puis une moyenne est calculée.

---

---

## ▶️ Lancer l’application localement

```bash
pip install -r requirements.txt
streamlit run app.py


##  À venir (pistes d'amélioration)
Filtres dynamiques par région ou pays

Ajout de seuils OMS sur les graphiques

Génération d’un rapport PDF automatique

