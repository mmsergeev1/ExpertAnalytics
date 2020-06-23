import DataAnalysis
import FileReader
from os import system, name


def clear():
    """
    A function used for clearing console screen

    :return: None
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def info():
    """
    Prints program info at the top of console

    :return: None
    """
    print('Read README.md before use!!!')
    print('Program by Mikhail Sergeev, 2020, Moscow')
    print('Leave feedback on GitHub')
    print('=========================================')


def main():
    # clearing console screen and printing info
    clear()
    info()

    # getting info from data.csv
    expert_count = FileReader.get_expert_count()
    csv_data, line_count = FileReader.get_data_and_line_count()

    # deleting commentaries and non-criteria info from dictionaries
    criteria_count, criteria_dict = DataAnalysis.get_criteria_dict_and_criteria_count(csv_data)

    # splitting criterias to blocks and counting concordance for blocks
    blocks_dict = DataAnalysis.split_blocks(criteria_dict)
    concordance_by_block = {}
    for block in blocks_dict:
        sum_on_criteria_dict = DataAnalysis.get_sum_on_criteria_dict(blocks_dict[block])
        average_mark = DataAnalysis.get_average_mark(sum_on_criteria_dict, len(blocks_dict[block]))
        squared_difference_sum = DataAnalysis.get_squared_difference_sum(sum_on_criteria_dict, average_mark)
        concordance_by_block[block] = float(DataAnalysis.get_concordance(squared_difference_sum, expert_count,
                                                                         len(blocks_dict[block])))

    # put data into output.csv
    FileReader.write_dict_to_csv(concordance_by_block)

    print("Done. Check output.csv.")


if __name__ == '__main__':
    main()
