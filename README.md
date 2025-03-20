# 🤖 Chatbot Mathématique 🤖

Un chatbot intelligent qui utilise un **LLM en local** grâce à **Ollama** et au modèle **Mistral 7B**, avec deux versions :
- **📟 Version Terminale** : Pour une utilisation en ligne de commande.
- **🌐 Version Gradio** : Avec une interface web interactive.

## 🚀 Installation et Utilisation
### 1️⃣ **Version Terminale** (CLI)

💡 **Cette version est plus rapide car elle ne charge pas d'interface graphique.**

1. **Installer Ollama** :
   Ollama est nécessaire pour exécuter le modèle Mistral. Installez-le depuis [Ollama](https://ollama.com).

2. **Télécharger et préparer le modèle Mistral** :
   ```bash
   ollama pull mistral:7b
   ```

3. **Cloner le projet** :
   ```bash
   git clone https://github.com/AdelMessaoudi-13/chatbot-math
   cd chatbot-math/terminal_version
   ```

4. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

5. **Lancer le chatbot** :
   ```bash
   python main.py
   ```

📌 **Pour plus de détails**, consultez le [README de la version terminale](terminal_version/README.md).

---

### 2️⃣ **Version Gradio** (Interface Web)

1. **Installer Ollama** :
   ```bash
   ollama pull mistral:7b
   ```

2. **Cloner le projet** :
   ```bash
   git clone https://github.com/AdelMessaoudi-13/chatbot-math
   cd chatbot-math/gradio_version
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer le chatbot** :
   ```bash
   python main.py
   ```

5. **Accéder à l'interface** :
   - Ouvrez votre navigateur et accédez à l'URL affichée (exemple : `http://127.0.0.1:7860`).
   - Posez vos questions et obtenez une réponse instantanée.

📌 **Pour plus de détails**, consultez le [README de la version Gradio](gradio_version/README.md).

---

## 📌 Fonctionnalités
✔️ Répond aux questions mathématiques grâce à un LLM local.
✔️ Deux modes disponibles : **Terminal** et **Gradio (Web UI)**.
✔️ Ne nécessite pas d’API externe : **fonctionne 100% en local**.
✔️ Utilise **Mistral 7B**et peut être configuré avec d'autres modèles disponibles sur [Ollama](https://ollama.com/library).

---

## 🛠 Technologies utilisées
- **Python 3.x**
- **Gradio** (Version Web UI)
- **Ollama** (Exécution locale des modèles LLM)
- **Mistral 7B** (Modèle de langage utilisé)

---

## 🤝 Contribuer
Les contributions sont bienvenues ! Si vous souhaitez proposer des améliorations, n’hésitez pas à ouvrir une *issue* ou une *pull request*.

---

## 📧 Contact
📩 amessaoudi.am@gmail.com
🌍 https://github.com/AdelMessaoudi-13
