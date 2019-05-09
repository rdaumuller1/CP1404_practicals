from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicKivyWidgetsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.status_text = "{}'s number is {}".format(name, self.name_to_phone[name])
        self.names = ["Amy", "Ben", "Cara", "Danny"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "My Dynamic Widgets"
        self.root = Builder.load_file('dynamic_kivy_widgets.kv')
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.labels_box.add_widget(temp_label)

        # id: labels_box
        # self.create_widgets()
        return self.root


DynamicKivyWidgetsApp().run()
