from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Header
from textual.events import Key

class QuestionApp(App[str]):
    CSS_PATH = "css01.tcss"
    TITLE = "A Question App"
    SUB_TITLE = "The most important question"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Do you love Textual?", id="question")
        yield Button("Yes", id="yes", variant="primary")
        yield Button("No", id="no", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.log.debug(f"Pressed button with id {event.button.id}")
        self.exit(event.button.id)

    def on_key(self, event: Key):
        self.title = event.key
        self.sub_title = f"You just pressed {event.key}!"


if __name__ == "__main__":
    app = QuestionApp()
    reply = app.run()
    print(f"Pressed button with id {reply}")
