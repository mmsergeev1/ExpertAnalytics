def get_criteria_dict_and_criteria_count(csv_data):
    criteria_dict = {}
    criteria_count = 0
    for key in csv_data:
        if key[0] == 'Q':
            criteria_dict[key] = csv_data[key]
            criteria_count = criteria_count + 1

    return criteria_count, criteria_dict


def get_value(criteria_list, row_count, criteria_count):
    sum_of_marks = 0
    for i in range(1, row_count):
        sum_of_marks = sum_of_marks + int(criteria_list[i])

    average_mark = sum_of_marks / row_count
    result = []

    for i in range(1, row_count):
        result.append((12 * (int(criteria_list[i]) - average_mark ** 2))/(row_count ** 2 (criteria_count ** 3 - criteria_count)))

    return result
