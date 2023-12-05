from textual.app import App, ComposeResult
from textual.widgets import Static


class HorizontalLayoutExample(App):
    CSS_PATH = "horizontal_layout.tcss"

    # widgets expand to fill the width of their parent container. 
    # They do not, however, expand to fill the container's height. 
    # Thus, we need explicitly assign height: 100% to achieve this.

    # A consequence of this "horizontal growth" behaviour is that if we remove the width restriction from the above example (by deleting width: 1fr;), 
    # each child widget will grow to fit the width of the screen, and only the first widget will be visible. The other two widgets in our layout are offscreen, 
    # to the right-hand side of the screen. In the case of horizontal layout, Textual will not automatically add a scrollbar.

    # To enable horizontal scrolling, we can use the "overflow-x: auto;"" declaration in the tcss screen section.
    
    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two", classes="box")
        yield Static("Three", classes="box")


if __name__ == "__main__":
    app = HorizontalLayoutExample()
    app.run()
