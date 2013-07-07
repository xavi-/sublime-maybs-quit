import sublime_plugin


class QuitGuardCommand(sublime_plugin.TextCommand):

	OPTIONS = (
		('Quit Now!', 'exit', ),
		('Close View', 'close', ),
		('Close Window', 'close_window', ),
		('Save as...', 'prompt_save_as', ),
		('Cancel', None, ),
	)

	OPTIONS_NAMES = tuple((opt[0] for opt in OPTIONS))

	def run(self, edit):
		self.view.window().show_quick_panel(self.OPTIONS_NAMES, self.on_done)

	def on_done(self, idx):
		option, command = self.OPTIONS[idx]

		if command:
			self.view.window().run_command(command)
