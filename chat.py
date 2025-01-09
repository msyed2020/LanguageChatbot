print("Chat wassup")

import openai

openai.api_key = "" # gotta get this lol

def chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Sei un chatbot che parla solo italiano. Aiuta gli utenti con le loro domande in italiano."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
