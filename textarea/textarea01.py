from textual.app import App, ComposeResult
from textual.widgets import TextArea, Header, Static, Button, RichLog
from textual.containers import Container, Horizontal
from textual.reactive import reactive
from textual.events import MouseEvent, Key
from textual import on

TEXT = """\
def hello(name):
    print("hello" + name)

def goodbye(name):
    print("goodbye" + name)
"""



class TextAreaExample(App):
    CSS_PATH = "textarea01.tcss"

    cursor_location = reactive((0, 0))
    content = reactive("")

    # Update the display of the cursor location when cursor_location is updated.
    def watch_cursor_location(self, old_cursor, new_cursor):
        self.log.debug(f"watch_cursor: {old_cursor} -> {new_cursor}")
        self.query_one(Static).update(
            f"Cursor location: {new_cursor}"
        )

    def watch_content(self, old_content, new_content):
        self.log.debug(f"watch_content: {old_content} -> {new_content}")
        self.query_one(RichLog).write(new_content)

    def compose(self) -> ComposeResult:
        yield Static("Cursor location: (0, 0)", id="cursor_location")
        yield TextArea(TEXT, language="python")
        yield RichLog(auto_scroll=True, highlight=True, markup=True)
        with Horizontal():
            yield Button("Read", id="read")
            yield Button("Goodbye")
    
    def on_mount(self):
        self.query_one(RichLog).write("...")

    def update_cursor_location(self, event):
        self.cursor_location = self.query_one(TextArea).cursor_location
        self.log.debug(f"on event {event}, cursor location {self.cursor_location}")

    def on_click(self, event: MouseEvent):
        self.update_cursor_location(event)

    # on_key will only catch non-printable keys, like the arrow keys.
    # For printable keys, use on_text_area_changed.
    def on_key(self, event: Key):
        self.update_cursor_location(event)

    def on_text_area_changed(self, event: TextArea.Changed):
        self.update_cursor_location(event)

    @on(Button.Pressed, "#read")
    def read(self):
        self.log.debug("Reading text area")
        self.content = self.query_one(TextArea).text


    
# supported languages:
# https://tree-sitter.github.io/tree-sitter/

app = TextAreaExample()
if __name__ == "__main__":
    app.run()

