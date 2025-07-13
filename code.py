import argparse
from read_csv import read_csv
from aggregate import rows_aggregate
from filter import rows_filter
from validate import rows_validate

from tabulate import tabulate


def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description="Чтение и фильтрация CSV файла")

    # Фильтрация с передачей колонки, оператора и значения
    parser.add_argument("--where", type=str, help="Фильтровать данные по условию, например: rating>4.7")

    # Агрегация с передачей колонке
    parser.add_argument("--aggregate", type=str, help="Агрегация данных по колонке, например: avg, max, min")

    # Путь к CSV файлу
    parser.add_argument("csv_file", help="Путь к CSV файлу")

    # Разбор аргументов командной строки
    args = parser.parse_args()

    try:
        # Читаем CSV файл
        rows = read_csv(args.csv_file)
        if not rows:
            print("Файл пуст")
            return

        result = [] # Список для хранения результатов

        if args.where:
            # Валидируем куоманду
            column, op, value, filter_list = rows_validate(rows, args.where)

            # Фильтруем данные
            filter_rows = rows_filter(column, op, value, filter_list)

            # Сохраняем данные
            result = filter_rows

        if args.aggregate:
            # Валидируем куоманду
            column, op, value, filter_list = rows_validate(rows, args.aggregate)

            # Фильтруем данные
            aggregate_rows = rows_aggregate(column, op, value, filter_list)

            # Сохраняем данные
            result = aggregate_rows

        print(tabulate(result, headers="keys", tablefmt="grid"))

    except Exception as e:
        print(f"Ошибка: {e}")


main()
