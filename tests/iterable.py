import json
import os

from unittrial import TestCase, logger
from unittrial.assertions import assert_true, assert_equals, assert_is_instance, assert_is_not_none, assert_is_none, \
    assert_false

from pyfunctional import List, Set, Tuple


class IndexIteratorTests(TestCase):

    def all(self):
        assert_true(self.number_list.all(lambda x: isinstance(x, int)))

    def any(self):
        assert_true(self.number_list.any(lambda x: isinstance(x, int)))

    def filter(self):
        filtered_list = self.number_list.filter(lambda x: x % 2 == 0)

        logger.info(f"From {self.number_list}")
        logger.info(f"To   {filtered_list}")
        assert_equals(filtered_list[0], 2)
        assert_equals(filtered_list[1], 4)

    def find(self):
        found = self.str_list.find(lambda x: x.startswith("app"))
        logger.info(f"Found: {found}")
        assert_is_not_none(found)

        assert_is_none(self.str_list.find(lambda x: x == 1))

    def find_or_default(self):
        found = self.str_list.find(lambda x: x.startswith("app"))
        logger.info(f"Found: {found}")
        assert_is_not_none(found)

        assert_equals(self.str_list.find_or_default(lambda x: x == 1, 10), 10)

    def flatten(self):
        flatten_list = self.nested_number_list.flatten()

        logger.info(f"From {self.nested_number_list}")
        logger.info(f"To   {flatten_list}")
        assert_equals(len(flatten_list), 12)

    def is_empty(self):
        assert_true(List().is_empty())
        assert_false(List([1]).is_empty())

    def load_csv(self):
        self.dict_list.save_csv("loadtest.csv")

        test_dict_list = List.load_csv("loadtest.csv")
        assert_equals(len(test_dict_list), 4)
        assert_is_instance(test_dict_list[0], dict)
        os.remove("loadtest.csv")
        logger.info(test_dict_list)

    def load_json(self):
        self.dict_list.save_json("loadtest.json")

        test_dict_list = List.load_json("loadtest.json")

        assert_equals(len(test_dict_list), 4)
        assert_is_instance(test_dict_list[0], dict)

        os.remove("loadtest.json")
        logger.info(test_dict_list)

    def map(self):
        mapped_list = self.number_list.map(lambda x: x ** 2)

        logger.info(f"From {self.number_list}")
        logger.info(f"To   {mapped_list}")

        assert_equals(mapped_list[0], 1)
        assert_equals(mapped_list[8], 81)

    def save_csv(self):
        self.dict_list.save_csv("test.csv")
        assert_true(os.path.exists('test.csv'))
        with open("test.csv", "r") as f:
            assert_equals(f.read(), '''name,age,has_kids
Bob,23,True
Jim,12,False
Steve,57,True
Raphael,32,False''')
        os.remove("test.csv")
        assert_true(not os.path.exists('test.csv'))

    def save_json(self):
        self.dict_list.save_json("test.json")
        assert_true(os.path.exists('test.json'))
        with open("test.json", "r") as f:
            assert_equals(f.read(), json.dumps(self.dict_list))
        os.remove("test.json")
        assert_true(not os.path.exists('test.json'))

    def to_dict(self):
        dict1 = self.keys_list.zip(self.values_list).to_dict()
        assert_equals(dict1, {"key1": "value1", "key2": "value2", "key3": "value3"})

    def to_set(self):
        assert_is_instance(self.number_list.to_set(), set)
        assert_is_instance(self.number_list.to_set(), Set)

    def to_tuple(self):
        assert_is_instance(self.number_list.to_tuple(), tuple)
        assert_is_instance(self.number_list.to_tuple(), Tuple)

    def zip(self):
        dict1 = self.keys_list.zip(self.values_list)
        assert_equals(dict1, [("key1", "value1"), ("key2", "value2"), ("key3", "value3")])

    def zip_to(self):
        dict2 = self.keys_list.zip_to(self.values_list)
        assert_equals(dict2, [("value1", "key1"), ("value2", "key2"), ("value3", "key3")])

    def __init__(self):
        self.dict_list = List(
            [{"name": "Bob", "age": 23, "has_kids": True}, {"name": "Jim", "age": 12, "has_kids": False},
             {"name": "Steve", "age": 57, "has_kids": True}, {"name": "Raphael", "age": 32, "has_kids": False}])
        self.nested_number_list = List([1, 2, 3, [1, 2, 3], [[1, 4, 5], [6, 8, 9]]])
        self.number_list = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        self.str_list = List(["blue", "apple", "car", "kite", "rough", "idk"])
        self.keys_list = List(["key1", "key2", "key3"])
        self.values_list = List(["value1", "value2", "value3"])

        self.tests = [
            self.all,
            self.any,
            self.filter,
            self.find,
            self.find_or_default,
            self.flatten,
            self.is_empty,
            self.map,
            self.to_dict,
            self.to_set,
            self.to_tuple,
            self.save_csv,
            self.load_csv,
            self.save_json,
            self.load_json,
            self.zip,
            self.zip_to]
