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

# Fonction qui envoie une requête à Ollama et affiche la réponse en streaming
def generate(user_input, context):
    """
    Envoie une requête à Ollama avec le message de l'utilisateur et un contexte.
    Affiche la réponse en temps réel et retourne le contexte mis à jour.
    """
    full_prompt = f"{prompt_base}\n\nQuestion : {user_input}"

    r = requests.post(
        'http://localhost:11434/api/generate',  # URL de l'API locale d'Ollama
        json={'model': model, 'prompt': full_prompt, 'context': context},  # Données envoyées
        stream=True  # Active le mode streaming pour recevoir la réponse progressivement
    )

    r.raise_for_status()  # Vérifie si la requête a réussi (sinon, déclenche une erreur)

    response_text = ""  # Stocke la réponse complète

    for line in r.iter_lines():
        body = json.loads(line.decode('utf-8'))
        response_part = body.get('response', '')

        if response_part:
            print(response_part, end='', flush=True)
            response_text += response_part

        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):
            return body['context']

from chatbot import is_math_question, generate

# Fonction principale qui gère l'interaction utilisateur
def main():
    """
    Boucle principale du chatbot :
    - Demande une entrée à l'utilisateur
    - Envoie la requête à Ollama
    - Affiche la réponse et met à jour le contexte
    """
    context = []  # Liste pour stocker l'historique de la conversation
    print("🤖 Bienvenue sur le Chatbot Mathématiques ! Pose-moi une question en maths ou tape 'exit' pour quitter.")

    while True:
        user_input = input("\nPose une question en maths (ou 'exit' pour quitter) : ")

        if user_input.lower() == 'exit':
            print("\n👋 Fermeture du chatbot. À bientôt !")
            break

        if not is_math_question(user_input):
            print("🚫❌⛔️ Je suis un chatbot spécialisé en mathématiques. Pose-moi une question en maths !")
            continue

        print()
        context = generate(user_input, context)

if __name__ == "__main__":
    main()
