from textual.app import App, ComposeResult
from textual.widgets import Static

TEXT = """
[b]Set your background[/b]
[@click=set_background('red')]Red[/]
[@click=set_background('green')]Green[/]
[@click=set_background('blue')]Blue[/]
"""

"""
Actions may be embedded as links within console markup. You can create such links with a @click tag.

https://textual.textualize.io/guide/actions/#links
"""

class ActionsApp(App):
    def compose(self) -> ComposeResult:
        yield Static(TEXT)

    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color


if __name__ == "__main__":
    app = ActionsApp()
    app.run()
