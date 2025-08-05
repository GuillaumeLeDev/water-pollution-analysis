import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration de la page
st.set_page_config(page_title="Pollution de l'eau - Analyse", layout="centered")
st.title("💧 Pollution de l'eau : Analyse simplifiée")

# Chargement des données
df = pd.read_csv("data/water_pollution_disease.csv")

# --------- Indicateurs clés ---------
st.subheader("🔢 Indicateurs clés")
col1, col2, col3 = st.columns(3)
col1.metric("Niveau moyen de contaminants", f"{df['Contaminant Level (ppm)'].mean():.2f} ppm")
st.markdown("""
<small>
**ℹ️ ppm = partie par million** (1 mg/L) – une unité qui permet de mesurer la concentration très faible d’un contaminant dans l’eau potable.

**Seuils recommandés :**
- OMS : ≤ **10 ppm** pour les nitrates
- Arsenic : ≤ **0,01 ppm** (10 µg/L)
- Esthétique (TDS) : ≤ **500 ppm**

> Au-delà de ces seuils, la consommation d’eau peut représenter un risque pour la santé (surtout pour les nourrissons, femmes enceintes ou populations fragiles).
</small>
""", unsafe_allow_html=True)

col2.metric("Accès à l'eau potable", f"{df['Access to Clean Water (% of Population)'].mean():.1f}%")
col3.metric("Mortalité infantile", f"{df['Infant Mortality Rate (per 1,000 live births)'].mean():.1f} ‰")

# --------- Pollution moyenne par région ---------
st.subheader("🌍 Pollution moyenne par région")
fig1, ax1 = plt.subplots()
moyenne = df.groupby("Region")["Contaminant Level (ppm)"].mean().sort_values()
sns.barplot(x=moyenne.values, y=moyenne.index, ax=ax1, color="royalblue")
ax1.set_xlabel("ppm")
ax1.set_ylabel("Région")
ax1.set_title("Contamination moyenne par région", fontsize=12)
st.pyplot(fig1)

# --------- Évolution dans le temps ---------
st.subheader("⏰ Évolution du niveau de contaminants")
fig2, ax2 = plt.subplots()
annee = df.groupby("Year")["Contaminant Level (ppm)"].mean()
ax2.plot(annee.index, annee.values, marker="o", color="darkblue")
ax2.set_ylabel("ppm")
ax2.set_xlabel("Année")
ax2.set_title("Niveau moyen de contamination dans le temps")
st.pyplot(fig2)

# --------- Corrélation PIB vs pollution ---------
st.subheader("📈 Corrélation PIB et pollution")
fig3, ax3 = plt.subplots()
sns.scatterplot(data=df, x="GDP per Capita (USD)", y="Contaminant Level (ppm)", ax=ax3)
ax3.set_title("Plus le PIB est élevé, moins l'eau est contaminée ?")
st.pyplot(fig3)

# --------- Sources d'eau ---------
st.subheader("🚧 Sources d'eau les plus fréquentes")
sources = df["Water Source Type"].value_counts()
st.bar_chart(sources)
