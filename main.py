from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.label = Label(text='Chào mừng đến với App Android bằng Python!', font_size=18, halign='center')
        btn = Button(text='Bấm vào đây', size_hint=(1, 0.3), background_color=(1, 0, 0, 1))
        btn.bind(on_press=self.on_button_click)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_button_click(self, instance):
        self.label.text = 'Bạn đã bấm nút thành công!'

if __name__ == '__main__':
    MyApp().run()
