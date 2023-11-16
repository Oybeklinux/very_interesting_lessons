import openai

openai.api_key = ""

model_engine = "text-davinci-003"
prompt = "Hello, how are you"

completion = openai.completions.create(
    model=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

response = completion.choices[0].text
print(response)