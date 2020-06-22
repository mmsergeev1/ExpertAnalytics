def get_criteria_dict_and_criteria_count(csv_data):
    """
    Analyse data in file and delete all non-usable stuff

    :param csv_data:
    :return: count of criterias in dict and dict of criterias
    """
    criteria_dict = {}
    criteria_count = 0
    for key in csv_data:
        if key[0] == 'Q':  # As we discussed before, all criteria names should start with Q
            criteria_dict[key] = csv_data[key]
            criteria_count += 1

    return criteria_count, criteria_dict


def get_sum_on_criteria_dict(criteria_dict):
    """
    :param criteria_dict:
    :return: dictionary of marks' sum on a criteria
    """
    sum_on_criteria = 0
    sum_on_criteria_dict = {}

    for key in criteria_dict:
        for i in range(len(criteria_dict[key])):
            sum_on_criteria += int(criteria_dict[key][i])
        sum_on_criteria_dict[key] = sum_on_criteria
        sum_on_criteria = 0

    return sum_on_criteria_dict


def get_average_mark(sum_on_criteria_dict, criteria_count):
    """
    :param sum_on_criteria_dict:
    :param criteria_count:
    :return: average mark on criteria, it also equals to mathematical expectation on a criteria
    """
    overall_sum = 0

    for key in sum_on_criteria_dict:
        overall_sum = overall_sum + int(sum_on_criteria_dict[key])

    average_mark = overall_sum / criteria_count
    return float("{:5.2f}".format(average_mark))


def get_squared_difference_sum(sum_on_criteria_dict, average_mark):
    """
    This sum is for concordance and dispersion counting

    :param sum_on_criteria_dict:
    :param average_mark:
    :return: sum of squared differences to average mark
    """
    squared_difference_sum = 0.0

    for key in sum_on_criteria_dict:
        squared_difference_sum += ((int(sum_on_criteria_dict[key]) - float(average_mark)) ** 2)

    return squared_difference_sum


def get_concordance(squared_difference_sum, expert_count, criteria_count):
    """
    Concordance shows how agreed are experts' opinions to each other

    :param squared_difference_sum:
    :param expert_count:
    :param criteria_count:
    :return: concordance for used params
    """
    concordance = (12 * squared_difference_sum) / ((expert_count ** 2) * ((criteria_count ** 3) - criteria_count))

    return "{:2.2f}".format(concordance)


def split_blocks(criteria_dict):
    """
    This is used to get blocks of criteria which are related to a certain question

    :param criteria_dict:
    :return: dictionary of blocks of criterias, where question is a primary key, and criteria with marks are secondary
    """
    blocks_dict = {}
    block = {}

    header = ''
    new_header = ''
    first = True
    i = 0
    for criteria in criteria_dict:  # Todo: refactor split_blocks, remove first and last
        i += 1
        for char in criteria:
            if char != '_':
                new_header += char
            else:
                break

        if first:
            header = new_header
            first = False

        if i == len(criteria_dict) - 1:
            blocks_dict[header] = block

        if new_header == header and new_header != '':
            block[criteria] = criteria_dict[criteria]
            new_header = ''

        elif new_header != '' and new_header != header:
            blocks_dict[header] = block
            block = {criteria: criteria_dict[criteria]}
            header = new_header
            new_header = ''

        elif new_header == '':
            break

    return blocks_dict


def get_gaussian_distribution():
    pass
# TODO: realise gaussian distribution count. mathematical expectation == average on criteria
# false dispersion == squared_difference_sum / expert_count
# true dispersion == false dispersion * expert_count / (expert_count - 1)
# gaussian distribution is counted by a formula
# graphics can be built with imported libs
