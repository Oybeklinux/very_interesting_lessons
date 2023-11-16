import openai

# OpenAI API mijozini sozlash
openai.api_key = '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'

# Model va so'rovni sozlash
model_engine = "text-davinci-003"
prompt = "Assalomu alaykum, qalaysiz?"

# So'rovga javob olishni (Response) hosil qilish
completion = openai.completions.create(
    model=model_engine,
    prompt=prompt,
    max_tokens=5,
    n=2,
    stop=None,
    temperature=0.5,
)

for choice in completion.choices:
    print(choice.text)
