import sys
import readline
import json

from novel import *
from save import *
from settings import *
from misc import *

print("LLM Novel Writer - Drafting")
print("----------------------------")

novel_number, novel = load_or_create()

# Parse the JSON created from the outline
novel.parse_outline_json()

# Write chapter outlines
previous_chapter_outline = "This is the beginning of the novel so it does not have a previous chapter."
previous_chapter_summary = previous_chapter_outline
chapter_summaries = [chapter for part in novel.parsed_plot for chapter in part['chapter-descriptions']]
for i, chapter_summary in enumerate(chapter_summaries):
    chapter_number = i+1
    if not getattr(novel, "chapter_outlines", None):
        novel.chapter_outlines = {}
    if str(chapter_number) not in novel.chapter_outlines:
        redo = True
        while redo:
            next_chapter_summary = (
                chapter_summaries[chapter_number]
                if len(chapter_summaries) > chapter_number else
                "This is the end of the novel so it does not have a next chapter."
            )
            new_outline = novel.write_chapter_outline(
                writer,
                chapter_number,
                chapter_summary,
                previous_chapter_summary,
                next_chapter_summary,
                previous_chapter_outline
            )
            print(new_outline)
            redo = redo_prompt()
        save(novel, novel_number)
        previous_chapter_outline = new_outline
    else:
        previous_chapter_outline = novel.chapter_outlines[str(chapter_number)]
    previous_chapter_summary = chapter_summary

# Parse the JSON from the chapter outlines
novel.parse_chapter_outline_json()
#print(novel.parsed_chapter_outlines)

# Write chapter paragraph blocks
for chapter_number, chapter_paragraph_descriptions in novel.parsed_chapter_outlines.items():
    chapter_num_paragraphs = len(chapter_paragraph_descriptions)
    paragraph_descriptions_block_list = [
        chapter_paragraph_descriptions[i:i + paragraphs_per_block]
        for i in range(0, chapter_num_paragraphs, paragraphs_per_block)
    ]
    previous_paragraph_block = "(Start of the first paragraph of the chapter)"
    chapter_paragraph_block_number = 1
    for block_number, paragraph_descriptions in enumerate(paragraph_descriptions_block_list):
        if chapter_number not in novel.chapters or str(block_number+1) not in novel.chapters[chapter_number]:
            if block_number+1 == len(paragraph_descriptions_block_list):
                next_paragraph_descriptions = []
            else:
                next_paragraph_descriptions = paragraph_descriptions_block_list[block_number+1]
            part = novel.parsed_plot[(int(chapter_number)-1) // 5]
            chapter_summary = part['chapter-descriptions'][(int(chapter_number)-1) % 5]
            redo = True
            while redo:
                paragraph_block = novel.write_paragraph_block(
                    writer,
                    chapter_paragraph_block_number,
                    previous_paragraph_block,
                    paragraph_descriptions,
                    next_paragraph_descriptions,
                    chapter_number,
                    chapter_summary,
                    chapter_num_paragraphs
                )
                print(paragraph_block)
                redo = redo_prompt()
            save(novel, novel_number)
            previous_paragraph_block = paragraph_block
        else:
            previous_paragraph_block = novel.chapters[chapter_number][str(block_number+1)]
        chapter_paragraph_block_number += 1

print(f"This concludes the novel drafting process. You should now review the file at novels/{novel_number}.json and make edits as needed. After editing the file, run finalize.py.")
