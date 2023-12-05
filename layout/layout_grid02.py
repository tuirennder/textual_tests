from textual.app import App, ComposeResult
from textual.widgets import Static, Header


class GridLayoutExample(App):
    CSS_PATH = "layout_grid02.tcss"

    def compose(self) -> ComposeResult:
        yield Header(id="header")
        yield Static("One", classes="box")
        yield Static("Two [b](column-span: 2 and row-span: 2)", classes="box", id="two")
        yield Static("Three", classes="box")
        yield Static("Four", classes="box")
        yield Static("Five", classes="box")
        yield Static("Six", classes="box")


app = GridLayoutExample()
if __name__ == "__main__":
    app.run()

