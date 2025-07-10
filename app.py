import streamlit as st
import requests

# URL de ton API
API_URL = "https://apifastheroku-8bd7a41e1bb2.herokuapp.com/predict"

st.title("Prédicteur de tags")

# Champ de saisie
user_input = st.text_area("Entrez votre texte :", height=200)

# Bouton
if st.button("Prédire les tags"):
    if not user_input.strip():
        st.warning("Veuillez entrer un texte.")
    else:
        try:
            # Appel API
            response = requests.post(API_URL, json={"text": user_input})
            if response.status_code == 200:
                tags = response.json()
                st.success("Tags prédits :")
                st.write(tags)
            else:
                st.error(f"Erreur {response.status_code} : {response.text}")
        except Exception as e:
            st.error(f"Erreur de connexion à l'API : {e}")