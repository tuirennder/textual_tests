from textual.app import App, ComposeResult
from textual.widgets import Static


class VerticalLayoutExample(App):
    CSS_PATH = "vertical_layout.tcss"
    # The layout: vertical CSS isn't strictly necessary in this case, since Screens use a vertical layout by default.
    
    # You might also have noticed that the child widgets are the same width as the screen, despite nothing in our CSS file suggesting this. 
    # This is because widgets expand to the width of their parent container (in this case, the Screen).

    # We've assigned each child .box a height of 1fr, which ensures they're each allocated an equal portion of the available height.
    # Fr is a fractional unit and 1fr is for 1 part of the available space.

    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two", classes="box")
        yield Static("Three", classes="box")
        yield Static("Four", classes="box2")


if __name__ == "__main__":
    app = VerticalLayoutExample()
    app.run()
