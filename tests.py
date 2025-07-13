import unittest

from aggregate import rows_aggregate
from read_csv import read_csv
from validate import rows_validate
from filter import rows_filter


class TestScript(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {"id": 1, "name": "Product1", "price": 100, "rating": 4.5},
            {"id": 2, "name": "Product2", "price": 200, "rating": 4.8},
            {"id": 3, "name": "Product3", "price": 150, "rating": 4.2}
        ]
        self.arg_1 = "rating>4.5"
        self.arg_2 = "name=Product1"
        self.arg_3 = "price<100"
        self.arg_4 = [
            {"id": 1, "name": "Product1", "price": 100, "rating": '4.5'}
        ]

    # Тест валидации
    def test_validate_filter(self):
        column, op, value, filter_list = rows_validate(self.rows, self.arg_1)
        self.assertEqual(column, "rating")
        self.assertEqual(op, ">")
        self.assertEqual(value, 4.5)
        self.assertEqual(len(filter_list), 3)

    def test_validate_aggregate(self):
        column, op, value, filter_list = rows_validate(self.rows, self.arg_2)
        self.assertEqual(column, "name")
        self.assertEqual(op, '=')
        self.assertEqual(value, 'product1')
        self.assertEqual(len(filter_list), 3)

    # Тест фильтрации
    def test_filter_rows_gt(self):
        column, op, value, filter_list = rows_validate(self.rows, self.arg_1)
        filter_list = rows_filter(column, op, value, filter_list)
        self.assertEqual(len(filter_list), 1)
        self.assertEqual(filter_list[0]['id'], 2)

    def test_filter_rows_eq(self):
        column, op, value, filter_list = rows_validate(self.rows, self.arg_2)
        filter_list = rows_filter(column, op, value, filter_list)
        self.assertEqual(len(filter_list), 1)
        self.assertEqual(filter_list[0]['name'], 'product1')

    def test_filter_rows_lt(self):
        column, op, value, filter_list = rows_validate(self.rows, self.arg_3)
        filter_list = rows_filter(column, op, value, filter_list)
        self.assertEqual(len(filter_list), 0)

    # Тест агрегации
    def test_aggregate_zero(self):
        with self.assertRaises(ValueError) as context:
            rows_aggregate("price", "avg", None, [])

        self.assertEqual(str(context.exception), "Нет данных для агрегации")

    def test_aggregate_rows_inst(self):
        filter_list = rows_aggregate("rating", "avg", '4', self.arg_4)
        self.assertEqual(len(filter_list), 0)

    def test_aggregate_rows_avg(self):
        filter_list = rows_aggregate("rating", ">", "avg", self.rows)
        self.assertEqual(len(filter_list), 1)
        self.assertEqual(filter_list, [{'avg': 4.5}])

    def test_aggregate_rows_min(self):
        filter_list = rows_aggregate("rating", ">", "min", self.rows)
        self.assertEqual(len(filter_list), 1)
        self.assertEqual(filter_list, [{'min': 4.2}])

    def test_aggregate_rows_max(self):
        filter_list = rows_aggregate("rating", ">", "max", self.rows)
        self.assertEqual(len(filter_list), 1)
        self.assertEqual(filter_list, [{'max': 4.8}])

    # Тест чтение файла
    def test_read_csv(self):
        result = read_csv('data2.csv')
        print(result)
        self.assertEqual(result, [{'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
                                  {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
                                  {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
                                  {'brand': 'xiaomi', 'name': 'poco x5 pro', 'price': '299', 'rating': '4.4'}]
                         )


if __name__ == '__main__':
    unittest.main()
