# import (structure given handily by OpenAI)
from openai import OpenAI

# allowing the user to give a prompt and update parameters
prompt = str(input("Enter your prompt please:"))
temp = float(input("Specify your temperature:"))
token = int(input("Specify the max tokens:"))
top = float(input("Speficy your top_p:"))

# read the API key which is hidden in my local enviornment
client = OpenAI()

# call the gpt-4o model with the user parameters
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=temp, # good default is 1.0
    max_tokens=token, # good default is 2048
    top_p=top, # good default is 1.0
)

# print the result for display in the terminal
print(response.choices[0].message.content)