import re


def prepare_text():
    with open('PythonTest.txt') as PT:
        lines = PT.readlines()
        pattern = re.compile('#')
        data_array = []
        for line in lines:
            result = pattern.search(line)
            if result is None and line != '\n':
                data_array.append(line)
        return data_array


def text_parser():
    for string in prepare_text():
        array = string.rstrip().split('\t')
        array_eng = list(set(array[0].split(" ; ")))
        array_ru = list(set(array[1].split(" ; ")))

        with open('English.txt', 'a', encoding='utf-8') as Eng, open('Russian.txt', 'a', encoding='utf-8') as Ru:
            for word in array_eng:
                for slovo in array_ru:
                    Eng.write(word+'\n')
                    Ru.write(slovo+'\n')


if __name__ == "__main__":
    text_parser()
