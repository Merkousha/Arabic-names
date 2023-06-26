import openai   
openai.api_key = "your gpt api key"


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": "type this name in arabic:"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)