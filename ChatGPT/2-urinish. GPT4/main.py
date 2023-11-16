import g4f

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking


def ask_gpt_35(prompt: str):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_long,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )

    for message in response:
        print(message, flush=True, end='')


def ask_gpt_4(prompt: str):
    # normal response
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": prompt}],
    )  # alternative model setting

    print(response)

# ask_gpt_35('write me python code that should find the middle value between 3 values')

# ask_gpt_35("""Bu kodda nima xato bor?
# print('Hello' + 3)""")

ask_gpt_4("""Menga ruslar haqida latifa gapirib ber""")
