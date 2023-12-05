from textual.app import App
from textual.widgets import Welcome, Button
from textual import events


class WelcomeApp(App):
    async def on_key(self, event: events.Key) -> None:
        self.log.debug(f"key {event.key} pressed")
        await self.mount(Welcome())   # Must wait for mount before searching for the Button 
        # Error otherwise: 
        # NoMatches: No nodes match <DOMQuery query='Button'>
        self.query_one(Button).label = "YES!"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.log.debug(f"button with label {event.button.label} pressed")
        self.exit()


if __name__ == "__main__":
    app = WelcomeApp()
    app.run()
