import requests
from flask import Flask, render_template, request, Response
from story_generator import generate_reponse, generate_question

app = Flask(__name__)

# État de la session
session_state = {
    'question_number': 0,  # Nombre de questions posées
    'current_topic': "",  # Sujet actuel choisi par l'utilisateur
    'current_question': "",  # Question actuelle
    'user_answer': None,  # Réponse de l'utilisateur
}

# Liste des thèmes pour les bonnes pratiques et les risques
topics = {
    "good_practices": [
        "Les mots de passe",
        "La sécurité sur les réseaux sociaux",
        "La sécurité des appareils mobiles",
        "Les sauvegardes",
        "Les mises à jour",
        "La sécurité des usages pro-perso"
    ],
    "risks": [
        "L'hameçonnage",
        "Les rançongiciels",
        "L'arnaque au faux support technique"
    ]
}

@app.route('/')
def index():
    # Affiche l'état initial du jeu avec les thèmes
    return render_template("index1.html", topics=topics)

@app.route('/action', methods=['GET'])
def action():
    action = request.args.get('action', '')  # Récupérer l'action ou réponse de l'utilisateur
    topic = request.args.get('topic', '')  # Récupérer le sujet choisi par l'utilisateur

    # Si un sujet est choisi et c'est la première question, mettre à jour le sujet
    if topic and session_state['question_number'] == 0:
        session_state['current_topic'] = topic
        session_state['question_number'] = 1  # On commence la première question

    # Si aucune action n'a été fournie, retour d'erreur
    if not action.strip() and session_state['question_number'] > 0:
        return Response("Aucune action n'a été fournie.", status=400)


    # Fonction pour générer la question et la réponse
    def generate():
        try:
            # Si aucune question n'a encore été posée ou si l'utilisateur a répondu
            if session_state['current_question'] == "" or session_state['user_answer'] is not None:
                if session_state['user_answer'] is None:  # Génération de la question initiale
                    session_state['current_question'] = ""
                    for chunk in generate_question(session_state['current_topic']):
                        session_state['current_question'] += chunk
                    session_state['user_answer'] = session_state['current_question']
                    # Envoie la question complète
                    yield f"data: {session_state['current_question']}\n\n"
                else:  # L'utilisateur a répondu, génération de la correction
                    correction = ""
                    for chunk in generate_reponse(session_state['user_answer'], session_state['current_question']):
                        correction += chunk
                    # Envoie la réponse complète
                    yield f"data: {correction}\n\n"
                    session_state['user_answer'] = None
                    # Réinitialiser pour la prochaine question
                    session_state['current_question'] = ""
                    session_state['question_number'] += 1  # Passe à la question suivante
                    yield f"data: [Prêt pour une nouvelle question]\n\n"

        except Exception as e:
            yield f"data: Erreur de traitement : {str(e)}\n\n"

    return Response(generate(), content_type='text/event-stream')


if __name__ == "__main__":
    app.run(debug=True)
