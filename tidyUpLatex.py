import sublime, sublime_plugin, os, os.path, platform
import getTeXRoot
from subprocess import Popen

class TidyuplatexCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		# get the name of the current file
		texFile, texExt = os.path.splitext(self.view.file_name())

		# if the file is not ending with .tex, return an error message
		if texExt.upper() != ".TEX":
			sublime.error_message("%s is not a TeX source file: Cannot tidy up." % (os.path.basename(self.view.file_name()),))
			return
		quotes = ""# \"" MUST CHECK WHETHER WE NEED QUOTES ON WINDOWS!!!
		root = getTeXRoot.get_tex_root(self.view.file_name())
		rootFile, rootExt = os.path.splitext(root)

		# use latexmk to clean up all auxiliary files
		tidyupcmd = ["latexmk","-c"];
		try:
			Popen(tidyupcmd + [rootFile+".tex"]);
		except OSError:
			# if there occured an error, show an error message
			sublime.error_message("Error while executing latexmk. Make sure it is on your PATH.")					

		# if successfully tidied up, show this in status bar
		sublime.status_message("Finished tidying up.");
