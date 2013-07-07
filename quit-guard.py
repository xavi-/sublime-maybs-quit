import sublime, sublime_plugin
from sublime import Window

options = [
    "Quit Now!",
    "Close View",
    "Close Window",
    "Save as...",
    "Cancel"
]

commands = {
    "Quit Now!": "exit",
    "Close View": "close",
    "Close Window": "close_window",
    "Save as...": "prompt_save_as"
}

class QuitGuardCommand(sublime_plugin.TextCommand):
    def on_done(self, idx):
        option = options[idx]

        if option in commands:
            self.view.window().run_command(commands[option])

    def run(self, edit):
        window = self.view.window()
        window.show_quick_panel(options, self.on_done)
