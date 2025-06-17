
#pip install langchain langchain-ollama

from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

import speaker
#import listener as listener

s = speaker.Speaker(also_print=True)
#l = listener.Listener()

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def chat():
    context = ""
    print("Let's chat! (Type exit to quit):")
    while True:
        question = input("You: ")
        #question = l.listen()
        #print(f"You: {user_input}\n")
        if question.lower() == "exit":
            break

        answer = chain.invoke({"context": context,"question": question})
        print("Ollama:")
        s.speak(f"{answer}")
        context += f"\nUser: {question}\nAI: {answer}"

if __name__ == "__main__":
    chat()
