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

    expert_count = FileReader.get_expert_count()
    csv_data, line_count = FileReader.get_data_and_line_count()

    criteria_count, criteria_dict = DataAnalysis.get_criteria_dict_and_criteria_count(csv_data)

    blocks_dict = DataAnalysis.split_blocks(criteria_dict)
    concordance_by_block = {}
    for block in blocks_dict:
        sum_on_criteria_dict = DataAnalysis.get_sum_on_criteria_dict(blocks_dict[block])
        average_mark = DataAnalysis.get_average_mark(sum_on_criteria_dict, len(blocks_dict[block]))
        squared_difference_sum = DataAnalysis.get_squared_difference_sum(sum_on_criteria_dict, average_mark)
        concordance_by_block[block] = float(DataAnalysis.get_concordance(squared_difference_sum, expert_count, len(blocks_dict[block])))

    FileReader.write_dict_to_csv(concordance_by_block)

    print("Done. Check output.csv.")


if __name__ == '__main__':
    main()
