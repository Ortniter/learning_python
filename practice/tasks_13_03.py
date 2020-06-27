import os


# Напишите функцию копирования файлов. На вход ваша функция принимает два аргумента:
# - путь файла который необходимо скопировать
# - путь каталога куда этот файл необходимо скопировать

# все могло быть намного короче с помощью импорта 'from shutil import copyfile'
# но по заданию наверное надо было с помощью os сделать
def copyFileDir(inFile, outDir):
    with open(inFile, 'r') as file:
        content = file.read()
    os.chdir(outDir)
    with open(inFile, 'w') as file:
        file.write(content)


copyFileDir('tasks_13_03.py', 'test')

# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline


def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }

        def wrapper(text):
            for tag in tags:
                if tag in tag_base:
                    text = tag_base[tag].replace('%text%', func(text))
            return text

        return wrapper

    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text


# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных

def log_reading(func):
    def wrapper():
        for file in func():
            if file.endswith('.log'):
                with open(file, 'r') as log:
                    print(log.read())
        return func()

    return wrapper


@log_reading
def get_files():
    path = os.getcwd()
    file_list = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    return file_list

# Напишите функцию, которая читает и распечатывает текстовый файл.
# Напишите декоратор к этой функции, который печатает название файла и количество слов в нем


def name_and_length(func):
    def wrapper(file):
        with open(file, 'r') as txt:
            read_file = txt.read()
            name = os.path.basename(os.path.join(os.getcwd(), file))
            print(f"There are {len(read_file.split(' '))} words in file called - {name}\n"
                  f"___________________________________________")
        return func(file)

    return wrapper


@name_and_length
def read_txt(file):
    with open(file, 'r') as txt:
        print(txt.read())
