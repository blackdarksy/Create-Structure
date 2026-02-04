Create Structure
================

Short description
-----------------
This small Python utility reads a tree-like text description (e.g., `structure.txt`) and creates the corresponding folders and files on disk. It's useful for bootstrapping a project skeleton from a plain text outline.

Files in this repo
------------------
- `create_structure.py` — main script that parses the structure file and creates folders/files.
- `structure.txt` — example input showing a tree using box-drawing characters and `/` for folders.

Requirements
------------
- Python 3.7+ (tested on 3.8+)
- No external packages required (uses the standard library)

Usage
-----
1. Open a terminal in the repository folder.
2. Run:

   python create_structure.py

3. When prompted, enter the structure file name, for example:

   Enter the structure file (e.g., structure.txt): structure.txt

The script will parse the file and create directories and files under the current working directory. It prints created items like `[DIR ]` and `[FILE]` lines.

Notes on the structure file format
---------------------------------
- Lines that end with `/` are treated as directories.
- Box-drawing characters such as `│ ├ └ ─` (and emojis like `📁 📄`) are supported and removed during parsing.
- Blank lines are ignored.
- The parser uses the prefix to determine depth; indentation may be box characters or groups of spaces.

Safety
------
- The script will create files and directories—test it in an empty folder or a temporary directory first.

Suggestions / Improvements
-------------------------
- Add a `--dry-run` or command-line argument option to avoid interactive input.
- Add a `--root` flag to change the destination base.

License
-------
You may use or adapt this script freely. Consider adding an explicit license (e.g., MIT) to the repo.

Welcome! If you want, I can also add a `README.md` (Markdown) version optimized for GitHub display or implement command-line options for convenience.
