from textual.app import App
from textual import events


class EventApp(App):

    COLORS = [
        "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "olive",
        "yellow",
        "navy",
        "teal",
        "aqua",
    ]

    """
    Event handlers are methods prefixed with on_ followed by the name of the event.

    Ref: https://textual.textualize.io/events/

    Format:
    Even 'MouseMove' is handled by 'on_mouse_move' method
    https://textual.textualize.io/guide/events/#message-handlers

    Tip to get the name:
    >>> from textual.widgets import Input
    >>> Input.Changed.handler_name
    'on_input_changed'
    """

    def on_mount(self, event: events.Mount) -> None:
        self.log.debug(f"on_mount() event {event}")
        self.screen.styles.background = "darkblue"

    def on_key(self, event: events.Key) -> None:
        self.log.debug(f"event.key {event.key}")
        if event.key.isdecimal():
            self.screen.styles.background = self.COLORS[int(event.key)]

    def on_mouse_move(self, event:events.MouseMove):
        self.log.debug(f"on mouse event (X {event.screen_x}, Y {event.screen_y})")


if __name__ == "__main__":
    app = EventApp()
    app.run()
