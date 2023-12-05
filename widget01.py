from textual.app import App, ComposeResult
from textual.widgets import Welcome, Button

"""
To add widgets to your app implement a compose() method which should return an iterable of Widget instances. 
A list would work, but it is convenient to yield widgets, making the method a generator.
"""

class WelcomeApp(App[str]):
    def compose(self) -> ComposeResult:
        self.log.debug("compose yields a Welcome widget")
        yield Welcome()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.log.debug(f"button with label {event.button.label} pressed")
        self.exit(event.button.label)


if __name__ == "__main__":
    app = WelcomeApp()
    result = app.run()
    print(f"Pressed button \"{result}\"")

