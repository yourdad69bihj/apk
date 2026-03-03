from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class JordanApp(App):
    def build(self):
        # Setting the "Purple Elite" Theme
        Window.clearcolor = (0.1, 0, 0.2, 1) # Dark Purple Background
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Label with Neon Purple text
        self.lbl = Label(
            text="JORDAN'S ELITE V1", 
            font_size='32sp', 
            color=(0.7, 0, 1, 1), 
            bold=True
        )
        
        # A Big Purple Button
        btn = Button(
            text="CLICK TO ACTIVATE", 
            background_color=(0.5, 0, 0.8, 1), 
            font_size='20sp'
        )
        
        # When you click the button, change the text
        btn.bind(on_press=self.on_click)
        
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def on_click(self, instance):
        self.lbl.text = "SYSTEM ACTIVE"
        self.lbl.color = (0, 1, 0, 1) # Turns Green

if __name__ == "__main__":
    JordanApp().run()