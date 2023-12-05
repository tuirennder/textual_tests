from textual.app import App, ComposeResult
from textual.widgets import Static


class GridLayoutExample(App):
    CSS = """
    Screen {
        layout: grid;
        grid-size: 3;
        grid-columns: 2fr 1fr 1fr;
        grid-rows: 25% 75%;
    }

    .box {
        height: 100%;
        border: solid green;
    }
    """

    # The grid-columns and grid-rows rules can both accept a value of "auto" in place of any of the dimensions, 
    # which tells Textual to calculate an optimal size based on the content.

    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two", classes="box")
        yield Static("Three", classes="box")
        yield Static("Four", classes="box")
        yield Static("Five", classes="box")
        yield Static("Six", classes="box")


if __name__ == "__main__":
    app = GridLayoutExample()
    app.run()
