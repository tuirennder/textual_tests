from textual.app import App
from textual.widgets import Welcome, Button
from textual import events

"""
Mount a Welcome widget
Exits on button pressed
"""

class WelcomeApp(App):
    def on_key(self, event: events.Key) -> None:
        self.log.debug(f"key {event.key} pressed")
        self.mount(Welcome())

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.log.debug(f"button with label {event.button.label} pressed")
        self.exit()


if __name__ == "__main__":
    app = WelcomeApp()
    app.run()
