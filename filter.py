def rows_filter(column, op, value, rows):
    """ Функция фильтрует данные по заданным параметрам """

    filter_list = []
    for row in rows:

        if op == "=" and row[column] == value:
            filter_list.append(row)
        elif op == ">" and row[column] > value:
            filter_list.append(row)
        else:
            continue

    return filter_list
