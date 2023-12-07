from textual import events
from textual.app import App


class ActionsApp(App):
    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color

    async def on_key(self, event: events.Key) -> None:
        if event.key == "r":
            await self.run_action("set_background('red')")
"""
Note that the run_action() method is a coroutine 
so on_key needs to be prefixed with the async keyword.
"""

if __name__ == "__main__":
    app = ActionsApp()
    app.run()
