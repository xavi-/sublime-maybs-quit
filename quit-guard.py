import sublime, sublime_plugin
from sublime import Window

from time import time;

class QuitGuardCommand(sublime_plugin.TextCommand):
	lastQuitCommand = -1

	def run(self, edit):
		now = time()

		if now - QuitGuardCommand.lastQuitCommand > 2:
			QuitGuardCommand.lastQuitCommand = now
		else:
			self.view.window().run_command("exit")
