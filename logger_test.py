from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual import log # instance of Logger

"""
In another terminal, start the console:
textual console -x EVENT -x SYSTEM

start the script with:
textual run --dev logger_test.py
"""

class ExampleApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        log.debug("debug log example")
        log.logging("logging log example")
        self.log("self default log level example")
        log(locals())  # Log local variables
        log(children=self.children, pi=3.141592)  # key/values
        log(self.tree)  # Rich renderables


if __name__ == "__main__":
    app = ExampleApp()
    app.run()


"""
Output:

──────────────────────────────────────────── Client '127.0.0.1' connected ────────────────────────────────────────────
[18:33:41] DEBUG                                                                                     logger_test.py:18
debug log example
[18:33:41] LOGGING                                                                                   logger_test.py:19
logging log example
[18:33:41] INFO                                                                                      logger_test.py:20
self default log level example
[18:33:41] INFO                                                                                      logger_test.py:21
{'self': ExampleApp(title='ExampleApp', classes={'-dark-mode'})}
[18:33:41] INFO                                                                                      logger_test.py:22
children=(Screen(id='_default'),) pi=3.141592
[18:33:41] INFO                                                                                      logger_test.py:23
ExampleApp(title='ExampleApp', classes={'-dark-mode'})
└── Screen(id='_default')
"""