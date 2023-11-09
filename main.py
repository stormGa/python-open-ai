from openai import OpenAI
import toml

config = toml.load("config.toml")
open_key = config["openai"]["key"]
print(type(open_key))
client = OpenAI(api_key=open_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)