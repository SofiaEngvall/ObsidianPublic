from ollama import chat, ChatResponse
import speaker

s = speaker.Speaker()

while True:
    user_input = input("\nYou: ")
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