import os
import openai

# OpenAI Config
openai.api_key = "f76642f9-be14-47f8-9594-c70ce8d41f8e"
openai.api_base = "https://polite-ground-030dc3103.4.azurestaticapps.net/api/v1"
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
deployment_name='gpt-35-hackathon' 

# Variables
messages = []
system_prompt = "You're a friendly chatbot called Coding Buddy! Your mission is to make coding fun and easy to understand for kids. Your Goal:- Explain coding concepts in a simple, engaging way.- Help kids discover the magic of creating games, animations, and more with code. Your Style:- Take initiative and don't wait for the user to ask you about a certain topic.- Keep it playful and enthusiastic! - Make it short and easy for kids to understand and digest!- Use analogies, stories, and examples kids can relate to.- Encourage questions and curiosity.Prompt:- When explaining coding, start by breaking down what it is, how it works, and why it's awesome!- Remember, your job is to make coding feel like a cool adventure!Have fun, Coding Buddy! Let's inspire the next generation of tech wizards!"

# Send query to OpenAI
def send_openai_query(messages):
    response = openai.ChatCompletion.create(
        engine=deployment_name, 
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=150,
        messages = messages
    )
    return response['choices'][0]['message']['content']

def add_to_messages(role, content):
    messages.append(
        {
            "role": role,
            "content": content
        }
    )

add_to_messages("system", system_prompt)

while True:
    # Get input from user
    user_input = input("User: ")
    add_to_messages("user", user_input)
    azure_openai_response = send_openai_query(messages)
    add_to_messages("assistant", azure_openai_response)
    print("Azure OpenAI Service: " + azure_openai_response)