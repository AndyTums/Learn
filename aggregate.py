def rows_aggregate(column, op, value, rows):
    """ Функция агрегирует данные по заданным параметрам """

    if not rows:
        raise ValueError("Нет данных для агрегации")

    aggregate_list = []
    values = []
    for row in rows:

        if isinstance(row[column], (int, float)):
            values.append(row[column])
            if not row[column]:
                values.append(0)

        else:
            continue

    if value == "avg":
        result = {'avg': sum(values) / len(values)}
        aggregate_list.append(result)

    elif value == "min":
        result = {'min': min(values)}
        aggregate_list.append(result)

    elif value == "max":
        result = {'max': max(values)}
        aggregate_list.append(result)

    return aggregate_list
