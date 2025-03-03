import json
import requests
from math_keywords import math_keywords  # Importation des mots-clés

# Définition du modèle à utiliser avec Ollama
model = 'mistral:7b'

# Fonction pour vérifier si une question est mathématique
def is_math_question(question):
    """
    Vérifie si la question posée concerne les mathématiques en utilisant une liste améliorée de mots-clés.
    Retourne True si c'est une question mathématique, sinon False.
    """
    # Vérifier si un des mots-clés est présent dans la question
    return any(word in question.lower() for word in math_keywords)

# Fonction qui envoie une requête à Ollama et affiche la réponse en streaming
def generate(user_input, context):
    """
    Envoie une requête à Ollama avec le message de l'utilisateur et un contexte.
    Affiche la réponse en temps réel et retourne le contexte mis à jour.
    """

    # Envoi d'une requête POST à Ollama avec le modèle, le prompt et le contexte
    r = requests.post(
        'http://localhost:11434/api/generate',  # URL de l'API locale d'Ollama
        json={'model': model, 'prompt': user_input, 'context': context},  # Données envoyées
        stream=True  # Active le mode streaming pour recevoir la réponse progressivement
    )

    r.raise_for_status()  # Vérifie si la requête a réussi (sinon, déclenche une erreur)

    # Lecture progressive de la réponse (streaming)
    response_text = ""  # Stocke la réponse complète

    for line in r.iter_lines():
        # Décodage de la ligne en texte UTF-8 puis conversion JSON → dictionnaire Python
        body = json.loads(line.decode('utf-8'))

        # Récupération de la partie réponse générée par Ollama (ou chaîne vide si absente)
        response_part = body.get('response', '')

        # Affichage progressif du texte généré
        if response_part:
            print(response_part, end='', flush=True)  # Affichage immédiat sans retour à la ligne
            response_text += response_part

        # Gestion des erreurs (si la réponse contient une clé "error")
        if 'error' in body:
            raise Exception(body['error'])  # Arrête le programme et affiche l'erreur

        # Vérifie si Ollama a fini d'envoyer la réponse
        if body.get('done', False):  # False par défaut si "done" n'est pas présent
            return body['context']  # Retourne le contexte mis à jour
