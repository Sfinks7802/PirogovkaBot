from pathlib import Path

def readFile(filename, Path=Path):
    return open(Path(__file__).with_name(filename), encoding='UTF-8').read()

individual_courses_text = readFile('individual_courses.txt')
groupe_courses_text = readFile('group_courses.txt')
letniy_intensiv_text = readFile('letniy_intensiv.txt')
letniy_intensiv_2_text = readFile('letniy_intensiv_2.txt')
komu_podhodit_text = readFile('komu_podhodit.txt')
temy_int = readFile('temy_int.txt')
bibla_text = readFile('bibla.txt')
gista_course_txt = readFile('gista_course.txt')
for_who_txt = readFile('for_who.txt')
tarifs_course_txt = readFile('tarifs_course.txt')
conspects_course_txt = readFile('conspeccts_course.txt')
how_learn_txt = readFile('how_learn.txt')
courator_txt = readFile('courator.txt')
why_us_txt = readFile('why_us.txt')
mission_txt = readFile('mission.txt')