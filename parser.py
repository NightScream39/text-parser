import re


data_array = []


def prepare_text():
    with open('PythonTest.txt') as PT:
        lines = PT.readlines()
        pattern = re.compile(re.escape('#'))
        for line in lines:
            result = pattern.search(line)
            if result is None and line != '\n':
                data_array.append(line)


def text_parser():
    for string in data_array:
        array = string.rstrip().split('\t')
        array_eng = list(set(array[0].split(" ; ")))
        array_ru = list(set(array[1].split(" ; ")))

        with open('English.txt', 'a', encoding='utf-8') as Eng, open('Russian.txt', 'a', encoding='utf-8') as Ru:
            for word in array_eng:
                for slovo in array_ru:
                    Eng.write(word+'\n')
                    Ru.write(slovo+'\n')


if __name__ == "__main__":
    prepare_text()
    text_parser()
