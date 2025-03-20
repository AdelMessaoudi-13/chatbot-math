import json
import requests
from math_keywords import math_keywords  # Importation des mots-clés

# Définition du modèle à utiliser avec Ollama
model = 'mistral:7b'

# Prompt pour contraindre le modèle à répondre uniquement aux questions mathématiques
prompt_base = "Tu ne réponds qu'aux questions mathématiques."

# Fonction pour vérifier si une question est mathématique
def is_math_question(question):
    """
    Vérifie si la question posée concerne les mathématiques en utilisant une liste de mots-clés.
    Retourne True si c'est une question mathématique, sinon False.
    """
    return any(word in question.lower() for word in math_keywords)

import json
import requests

# Fonction qui envoie une requête à Ollama et affiche la réponse en streaming pour Gradio
def generate(user_input, context):
    """
    Envoie une requête à Ollama et retourne la réponse complète en texte.
    """
    full_prompt = f"{prompt_base}\n\nQuestion : {user_input}"

    r = requests.post(
        'http://localhost:11434/api/generate',  # URL de l'API locale d'Ollama
        json={'model': model, 'prompt': full_prompt, 'context': context, 'stream': False}  # Désactive le streaming
    )

    r.raise_for_status()  # Vérifie si la requête a réussi

    response_data = r.json()  # Convertir la réponse en JSON

    # Vérifier si la réponse contient bien du texte
    return response_data.get("response", "❌ Erreur : Réponse vide ou incorrecte.")
