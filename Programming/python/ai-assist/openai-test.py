import openai

openai.api_key = open("OPENAI_API_KEY").read()

text = "How do I add a task using googles calendar api and python?"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": text}
    ])

print(completion.choices[0].message.content)
