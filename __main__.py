import DataAnalysis
import FileReader
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def info():
    print('Прочти инструкцию перед использованием!!!')
    print('Автор Михаил С. Москва 2020')
    print('=========================================')


def main():
    clear()
    info()

    row_count = FileReader.get_row_count()
    csv_data, line_count = FileReader.get_data_and_line_count()

    criteria_count, criteria_dict = DataAnalysis.get_criteria_dict_and_criteria_count(csv_data)

    w = {}
    for key in criteria_dict:
        w[key] = DataAnalysis.get_value(criteria_dict[key], row_count, criteria_count)

    print(w)


if __name__ == '__main__':
    main()
