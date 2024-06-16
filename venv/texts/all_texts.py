from pathlib import Path

def readFile(filename, Path=Path):
    return open(Path(__file__).with_name(filename), encoding='UTF-8').read()

individual_courses_text = readFile('individual_courses.txt')
groupe_courses_text = readFile('group_courses.txt')