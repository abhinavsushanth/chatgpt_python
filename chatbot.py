import os
from dotenv import load_dotenv
import openai

def main():
    # Fetch key from .env file
    load_dotenv()
    api_key = os.environ.get("API_KEY")

    # Set API key for OpenAI
    openai.api_key = api_key

    # We have a role for each message, user or assistant (system is also present but rarely used)
    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     # messages=[{"role":"user", "content":"What is a horcrux in Harry Potter?"}]
    #     messages=[{"role":"user", "content":"Who is the founder of Disney?"}]
    # )

    # # print(completion)
    # reply_content = completion.choices[0].message.content
    # print(reply_content)

    # We need to pass history of chat everytime to the API (back n forth conversation)
    # Initialize message history
    message_history = []

    # Ask a question
    user_input = "User Input is " + "Who is the founder of Disney?"
    # message_history.append({"role":"user", "content":user_input})
    reply_content = chat_completion_create(message_history, user_input)

    # # Get the reply and append it to the message history
    # reply_content = completion.choices[0].message.content
    # message_history.append({"role":"assistant", "content":reply_content})

    # Ask another question
    user_input = "User Input is " + "When was he born?"
    # message_history.append({"role":"user", "content":user_input})
    reply_content = chat_completion_create(message_history, user_input)

    # Get the reply and append it to the message history
    # reply_content = completion.choices[0].message.content
    print(reply_content)


def chat_completion_create(message_history, content):
    message_history.append({"role":"user", "content":content})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    
    # Get the reply and append it to the message history
    reply_content = completion.choices[0].message.content
    message_history.append({"role":"assistant", "content":reply_content})
    
    return reply_content

if __name__ == "__main__":
    main()
