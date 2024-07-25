import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Analyse et Nettoyage de Données avec Streamlit")

# Charger le fichier CSV
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

if uploaded_file is not None:
    # Lire les données
    df = pd.read_csv(uploaded_file)
    
    # Afficher les premières lignes du DataFrame
    st.write("### Premières lignes du DataFrame")
    st.write(df.head())
    
    # Informations générales sur l'ensemble de données
    st.write("### Informations générales")
    buffer = pd.io.formats.format.DataFrameFormatter(df).buf
    st.text(buffer.getvalue())
    
    # Statistiques descriptives
    st.write("### Statistiques descriptives")
    st.write(df.describe())




    
    

