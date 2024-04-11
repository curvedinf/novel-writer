import sys
import readline
import json

from novel import *
from save import *
from settings import *
from misc import *

print("LLM Novel Writer - Outlining")
print("----------------------------")

novel_number, novel = load_or_create()

# Synopsis
if not getattr(novel, "synopsis", None):
    novel.setup()
    redo = True
    while redo:
        print(novel.create_synopsis(writer))
        redo = redo_prompt()
    novel_number = save_new(novel)

# Characters
if not getattr(novel, "characters", None):
    redo = True
    while redo:
        print(novel.create_characters(writer))
        redo = redo_prompt()
    save(novel, novel_number)

# Settings
if not getattr(novel, "settings", None):
    redo = True
    while redo:
        print(novel.create_settings(writer))
        redo = redo_prompt()
    save(novel, novel_number)

# Plot
if not getattr(novel, "plot", None):
    redo = True
    while redo:
        print(novel.create_plot(writer))
        redo = redo_prompt()
    save(novel, novel_number)

# Title
if not getattr(novel, "title", None):
    redo = True
    while redo:
        print(novel.create_title(writer))
        redo = redo_prompt()
    save(novel, novel_number)

print(f"This concludes the novel outlining process. You should now review the file at novels/{novel_number}.json and make edits as needed. After editing the file, run draft.py.")
