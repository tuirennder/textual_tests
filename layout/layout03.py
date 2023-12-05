from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static


class UtilityContainersExample(App):
    CSS_PATH = "utility_containers.tcss"

    # When composing a widget, you can introduce a container using Python's with statement. 
    # Any widgets yielded within that block are added as a child of the container.

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(classes="column"):
                yield Static("One")
                yield Static("Two")
            with Vertical(classes="column"):
                yield Static("Three")
                yield Static("Four")


if __name__ == "__main__":
    app = UtilityContainersExample()
    app.run()
