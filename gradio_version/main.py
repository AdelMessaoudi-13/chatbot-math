import gradio as gr
from chatbot import is_math_question, generate

# Fonction pour gérer l'interaction avec Gradio
def chatbot_interface(user_input):
    if not is_math_question(user_input):
        return "🚫❌⛔️ Je ne peux répondre qu'aux questions mathématiques. Essaie une autre question."

    # Générer la réponse avec Ollama
    response = generate(user_input, [])
    return response

# Interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Bienvenue sur le Chatbot Mathématiques !")
    user_input = gr.Textbox(label="Pose-moi une question en mathématiques")
    output_text = gr.Textbox(label="Réponse du chatbot")
    submit_button = gr.Button("Envoyer")

    submit_button.click(chatbot_interface, inputs=user_input, outputs=output_text)

demo.launch()
