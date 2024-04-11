from novel import *
from save import *
from settings import *

def redo_prompt():
    if auto_write:
        return False

    answer = None
    while answer != "y" and answer != "n":
        answer = input("Is this acceptable? (y/n) ")
    if answer == "y":
        return False
    return True

def load_or_create():
    novel_number = input("Load an existing novel? (Enter [novel number] or [nothing] to start a new novel) ") 
    if novel_number == "":
        novel = Novel()
    else:
        parsed = False
        while not parsed:
            try:
                novel_number = int(novel_number)
                parsed = True
            except:
                novel_number = input("Unable to parse novel number. Please re-enter: ")
        novel = load(novel_number)
    return novel_number, novel
