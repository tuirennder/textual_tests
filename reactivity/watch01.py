from textual.app import App, ComposeResult
from textual.color import Color, ColorParseError
from textual.containers import Grid
from textual.reactive import reactive
from textual.widgets import Input, Static


class WatchApp(App):
    CSS_PATH = "watch01.tcss"

    color = reactive(Color.parse("transparent"))  

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter a color")
        yield Grid(Static(id="old"), Static(id="new"), id="colors")

    # Called when the reactive attribute color is changing
    # The old and new colors are passed as arguments
    # https://textual.textualize.io/guide/reactivity/#watch-methods
    
    # Textual only calls watch methods if the value of a reactive attribute changes. 
    # If the newly assigned value is the same as the previous value, the watch method is not called. 
    # You can override this behaviour by passing always_update=True to reactive.

    def watch_color(self, old_color: Color, new_color: Color) -> None:  
        self.query_one("#old").styles.background = old_color
        self.query_one("#new").styles.background = new_color

    def on_input_submitted(self, event: Input.Submitted) -> None:
        try:
            input_color = Color.parse(event.value)
        except ColorParseError:
            pass
        else:
            self.query_one(Input).value = ""
            self.color = input_color  


if __name__ == "__main__":
    app = WatchApp()
    app.run()
