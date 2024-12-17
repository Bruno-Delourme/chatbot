import openai

# Configuration de la cle API
openai.api_key = ".../api"

def chatbot():
    print("Bienvenue dans l'application IA! Posez une question ou tapez 'exit' pour quitter.")

    while True:
        # Demander une entrée utilisateur
        user_input = input("Vous: ")

        # Vérification si l'utilisateur veut quitter
        if user_input.lower() == "exit":
            print("Au revoir!")
            break

        # Envoie la question à l'API OpenAI et obtient une réponse
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # "text-davinci-003 a venir"
                prompt=user_input,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.7,
            )

            # Affiche la réponse
            answer = response.choices[0].text.strip()
            print(f"IA: {answer}")

        except Exception as e:
            print(f"Une erreur est survenue: {e}")

if __name__ == "__main__":
    chatbot()
