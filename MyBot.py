import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
model = "gpt-4"

client = AzureOpenAI(api_key=api_key, api_version="2023-03-15-preview", azure_endpoint=endpoint)

def Chat_with_me(question):
    conversation = [{"role": "user", "content": question}, {"role": "system", "content": "I can answer your questions or follow your instructions."}]
    response = client.chat.completions.create(model=model, messages=conversation)
    return response.choices[0].message.content

while(True):
    question = str(input("Ask: "))
    if question.lower() == 'bye':
        print("Bye...have a nice day")
        break
    print(f"Bot: {(Chat_with_me(question))}")