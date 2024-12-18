import openai
from dotenv import load_dotenv
import os

# Chargement de la clé API depuis un fichier .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
    print("Bienvenue dans l'application IA! Posez une question ou tapez 'exit' pour quitter.")
    
    # Initialisation de l'historique
    conversation_history = []

    while True:
        user_input = input("Vous: ")

        if user_input.lower() == "exit":
            print("Au revoir!")
            break

        try:
            # Ajout du message utilisateur à l'historique
            conversation_history.append({"role": "user", "content": user_input})

            # Utilisation de l'API ChatCompletion
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation_history,
                max_tokens=150,
                n=1,
                temperature=0.7,
            )

            # Récupération et affichage de la réponse
            answer = response.choices[0].message.content
            print(f"IA: {answer}")

            # Ajout de la réponse à l'historique
            conversation_history.append({"role": "assistant", "content": answer})

        except openai.error.RateLimitError:
            print("Erreur: Limite de requêtes API atteinte. Veuillez patienter.")
        except openai.error.AuthenticationError:
            print("Erreur: Problème d'authentification avec l'API OpenAI.")
        except Exception as e:
            print(f"Une erreur inattendue est survenue: {e}")

if __name__ == "__main__":
    chatbot()
