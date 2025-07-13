def rows_validate(rows, filter_data):

    operators = ['>', '<', '=', '>=', '<=', '!=']

    # Находим оператор, значение и столбец
    for op in operators:
        if op in filter_data:
            # Присваиваем переменные
            column, value = filter_data.split(op)

            # Чистим переменные
            column = column.strip().lower()
            value = value.strip().lower()

            # Валидируем данные с команды
            try:
                # Перебразуем в float
                value = float(value)
            except ValueError:
                pass  # Если это строка, оставляем как есть

            filter_list = []
            # Форматируем данные из файла
            for row in rows:
                format_row = row.copy()

                if column in format_row:

                    try:
                        # Перебразуем в float
                        curr_value = float(format_row[column])

                    except ValueError:
                        # Если это строка, оставляем как есть
                        curr_value = format_row[column].strip().lower()

                    format_row[column] = curr_value
                    filter_list.append(format_row)

                else:
                    continue  # Пропускаем, если нет данных

            return column, op, value, filter_list
