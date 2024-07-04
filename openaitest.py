from openai import OpenAI

OpenAIapiKey = "your api key"

client = OpenAI(api_key=OpenAIapiKey)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Write an email to wish happy birthday"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)