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


def get_result_dict(average_mark, squared_difference_sum, row_count, criteria_count, overall_concordance):
    result = {
        'Инфо': [
            'Средняя оценка по критериям в таблице',
            'Сумма квадратов отклонений',
            'Количество экспертов',
            'Количество критериев оценки',
            'Общая конкордация'
        ],
        'Результат': [
            average_mark,
            squared_difference_sum,
            row_count,
            criteria_count,
            overall_concordance
        ]
    }

    return result

def main():
    clear()
    info()

    row_count = FileReader.get_row_count()
    csv_data, line_count = FileReader.get_data_and_line_count()

    criteria_count, criteria_dict = DataAnalysis.get_criteria_dict_and_criteria_count(csv_data)

    sum_on_criteria_dict = DataAnalysis.get_sum_on_criteria_dict(criteria_dict)

    average_mark = DataAnalysis.get_average_mark(sum_on_criteria_dict, criteria_count)
    squared_difference_sum = DataAnalysis.get_squared_difference_sum(sum_on_criteria_dict, average_mark)
    overall_concordance = DataAnalysis.get_concordance(squared_difference_sum, row_count, criteria_count)

    result_dict = get_result_dict(average_mark, squared_difference_sum, row_count, criteria_count, overall_concordance)

    FileReader.write_dict_to_csv(result_dict)

    print("Расчеты произведены. Проверь output.csv")


if __name__ == '__main__':
    main()
