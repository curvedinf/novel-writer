import sys
import readline
import json

from writer import *
from novel import *
from save import *
from settings import *
from misc import *

print("LLM Novel Writer - Finalizing")
print("----------------------------")

writer = AnthropicWriter(system_context) # Gemini10Writer(system_context)

novel_number, novel = load_or_create()

# write all the chapters to a plain text file
with open(f"novels/{novel_number}.txt", "w") as f:
    # Write the title
    f.write(f'{novel.title}\n\nBy AI written by Chase Adams\n\n')
    for chapter_number, chapter_blocks in novel.chapters.items():
        # Write the chapter number
        f.write(f'Chapter {chapter_number}\n\n')
        # Write the chapter blocks
        for block_number, block_text in chapter_blocks.items():
            f.write(f'{block_text}\n\n')
