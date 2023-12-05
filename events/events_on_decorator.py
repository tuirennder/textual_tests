from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


"""
The on decorator takes a CSS selector in addition to the event type which will be used to select which controls the handler should work with. 
We can use this to write a handler per control rather than manage them all in a single handler.

https://textual.textualize.io/guide/events/#on-decorator
"""

class OnDecoratorApp(App):
    CSS_PATH = "events_on_decorator.tcss"

    def compose(self) -> ComposeResult:
        """Three buttons."""
        yield Button("Bell", id="bell")
        yield Button("Toggle dark", classes="toggle dark")
        yield Button("Quit", id="quit")

    @on(Button.Pressed, "#bell")  
    def play_bell(self):
        """Called when the bell button is pressed."""
        self.bell()

    @on(Button.Pressed, ".toggle.dark")  
    def toggle_dark(self):
        """Called when the 'toggle dark' button is pressed."""
        self.dark = not self.dark

    @on(Button.Pressed, "#quit")  
    def quit(self):
        """Called when the quit button is pressed."""
        self.exit()


if __name__ == "__main__":
    app = OnDecoratorApp()
    app.run()
