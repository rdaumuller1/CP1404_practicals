
from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETRES = 1.60934


class KilometreMilesConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('kilomtere_miles_converter.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


KilometreMilesConverter().run()
