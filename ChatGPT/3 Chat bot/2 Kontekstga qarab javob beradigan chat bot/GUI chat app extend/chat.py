import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from openai import OpenAI
import pickle


class ChatApp(App):
    def build(self):
        self.messages = []
        self.title = "Kivy Chat App"
        Window.size = (400, 500)

        # Layout
        self.layout = BoxLayout(orientation='vertical')

        # Display messages
        self.message_label = TextInput(multiline=True, size_hint_y=0.9)
        self.layout.add_widget(self.message_label)

        # Input field
        self.message_input = TextInput(size_hint_y=0.1, multiline=False)
        self.layout.add_widget(self.message_input)

        # Send button
        send_button = Button(text="Send", size_hint_y=0.1)
        send_button.bind(on_press=self.send_message)
        self.layout.add_widget(send_button)
        self.load_history()
        self.train()
        return self.layout

    def train(self):
        self.messages.extend([
            {"role": "system", "content": "Assalomu alaykum, hush kelibsiz. NextGen IT Academy sizni eshitadi. Sizga qanday yordam bersam bo'ladi"},
            {"role": "user", "content": "Sizlarda qanday kurslar bor?"},
            {"role": "system", "content": "Bizda hozirda Python, Javascript, Flutter va Php bo'yicha kurslarimiz bor"},
            {"role": "user", "content": "Menga Python kursi haqida ma'lumot bera olasizmi?"},
            {"role": "system", "content": "Python kursi 7 oy o'rgatiladi. Kursimiz narxi 1.8 mln."},
            {"role": "user", "content": "Dars vaqtlari va kunlari?"},
            {"role": "system", "content": "Dars vaqti va kunlari mijozlar bilan kelishgan holda belgilanadi"},
            {"role": "user", "content": "Ayollarga chegirma bormi?"},
            {"role": "system", "content": "Ha ayollarga 20% chegirma bor"},
            {"role": "user", "content": "O'quv markaz nomi nima?"},
            {"role": "system", "content": "NextGen IT Academy"},
            {"role": "user", "content": "U qayerda joylashgan?"},
            {"role": "system", "content": "IT park hududi Aloqabank binosi 16-qavatda joylashgan"}]
        )
    def load_history(self):
        if os.path.exists("data.pkl"):
            # Deserialize the object from the binary file
            with open('data.pkl', 'rb') as file:
                self.messages = pickle.load(file)
        msg = ''
        i = 0
        for message in self.messages:
            i += 1
            msg += f"\n{message['role']}: {message['content']}"
            if i % 2 == 0:
                msg += '\n'
        self.message_label.text = msg.strip()

        print(self.messages)

    def __del__(self):
        self.save_history()

    def save_history(self):
        print("Saving history ... ")
        # Serialize the object to a binary format
        with open('data.pkl', 'wb') as file:
            pickle.dump(self.messages, file)

    def send_system_message(self, prompt):
        message = self.get_chatGPT_message(prompt)
        self.message_label.text += f'\nChatGPT: {message}'

    def send_message(self, instance):
        message = self.message_input.text
        if message:
            current_text = self.message_label.text
            self.message_label.text = f'{current_text}\n\nYou: {message}'
            self.message_input.text = ''
        self.send_system_message(message)

    def get_chatGPT_message(self, prompt):
        client = OpenAI(api_key="OPENAI_API_KEY=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")
        self.messages.append({"role": "user", "content": prompt})
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )

        response = completion.choices[0].message.content
        self.messages.append({"role": "system", "content": response})
        return response


if __name__ == '__main__':
    ChatApp().run()
