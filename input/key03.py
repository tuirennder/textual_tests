from textual import events
from textual.app import App, ComposeResult
from textual.widgets import RichLog

"""
Demo of input focus, blur events; mouse enter, leave events

Border colors set in TCSS by :hover and :focus
"""

class KeyLogger(RichLog):
    def on_key(self, event: events.Key) -> None:
        self.write(event)

    def on_focus(self, event: events.Focus) -> None:
        self.write(f"Widget {self.id} on focus")
    
    def on_blur(self, event: events.Blur) -> None:
        self.write(f"Widget {self.id} out of focus")
    
    def on_enter(self, event: events.Enter) -> None:
        self.write(f"Mouse entered {self.id}")

    def on_leave(self, event: events.Leave) -> None:
        self.write(f"Mouse left {self.id}")


class InputApp(App):
    """App to display key events."""

    CSS_PATH = "key03.tcss"

    def compose(self) -> ComposeResult:
        yield KeyLogger(id="widget 1")
        yield KeyLogger(id="widget 2")
        yield KeyLogger(id="widget 3")
        yield KeyLogger(id="widget 4")


if __name__ == "__main__":
    app = InputApp()
    app.run()
