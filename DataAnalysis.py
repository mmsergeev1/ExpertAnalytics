def get_criteria_dict_and_criteria_count(csv_data):
    criteria_dict = {}
    criteria_count = 0
    for key in csv_data:
        if key[0] == 'Q':
            criteria_dict[key] = csv_data[key]
            criteria_count = criteria_count + 1

    return criteria_count, criteria_dict


def get_sum_on_criteria(criteria_list, row_count):
    sum_on_criteria = 0

    for i in range(row_count):
        sum_on_criteria = sum_on_criteria + int(criteria_list[i])

    return sum_on_criteria


def get_average_mark(sum_on_criteria, criteria_count):
    overall_sum = 0

    for key in sum_on_criteria:
        overall_sum = overall_sum + int(sum_on_criteria[key])

    average_mark = overall_sum / criteria_count
    return "{:5.2f}".format(average_mark)


def get_squared_difference_sum(sum_on_criteria, average_mark):
    squared_difference_sum = 0.0

    for key in sum_on_criteria:
        squared_difference_sum = squared_difference_sum + ((int(sum_on_criteria[key]) - float(average_mark)) ** 2)

    return squared_difference_sum


def get_concordance(squared_difference_sum, row_count, criteria_count):
    concordance = (12 * squared_difference_sum) / ((row_count ** 2) * ((criteria_count ** 3) - criteria_count))

    return "{:2.2f}".format(concordance)
