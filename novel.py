import json
import random

class Novel:
    def __init__(self):
        self.one_liner = None
        self.extra_context = None
        self.synopsis = None
        self.characters = None
        self.settings = None
        self.title = None
        self.plot = None
        self.chapter_outlines = {}
        self.chapters = {}
    
    def setup(self):
        self.one_liner = input("What do you want the novel to be about? ")
        self.extra_context = input("How should the novel be written? ")
    
    def create_synopsis(self, writer):
        print("I'm writing a synopsis...")
        prompt = f"""Write a synopsis for a novel.


One line description for the novel:
{self.one_liner}


How the novel is written (its writing style):
{self.extra_context}


Do not write the title or any additional formatting. Only write a single long paragraph."""
        self.synopsis = writer.write(prompt)
        return self.synopsis
            
    def create_characters(self, writer):
        print("I'm writing a list of characters...")
        prompt = f"""Write a json object that describes 10 characters of the novel. The list should
include the main character, 3 supporting character, a main antagonist, 2 secondary antagonists,
and 3 neutral characters. 


How the novel is written:
{self.extra_context}


Novel synopsis:
{self.synopsis}


Here is the format to follow:

[
{{
"name": "The name of the character.",
"personality": "A paragraph describing the character's personality. Include some likeable attributes and dislikeable attributes. Write a considerable amount about the character's personality and use colorful language to describe him or her. Write in the tone of the novel. Do not write about what the character does in the novel.",
"physique": "Some details about the character's physique."
}},
...
]


Do not write anything except json. Do not respond with an introduction or statement before the json. Do not format with markup."""
        self.characters = writer.write(prompt)
        return self.characters
            
    def create_settings(self, writer):
        print("I'm writing a list of settings...")
        prompt = f"""Write a json object that describes 5 settings of the novel.


How the novel is written (its writing style):
{self.extra_context}


Novel synopsis:
{self.synopsis}


Novel characters:
{self.characters}


Here is the format to follow:

[
{{
"name": "The name of the setting.",
"description": "A paragraph describing the setting. Describe its attributes in detail so a reader can clearly picture the place. Use words that inspire the right emotions that will accentuate the plot elements that take place in the setting. Write in the correct tone for the novel."
}},
...
]


Do not write anything except json. Do not respond with an introduction or statement before the json. Do not format with markup."""
        self.settings = writer.write(prompt)
        return self.settings

    def create_plot(self, writer):
        print("I'm writing a plot...")
        prompt = f"""Write a json object that describes every chapter of the novel in a paragraph each.


How the novel is written (its writing style):
{self.extra_context}


Novel synopsis:
{self.synopsis}


Novel characters:
{self.characters}

Novel settings:
{self.settings}


Here is the format to follow:

[
{{
"part-number": <An integer representing the part number>,
"chapter-descriptions": [
"A paragraph describing the first chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the second chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the third chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the fourth chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the fifth chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel."
]
}},
{{
"part-number": <An integer representing the part number>,
"chapter-descriptions": [
"A paragraph describing the first chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the second chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the third chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the fourth chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the fifth chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel."
]
}},
{{
"part-number": <An integer representing the part number>,
"chapter-descriptions": [
"A paragraph describing the first chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the second chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the third chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the fourth chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the fifth chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel."
]
}},
{{
"part-number": <An integer representing the part number>,
"chapter-descriptions": [
"A paragraph describing the first chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the second chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the third chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the fourth chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel.",
"A paragraph describing the fifth chapter of this part. It should consist of 5 sentences. The paragraph should describe who did what, why they did it, and where they did it. Write it in the style of the novel."
]
}}
]


The json object should have four main elements representing each part of the story, and each part
should have five chapter descriptions. Each chapter description is a paragraph of 5 sentences.
Do not write anything except json. Do not respond with an introduction or statement before the 
json. Do not format with markup."""
        self.plot = writer.write(prompt)
        return self.plot

    def create_title(self, writer):
        print("I'm writing a title...")
        prompt = f"""Create the title of this story.


How the novel is written (its writing style):
{self.extra_context}


Novel synopsis:
{self.synopsis}


Novel characters:
{self.characters}


Novel settings:
{self.settings}


Novel plot:
{self.plot}


Respond with only the title of the novel. Do not respond with an introduction or statement before the title."""
        self.title = writer.write(prompt)
        return self.title

    def parse_outline_json(self):
        print("Parsing outline JSON into native objects...")
        try:
            self.parsed_characters = json.loads(self.characters)
        except Exception as e:
            print("Characters weren't able to be parsed to JSON. Fix it in the novel json file then rerun.")
            raise e

        try:
            self.parsed_settings = json.loads(self.settings)
        except Exception as e:
            print("Settings weren't able to be parsed to JSON. Fix it in the novel json file then rerun.")
            raise e
            
        try:
            self.parsed_plot = json.loads(self.plot)
        except Exception as e:
            print("Plot wasn't able to be parsed to JSON. Fix it in the novel json file then rerun.")
            raise e

    def write_chapter_outline(
            self, 
            writer, 
            chapter_number, 
            chapter_summary, 
            previous_chapter_summary, 
            next_chapter_summary, 
            previous_outline
        ):
        print(f"I'm writing an outline for chapter {chapter_number}...")
        print(f"Previous chapter summary:\n{previous_chapter_summary}")
        print(f"Chapter summary:\n{chapter_summary}")
        print(f"Next chapter summary:\n{next_chapter_summary}")
        num_paragraphs = random.randint(13,20)
        output_format = ",\n".join([
            f"""{{
"paragraph-number": {pn},
"paragraph-summary": "A sentence outlining paragraph {pn} of the chapter written in the correct tone for the novel."
}}"""
            for pn in range(1,5)
        ])
        prompt = f"""Write JSON that outlines the chapter {chapter_number} of this novel as {num_paragraphs} paragraph summaries.


Current chapter number:
{chapter_number}


Current chapter summary (the paragraphs should all describe this):
{chapter_summary}


Previous chapter summary (the first paragraph should lead from this):
{previous_chapter_summary}


Previous chapter outline (the first paragraph should lead from this):
{previous_outline}


Next chapter summary (the last paragraph should lead into this):
{next_chapter_summary}


How the novel is written (its writing style):
{self.extra_context}


Novel title:
{self.title}


Novel characters:
{self.characters}


Novel settings:
{self.settings}


Novel plot:
{self.plot}


Here is the format to follow:

[
{output_format}
]


Create a JSON object that has a paragraph summary for each of the chapter's {num_paragraphs} paragraphs.
Every paragraph summary you write is a part of the current chapter and should be described by the
current chapter summary. None of the paragraph summaries should be described by the rest of the plot.
The first paragraph should begin where from the previous chapter summary leaves off. The last paragraph 
should lead to the next chapter summary. Do not write anything except json. Do not respond with an
introduction or statement before the json. Do not format with markup."""
        self.chapter_outlines[chapter_number] = writer.write(prompt)
        return self.chapter_outlines[chapter_number]

    def parse_chapter_outline_json(self):
        print("Parsing chapter outline JSON into native objects...")
        self.parsed_chapter_outlines = {}
        for key, value in self.chapter_outlines.items():
            try:
                self.parsed_chapter_outlines[key] = json.loads(value)
            except Exception as e:
                print(f"Chapter {key}'s outline wasn't able to be parsed to JSON. Fix it in the novel json file then rerun.")
                raise e

    def write_paragraph_block(
            self,
            writer,
            chapter_paragraph_block_number,
            previous_paragraph_block,
            paragraph_descriptions,
            next_paragraph_descriptions,
            chapter_number,
            chapter_summary,
            chapter_num_paragraphs
        ):
        start_paragraph_number = paragraph_descriptions[0]["paragraph-number"]
        end_paragraph_number = paragraph_descriptions[-1]["paragraph-number"]

        paragraph_descriptions_unrolled = "\n\n".join([
            paragraph_data["paragraph-summary"]
            for paragraph_data in paragraph_descriptions
        ])

        next_paragraph_descriptions_unrolled = "\n\n".join([
            paragraph_data["paragraph-summary"]
            for paragraph_data in next_paragraph_descriptions
        ])

        print(f"I'm writing paragraphs {start_paragraph_number}-{end_paragraph_number} for chapter {chapter_number} (block number {chapter_paragraph_block_number})...")
        print(f"Paragraph descriptions:\n{paragraph_descriptions}")

        prompt = f"""Continue writing {len(paragraph_descriptions)} more paragraphs of the novel using the information below.


Novel title:
{self.title}


How the novel is written (its writing style):
{self.extra_context}


Novel characters:
{self.characters}


Novel settings:
{self.settings}


Novel synopsis:
{self.synopsis}


Summary of the current chapter:
{chapter_summary}


Descriptions of the paragraphs you will write (PARAGRAPH DESCRIPTIONS):
{paragraph_descriptions_unrolled}


Descriptions of paragraphs that will be directly after the paragraphs you write (NEXT PARAGRAPHS):
{next_paragraph_descriptions_unrolled}


Continue writing the story for {len(paragraph_descriptions)} more paragraphs based on the PARAGRAPH DESCRIPTIONS 
above. Each paragraph should have 3-7 sentences. Make sure what you write leads well into NEXT
PARAGRAPHS. Only write the novel's paragraphs. Do not write an introduction or description before
or after the paragraphs. Below are the paragraphs that are directly before the paragraphs you will write:

{previous_paragraph_block}"""
        if getattr(self, "chapters", None) is None:
            self.chapters = {}
        if chapter_number not in self.chapters:
            self.chapters[chapter_number] = {}
        self.chapters[chapter_number][chapter_paragraph_block_number] = writer.write(prompt)
        return self.chapters[chapter_number][chapter_paragraph_block_number]
