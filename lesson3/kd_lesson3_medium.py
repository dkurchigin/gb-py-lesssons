import os


def programm_title():
    print("**************************")
    print("*GB/Python/Lesson3/MEDIUM*")
    print("**************************")


def write_to_file(file, info):
    with open(file, 'a', encoding='UTF-8') as f:
        for key, value in info.items():
            if value >= 500000:
                value = "*засекречено*"
            out_string = str(key) + " - " + str(value) + "\n"
            f.write(str(out_string))


def format_names(names):
    for element in names:
        names[names.index(element)] = element.capitalize()
    return names


def print_strings_from_file(file):
    with open(file, 'r', encoding='UTF-8') as f:
        for line in f:
            name, salary = line.split(' - ')
            if not (salary == "*засекречено*\n"):
                salary = float(salary) * 0.87
            else:
                salary = salary.replace('\n','')
            print(name, salary, "- получит на руки после вычета налогов")


names = ["Василий", "мИхаИл", "рома"]
salary = [120000.50, 35000, 510003.90]

out_file = "salary.txt"

names = format_names(names)
zipped_info = dict(zip(names, salary))

if os.path.isfile(out_file):
    os.remove(out_file)
write_to_file(out_file, zipped_info)

print_strings_from_file(out_file)