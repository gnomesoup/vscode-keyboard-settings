# VSCode Keyboard Settings Switcher

This is a command-line tool for switching keyboard layouts in a vscode settings.json
file. It will add the key bindings to the VsCodeVim normal and visual settings to
switch the main navigation keys to the right hand home row for the Colemak DH layout.
It will also add bindings for any conflicts that are caused by the switch.

## Usage

```bash
python main.py [layout] [filename]
```

Where:

- `layout` is either 'colemak' or 'querty'
- `filename` is the path to your settings.json file (default is 'settings.json')

## Example

```bash
python main.py colemak ./mysettings.json
```

This will change the key bindings in the 'mysettings.json' file to the 'colemak' layout.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository
2. Run the script with Python

## License

MIT
