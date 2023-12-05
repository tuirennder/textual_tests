from textual.app import App, ComposeResult
from textual.color import Color
from textual.message import Message
from textual.widgets import Static
from rich.console import RenderableType

class ColorButton(Static):
    """A color button."""

    class Selected(Message):
        """Color selected message."""

        def __init__(self, color: Color) -> None:
            self.color = color
            super().__init__()

    def __init__(self, color: Color, tag: RenderableType) -> None:
        self.log.debug(f"instantiate button {tag}")
        self.color = color
        super().__init__(renderable=tag, name=f"super Static color {color}")

    def on_mount(self) -> None:
        self.log.debug(f"ColorButton widget loaded: color {self.color}")
        self.styles.margin = (1, 2)
        self.styles.content_align = ("center", "middle")
        self.styles.background = Color.parse("#ffffff33")
        self.styles.border = ("tall", self.color)

    def on_click(self) -> None:
        # The post_message method sends an event to be handled in the DOM
        self.log.debug(f"Button {self.name} clicked. Sending message {self.Selected(self.color)}")
        self.post_message(self.Selected(self.color))

    # Comment this out to let the super Static class do the render
    # def render(self) -> str:
    #     return str(self.color)


class ColorApp(App):
    def compose(self) -> ComposeResult:
        yield ColorButton(Color.parse("#008080"), f"Custom Button color 1")
        yield ColorButton(Color.parse("#808000"), f"Custom Button color 2")
        yield ColorButton(Color.parse("#E9967A"), f"Custom Button color 3")
        yield ColorButton(Color.parse("#121212"), f"Custom Button color 4")

    def on_color_button_selected(self, message: ColorButton.Selected) -> None:
        self.screen.styles.animate("background", message.color, duration=0.5)


if __name__ == "__main__":
    app = ColorApp()
    app.run()
