from kivy.app import App
from kivy.uix.label import Label

class DaftarYarApp(App):
    def build(self):
        return Label(text="دفتر یار - مدیریت منابع انسانی", font_size=24)

if __name__ == '__main__':
    DaftarYarApp().run()
