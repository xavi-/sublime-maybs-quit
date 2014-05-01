import sublime_plugin

class QuitGuardCommand(sublime_plugin.TextCommand):

	OPTIONS = (
		('Quit Now!', 'exit', ),
		('Close View', 'close', ),
		('Close Window', 'close_window', ),
		('Close Project', 'close_project'),
		('Save as...', 'prompt_save_as', ),
		('Cancel', None, ),
	)

	OPTION_NAMES = [ opt[0] for opt in OPTIONS ]

	def run(self, edit):
		self.view.window().show_quick_panel(self.OPTION_NAMES, self.on_done)

	def on_done(self, idx):
		option, command = self.OPTIONS[idx]

		if command:
			self.view.window().run_command(command)

class CloseGuardCommand(QuitGuardCommand):

	OPTIONS = (
		('Close Window', 'close_window', ),
		('Save as...', 'prompt_save_as', ),
		('Cancel', None, ),
	)

	OPTION_NAMES = [ opt[0] for opt in OPTIONS ]

	def run(self, edit):
		window = self.view.window()

		if len(window.views()) > 1: window.run_command("close")
		else: super(CloseGuardCommand, self).run(edit)
