# Sublime Maybs Quit

Why are <kbd>ctrl/cmd</kbd> + <kbd>w</kbd> (close file) and <kbd>ctrl/cmd</kbd> + <kbd>q</kbd> (quit) right next to each other?!?! I'm just trying to close a file, but for some insane reason my pinky drifts 1cm to the left and suddenly sublime disappears.

Never again!

## Usage

Quitting shouldn't be so easy. Modal confirmation dialogs are annoying, so why not show a quick panel instead?

- <kbd>ctrl/cmd</kbd> + <kbd>q</kbd> **(osx/linux)**: opens up a quick panel (shown below) that let you choose from a number of options.
- <kbd>alt</kbd> + <kbd>f4</kbd> **(windows only)**: also opens up the quick panel shown below.

<p align="center">
	<img src="http://xavi.co/static/maybs-quit-menu.png" alt="Quit menu" />
</p>

Optionally you can also make this menu appear before the last view in a window is closed by added this keybaord shortcut to your settings:

```json
{ "keys": ["super+w"], "command": "close_guard" }
```

### Why not just change your shortcuts?

Muscle memory... why fight it?

## Getting Maybs Quit

The easiest way to get Maybs Quit is with [Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation). Search for "Maybs Quit".

Alternatively you can clone this git repository into your [Packages Directory](http://sublimetext.info/docs/en/basic_concepts.html):

	git://github.com/xavi-/sublime-maybs-quit.git

## Developed by

* Xavi Ramirez

## License

This project is released under [The MIT License](http://www.opensource.org/licenses/mit-license.php).
