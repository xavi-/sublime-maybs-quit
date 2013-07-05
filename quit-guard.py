import sublime, sublime_plugin
from sublime import Window

from time import time;

QUIT = "Quit Now!"
CLOSE_VIEW = "Close View"
CLOSE_WINDOW = "Close Window"
CANCEL = "Cancel"

options = [
	QUIT,
	CLOSE_VIEW,
	CLOSE_WINDOW,
	CANCEL
]

class QuitGuardCommand(sublime_plugin.TextCommand):
	def on_done(self, idx):
		option = options[idx]

		if option == CANCEL and idx < 0:
			pass
		elif option == QUIT:
			self.view.window().run_command("exit")
		elif option == CLOSE_WINDOW:
			self.view.window().run_command("close_window")
		elif option == CLOSE_VIEW:
			self.view.window().run_command("close")

	def run(self, edit):
		window = self.view.window()
		window.show_quick_panel(options, self.on_done)
