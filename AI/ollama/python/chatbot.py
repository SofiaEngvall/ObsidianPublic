#!/usr/bin/env python3

# chatbot.py - RSS feed reader with AI summarization
# version 1.0
# by Sofia Engvall - FixIt42, 2025-05-04
# https://github.com/SofiaEngvall/RSS-Read-Aloud-Cyber-News-Reader.git

from ollama import chat, ChatResponse
import speaker
import AI.ollama.python.listener as listener

s = speaker.Speaker()
l = listener.Listener()

while True:
    #user_input = input("\nYou: ")
    user_input = l.listen()
    print(f"You: {user_input}\n")

    if user_input.lower() == "exit":
        break
    response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': user_input,
        },
    ])
    print("\nAI:", response.message.content)
    s.speak(response.message.content)
    