import sublime, sublime_plugin
from sublime import Window

from time import time;

class QuitGuardCommand(sublime_plugin.TextCommand):
	def on_done(self, idx):
		if idx == 1:
			self.view.window().run_command("exit")

	def run(self, edit):
		window = self.view.window()
		window.show_quick_panel(["Cancel", "Quit Now!"], self.on_done)
