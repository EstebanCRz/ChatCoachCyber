# Entrainement Cybersécurité - Chatbot enseignant

Bienvenue dans le projet "d'entrainement de cybersécurité" où vous explorez un divers mode de cyber et pourrais en apprendre plus grâce à un chatbot pour vous corriger et poser des questions.  
N'oubliez pas que le projet tourne en local pour fonctionner hors connexion, mais cela implique certaines lenteurs dans le modèle, alors soyez patient lors de la génération du texte.

## Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Exécution](#exécution)
- [Utilisation](#utilisation)
- [Technologies utilisées](#technologies-utilisées)
- [Contribuer](#contribuer)

## Prérequis

Avant de commencer l'installation, assurez-vous d'avoir les outils suivants installés sur votre machine :

1. **Python 3.12+** : Vous pouvez télécharger Python [ici](https://www.python.org/downloads/).
2. **Pip** : Le gestionnaire de packages Python pour installer les dépendances.

## Installation

1. Installer le LLM :
   1. Installer [Ollama](https://ollama.com/) pour Windows ou Mac.
   2. Inclure Ollama dans le PATH.
2. Installer les dépendances et lancer le projet :
```bash
pip install -r requirements.txt
ollama run llama3.2
```

4. Lancer le serveur Flask :
```bash
python app.py
```

## Exécution
Une fois le serveur Flask lancé, vous pouvez ouvrir un navigateur et accéder à l'adresse suivante :

```http
   http://127.0.0.1:5000/
```

Vous pourrez commencer à interagir avec le chatbot dans un monde fantastique, générant des histoires et des images en fonction de vos actions.

## Limitations
N'oubliez pas que le code tourne en local, ce qui peut entraîner des temps de réponse plus lents, notamment lors de la génération du texte. Soyez patient !

## Utilisation
Une fois l'application en cours d'exécution, vous serez invité à saisir des actions dans un champ de texte. Il suffit d'écrire un message pour lancer le chatbot.

## Technologies utilisées
- Flask : Un micro-framework Python pour créer l'application web.
- LLama : Un modèle de langage pour générer des questions, noter et répondre à l'utilisateur.
- HTML/CSS/JavaScript : Pour l'interface utilisateur et l'affichage dynamique des messages.
