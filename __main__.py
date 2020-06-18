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

    concordance = {}
    sum_on_criteria = {}
    for key in criteria_dict:
        sum_on_criteria[key] = DataAnalysis.get_sum_on_criteria(criteria_dict[key], row_count)

    average_mark = DataAnalysis.get_average_mark(sum_on_criteria, criteria_count)
    squared_difference_sum = DataAnalysis.get_squared_difference_sum(sum_on_criteria, average_mark)
    overall_concordance = DataAnalysis.get_concordance(squared_difference_sum, row_count, criteria_count)

    print(f'Средняя оценка по всем критериям: {average_mark}')
    print(f'Сумма квадратов отклонений: {squared_difference_sum}')
    print(f'Количество экспертов: {row_count}')
    print(f'Количество критериев оценки: {criteria_count}')
    print(f'Общая конкордация: {overall_concordance}')

if __name__ == '__main__':
    main()
