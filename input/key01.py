from textual import events
from textual.app import App, ComposeResult
from textual.widgets import RichLog, Header


class InputApp(App):
    """App to display key events."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield RichLog()

    def on_key(self, event: events.Key) -> None:
        self.query_one(RichLog).write(event)

    def on_mount(self) -> None:
        self.sub_title = "Prints pretty prints the Key events received" # Will appear in the Header


if __name__ == "__main__":
    app = InputApp()
    app.run()
