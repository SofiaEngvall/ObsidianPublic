from ollama import chat, ChatResponse
import speaker
import listener

s = speaker.Speaker()
l = listener.Listener()

while True:
    user_input = input("\nYou: ")
    #user_input = l.listen()
    #print(f"You: {user_input}\n")

    if user_input.lower() == "exit":
        break
    response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': user_input,
        },
    ])
    print("\nAI:", response.message.content)
    #s.speak(response.message.content)
    