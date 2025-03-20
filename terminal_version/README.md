# 🤖 Chatbot Mathématique - Version Terminal 🤖

Un chatbot intelligent qui utilise un **LLM en local** grâce à **Ollama** et au modèle **Mistral 7B** pour répondre aux questions mathématiques.

## 🚀 Installation
1. **Installer Ollama** :
   Ollama est nécessaire pour exécuter le modèle Mistral. Installez-le depuis [Ollama](https://ollama.com).

2. **Télécharger et préparer le modèle Mistral** :
   ```bash
   ollama pull mistral:7b
   ```

3. **Cloner le projet** :
   ```bash
   git clone https://github.com/AdelMessaoudi-13/chatbot-math
   cd chatbot-math
   ```

4. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

5. **Lancer le chatbot** :
- **Windows et Linux**
   ```bash
   python main.py
   ```
- **Mac**
   ```bash
   python3 main.py
   ```

## 📸 Exemple d'utilisation
```
🤖 Bienvenue sur le Chatbot Mathématiques ! Pose-moi une question en maths ou tape 'exit' pour quitter.

Pose une question en maths : Quelle est la dérivée de x^2 ?
📢 La dérivée de x^2 est 2x.
```

## 🛠 Technologies utilisées
- **Python 3.x**
- **Ollama** (Permet d'exécuter n'importe quel modèle de langage sur une machine locale)
- **Mistral 7B** (Modèle LLM utilisé)

## 🤝 Contribuer
Les contributions sont bienvenues !

## 📧 Contact
📩 amessaoudi.am@gmail.com
🌍 https://github.com/AdelMessaoudi-13
