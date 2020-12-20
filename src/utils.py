def check_inn(inn: str):
    """
        Checking INN based on that info https://www.egrul.ru/test_inn.html
        Checks valid only for individuals (физ лиц)
    """
    flag = 1

    check_sum = 7 * int(inn[0]) + 2 * int(inn[1]) + 4 * int(inn[2]) \
                + 10 * int(inn[3]) + 3 * int(inn[4]) + 5 * int(inn[5]) \
                + 9 * int(inn[6]) + 4 * int(inn[7]) + 6 * int(inn[8]) \
                + 8 * int(inn[9])
    num_11 = check_sum % 11

    if num_11 > 9:
        flag *= ((num_11 % 10) == int(inn[-2]))
    else:
        flag *= (num_11 == int(inn[-2]))

    check_sum = 3 * int(inn[0]) + 7 * int(inn[1]) + 2 * int(inn[2]) \
                + 4 * int(inn[3]) + 10 * int(inn[4]) + 3 * int(inn[5]) \
                + 5 * int(inn[6]) + 9 * int(inn[7]) + 4 * int(inn[8]) \
                + 6 * int(inn[9]) + 8 * int(inn[10])
    num_12 = check_sum % 11

    if num_12 > 9:
        flag *= ((num_12 % 10) == int(inn[-1]))
    else:
        flag *= (num_12 == int(inn[-1]))

    return flag