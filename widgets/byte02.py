from __future__ import annotations

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Input, Label, Switch

"""
Messages up
https://textual.textualize.io/guide/widgets/#data-flow

Let's extend the ByteEditor so that clicking any of the 8 BitSwitch widgets updates 
the decimal value. To do this we will add a custom message to BitSwitch that we catch in the ByteEditor.
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
            self.bit = bit # This will store the "bit" number (0-7)
            self.value = value # This will store the value 0 or 1 of the "bit".

    value = reactive(0) # This will store the value 0 or 1 of the "bit". 

    def __init__(self, bit: int) -> None:
        self.bit = bit
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label(str(self.bit))
        yield Switch()

    def on_switch_changed(self, event: Switch.Changed) -> None:  
        """When the switch changes, notify the parent via a message."""
        event.stop() # Stop the event, because we don't want it to go to the parent.
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

    def compose(self) -> ComposeResult:
        with Container(classes="top"):
            yield Input(placeholder="byte")
        with Container():
            yield ByteInput()

    # This will be called when the BitSwitch sends a BitChanged message.
    def on_bit_switch_bit_changed(self, event: BitSwitch.BitChanged) -> None:
        """When a switch changes, update the value."""
        value = 0
        for switch in self.query(BitSwitch): # Query all the BitSwitch widgets.
            value |= switch.value << switch.bit 
        self.query_one(Input).value = str(value) # Update the Input widget. str(value) converts the value to a string.


"""
The `|=` operator is a shorthand for a bitwise OR operation combined with assignment. 
It's equivalent to `value = value | (switch.value << switch.bit)`. 

The `<<` operator is a bitwise shift left operation. 
It shifts the bits of `switch.value` to the left by the number of positions specified by `switch.bit`. 

Here's a step-by-step breakdown of what this line of code does:

1. `switch.value << switch.bit`: This part of the code shifts the bits of `switch.value` to the left by `switch.bit`
positions. For example, if `switch.value` is `2` (which is `10` in binary) and `switch.bit` is `1`, then the result would be `4` (which is `100` in binary).

2. `value |= ...`: This part of the code performs a bitwise OR operation on `value` and the result 
of the shift operation, and then assigns the result back to `value`. 
The bitwise OR operation compares each bit of `value` and the result of the shift operation, 
and if either bit is `1`, then the corresponding result bit is set to `1`.

"""


class ByteInputApp(App):
    def compose(self) -> ComposeResult:
        yield ByteEditor()


if __name__ == "__main__":
    app = ByteInputApp()
    app.run()
