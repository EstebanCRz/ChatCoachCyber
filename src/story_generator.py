import ollama
from markdown import markdown

def generate_reponse(prompt, question):
    """Génère une réponse en streaming en corrigeant la réponse de l'utilisateur."""

    # Utiliser Ollama pour obtenir la réponse en streaming
    stream = ollama.chat(
        model='llama3.2',
        messages=[
            {'role': 'system', 'content': "Corrige ma réponse en 1 phrase résumé et en donnant la réponse courte sur la question et donne un rating sur 10 pour si j'ai eu une bonne réponse. voici la question : " + question},
            {'role': 'user', 'content': prompt}
        ],
        stream=True,
    )

    # Variable pour accumuler toute la réponse
    full_response = ""

    # Renvoyer chaque chunk de texte
    try:
        for chunk in stream:
            full_response += chunk['message']['content']  # Accumuler le texte dans full_response
            yield chunk['message']['content']  # Continuer à envoyer les chunks pour un affichage en temps réel

    except Exception as e:
        yield f"Erreur dans la génération de la réponse : {str(e)}\n\n"

def generate_question(prompt):
    """Génère une question en streaming à propos de la cybersécurité."""

    # Utiliser Ollama pour obtenir la réponse en streaming
    stream = ollama.chat(
        model='llama3.2',
        messages=[
            {'role': 'system', 'content': "Génère une question et seulement une question sur la cybersécurité, le réseaux ou les vulnérabilités."},
            {'role': 'user', 'content': "Génère moi une question en lien avec " + prompt}
        ],
        stream=True,
    )

    # Variable pour accumuler toute la question
    full_question = ""

    # Renvoyer chaque chunk de texte
    try:
        for chunk in stream:
            full_question += chunk['message']['content']  # Accumuler le texte dans full_question
            yield chunk['message']['content']  # Continuer à envoyer les chunks pour un affichage en temps réel

    except Exception as e:
        yield f"Erreur dans la génération de la question : {str(e)}\n\n"
