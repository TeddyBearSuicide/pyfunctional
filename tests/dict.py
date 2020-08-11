import json
import os

from unittrial import TestCase, logger
from unittrial.assertions import assert_true, assert_false, assert_equals, assert_is_none, assert_is_instance

from pyfunctional import Dict


class DictTests(TestCase):

    def all(self):
        assert_true(self.all_test_dict.all(lambda k, v: isinstance(v, str)))
        assert_false(self.all_test_dict.all(lambda k, v: isinstance(v, int)))

    def any(self):
        assert_true(self.any_test_dict.any(lambda k, v: isinstance(v, str)))
        assert_true(self.any_test_dict.any(lambda k, v: isinstance(v, int)))
        assert_false(self.any_test_dict.any((lambda k, v: isinstance(v, float))))

    def filter(self):
        assert_equals(self.any_test_dict.filter(lambda k, v: isinstance(v, int))["key4"], 3)

    def first_key(self):
        assert_equals(self.all_test_dict.first_key(lambda k, v: k.endswith("3")), "key3")
        assert_is_none(self.all_test_dict.first_key(lambda k, v: k.endswith("6")))
        assert_equals(self.all_test_dict.first_key(lambda k, v: k.endswith("6"), "NotFound"), "NotFound")

    def first_value(self):
        assert_equals(self.all_test_dict.first_value(lambda k, v: k.endswith("3")), "strawberry")
        assert_is_none(self.all_test_dict.first_value(lambda k, v: k.endswith("6")))
        assert_equals(self.all_test_dict.first_value(lambda k, v: k.endswith("6"), "NotFound"), "NotFound")

    def load_json(self):
        self.any_test_dict.save_json("loadtest.json")

        test_dict = Dict.load_json("loadtest.json")

        assert_equals(len(test_dict), 4)
        assert_is_instance(test_dict, dict)

        os.remove("loadtest.json")
        logger.info(test_dict)

    def map(self):
        assert_equals(self.all_test_dict.map(lambda k, v: k + "test"), ["key1test", "key2test", "key3test"])

    def map_keys(self):
        assert_equals(self.all_test_dict.map_keys(lambda k, v: int(k[-1])), {1: "apple", 2: "orange", 3: "strawberry"})

    def map_values(self):
        assert_equals(self.all_test_dict.map_values(lambda k, v: v[0]), {"key1": "a", "key2": "o", "key3": "s"})

    def save_json(self):
        self.any_test_dict.save_json("test.json")
        assert_true(os.path.exists('test.json'))
        with open("test.json", "r") as f:
            assert_equals(f.read(), json.dumps(self.any_test_dict))
        os.remove("test.json")
        assert_true(not os.path.exists('test.json'))

    def __init__(self):
        self.all_test_dict = Dict({"key1": "apple", "key2": "orange", "key3": "strawberry"})
        self.any_test_dict = Dict({"key1": "apple", "key2": "orange", "key3": "strawberry", "key4": 3})

        self.tests = [
            self.all,
            self.any,
            self.filter,
            self.first_key,
            self.first_value,
            self.map,
            self.map_keys,
            self.map_values,
            self.save_json,
            self.load_json
        ]
