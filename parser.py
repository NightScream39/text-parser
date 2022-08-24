import re


def prepare_text():
    with open('PythonTest.txt') as f:
        lines = f.readlines()
    pattern = re.compile(re.escape('#'))
    with open('PythonTest.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None and line != '\n':
                f.write(line)


def text_parser():
    with open('PythonTest.txt') as f:
        lines = f.readlines()
        for line in lines:
            array = line.rstrip().split('\t')
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
