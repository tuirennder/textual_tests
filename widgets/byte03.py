from __future__ import annotations

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.geometry import clamp
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Input, Label, Switch

"""
Attributes down
https://textual.textualize.io/guide/widgets/#attributes-down

We also want the switches to update if the user edits the decimal value.

Since the switches are children of ByteEditor we can update them by setting their attributes directly. 
This is an example of "attributes down".
"""

class BitSwitch(Widget):
    """A Switch with a numeric label above it."""

    DEFAULT_CSS = """
    BitSwitch {
        layout: vertical;
        width: auto;
        height: auto;
    }
    BitSwitch > Label {
        text-align: center;
        width: 100%;
    }
    """

    class BitChanged(Message):
        """Sent when the 'bit' changes."""

        def __init__(self, bit: int, value: bool) -> None:
            super().__init__()
            self.bit = bit
            self.value = value

    value = reactive(0)

    def __init__(self, bit: int) -> None:
        self.bit = bit
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label(str(self.bit))
        yield Switch()

    # If the value has been changed by the parent, Textual will call watch_value which sets 
    # the value of each of the eight switches. 
    # Because we are working with children of the ByteEditor, we can set attributes directly without going via a message.

    def watch_value(self, value: bool) -> None:  
        """When the value changes we want to set the switch accordingly."""
        self.query_one(Switch).value = value

    def on_switch_changed(self, event: Switch.Changed) -> None:
        """When the switch changes, notify the parent via a message."""
        event.stop()
        self.value = event.value
        self.post_message(self.BitChanged(self.bit, event.value))


class ByteInput(Widget):
    """A compound widget with 8 switches."""

    DEFAULT_CSS = """
    ByteInput {
        width: auto;
        height: auto;
        border: blank;
        layout: horizontal;
    }
    ByteInput:focus-within {
        border: heavy $secondary;
    }
    """

    def compose(self) -> ComposeResult:
        for bit in reversed(range(8)):
            yield BitSwitch(bit)


class ByteEditor(Widget):
    DEFAULT_CSS = """
    ByteEditor > Container {
        height: 1fr;
        align: center middle;
    }
    ByteEditor > Container.top {
        background: $boost;
    }
    ByteEditor Input {
        width: 16;
    }
    """

    value = reactive(0)

    # Called when the reactive value changes.
    def validate_value(self, value: int) -> int:  
        """Ensure value is between 0 and 255."""
        return clamp(value, 0, 255)

    def compose(self) -> ComposeResult:
        with Container(classes="top"):
            yield Input(placeholder="byte")
        with Container():
            yield ByteInput()

    def on_bit_switch_bit_changed(self, event: BitSwitch.BitChanged) -> None:
        """When a switch changes, update the value."""
        value = 0
        for switch in self.query(BitSwitch):
            value |= switch.value << switch.bit
        self.query_one(Input).value = str(value)

    def on_input_changed(self, event: Input.Changed) -> None:  
        """When the text changes, set the value of the byte."""
        try:
            self.value = int(event.value or "0") # If the value is empty, set it to 0.
        except ValueError:
            pass

    def watch_value(self, value: int) -> None:  
        """When self.value changes, update switches."""
        for switch in self.query(BitSwitch):
            with switch.prevent(BitSwitch.BitChanged): # Prevent the BitChanged message from being sent.
                switch.value = bool(value & (1 << switch.bit)) 
"""
Here's a step-by-step breakdown of what this line of code does:

1. `1 << switch.bit`: This part of the code shifts the bits of `1` to the left by `switch.bit` positions. 
For example, if `switch.bit` is `1`, then the result would be `2` (which is `10` in binary).

2. `value & ...`: This part of the code performs a bitwise AND operation on `value` and the result of the shift operation. 
For example, if `value` is `3` (which is `11` in binary) and the result of the shift operation 
is `2` (which is `10` in binary), then the result would be `2` (which is `10` in binary), 
because the second bit is `1` in both `value` and the result of the shift operation.

3. `switch.value = bool(...)`: This part of the code converts the result of the bitwise AND operation 
to a boolean value and assigns it to `switch.value`. If the result of the bitwise AND operation is `0`, 
then `switch.value` will be `False`. Otherwise, `switch.value` will be `True`.

"""

class ByteInputApp(App):
    def compose(self) -> ComposeResult:
        yield ByteEditor()


if __name__ == "__main__":
    app = ByteInputApp()
    app.run()
