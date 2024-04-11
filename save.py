import os
import jsonpickle

def save(instance, novel_number, extension="json", directory="novels"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = os.path.join(directory, f"{novel_number}.{extension}")
    with open(path, "w") as f:
        f.write(jsonpickle.encode(instance, unpicklable=True, make_refs=False, indent=4))
        print(f"Saved novel data to {path}")

def save_new(instance, extension="json", directory="novels"):
    novel_number = 1
    path = os.path.join(directory, f"{novel_number}.{extension}")
    while os.path.exists(path):
        novel_number += 1
        path = os.path.join(directory, f"{novel_number}.{extension}")
    save(instance, novel_number, extension, directory)
    return novel_number

def load(novel_number, extension="json", directory="novels"):
    path = os.path.join(directory, f"{novel_number}.{extension}")
    with open(path, 'rb') as f:
        return jsonpickle.decode(f.read())
