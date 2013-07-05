import sublime, sublime_plugin
from sublime import Window

from time import time;

options = [
	"Quit Now!",
	"Close View",
	"Close Window",
	"Cancel",
]

commands = {
	"Quit Now!": "exit",
	"Close View": "close",
	"Close Window": "close_window"
}

class QuitGuardCommand(sublime_plugin.TextCommand):
	def on_done(self, idx):
		option = options[idx]

		if option in commands:
			self.view.window().run_command(commands[option])

	def run(self, edit):
		window = self.view.window()
		window.show_quick_panel(options, self.on_done)
