# 🤖 Chatbot Mathématique - Version Gradio 🤖

Un chatbot intelligent qui utilise un **LLM en local** grâce à **Ollama** et au modèle **Mistral 7B**, avec une **interface web Gradio** pour une utilisation plus intuitive.

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
   cd chatbot-math/gradio_version
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

1. Lancez le programme avec `python main.py`.
2. Ouvrez votre navigateur et accédez à l'URL affichée (exemple : `http://127.0.0.1:7860`).
3. Posez votre question mathématique et obtenez une réponse instantanée via l'interface web.

## 🛠 Technologies utilisées
- **Python 3.x**
- **Gradio** (Interface web interactive)
- **Ollama** (Exécution locale des modèles LLM)
- **Mistral 7B** (Modèle de langage utilisé)

## 🤝 Contribuer
Les contributions sont bienvenues !

## 📧 Contact
📩 amessaoudi.am@gmail.com
🌍 https://github.com/AdelMessaoudi-13
