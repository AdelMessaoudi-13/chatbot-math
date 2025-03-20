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
    print("🤖 Bienvenue sur le Chatbot Mathématiques ! Pose-moi une question en mathématiques ou tape 'exit' pour quitter.")

    while True:  # Boucle infinie pour continuer la conversation
        # Demande à l'utilisateur d'entrer un message
        user_input = input("\nPose une question en mathématiques (ou 'exit' pour quitter) : ")

        # Vérifie si l'utilisateur veut quitter
        if user_input.lower() == 'exit':
            print("\n👋 Fermeture du chatbot. À bientôt !")
            break  # Sort de la boucle et termine le programme

        # Vérifie si c'est une question mathématique
        if not is_math_question(user_input):
            print("🚫❌⛔️ Je suis un chatbot spécialisé en mathématiques. Pose-moi une question en maths !")
            continue  # Ignore cette entrée et redemande une question

        print()  # Ajoute une ligne vide pour une meilleure lisibilité

        # Appelle la fonction generate() et met à jour le contexte
        context = generate(user_input, context)

# Exécute la fonction main() uniquement si ce fichier est lancé directement
if __name__ == "__main__":
    main()
