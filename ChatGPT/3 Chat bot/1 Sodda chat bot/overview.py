from openai import OpenAI

# Kalitni olish: https://platform.openai.com/api-keys
# OpenAI API mijoz kalitini sozlash
#
client = OpenAI(api_key="OPENAI_API_KEY=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")

# Model va so'rovni sozlash
prompt = "My name is Oybek"
model_engine = "gpt-3.5-turbo"

# So'rovga javob olish/hosil qilish
completion = client.chat.completions.create(
    model=model_engine,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# natijani hammasini ekranga chiqarish
print(completion)
print('===========')

# natijadan faqat matnni ekranga chiqarish
print(completion.choices[0].message.content)
