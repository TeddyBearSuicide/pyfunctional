from __future__ import annotations

import json
from typing import Callable, Any

import pyfunctional


class Dict(dict):

    def __getitem__(self, item):
        _obj = super(Dict, self).__getitem__(item)
        if isinstance(_obj, dict):
            return Dict(_obj)
        elif isinstance(_obj, list):
            return pyfunctional.List(_obj)
        elif isinstance(_obj, tuple):
            return pyfunctional.Tuple(_obj)
        elif isinstance(_obj, set):
            return pyfunctional.Set(_obj)

        return _obj

    def all(self, predicate: Callable[[Any, Any], bool] = None) -> bool:
        if predicate is None:
            return any(self)
        for k, v in self.items():
            if not predicate(k, v):
                return False
        return True

    def any(self, predicate: Callable[[Any, Any], bool]) -> bool:
        for k, v in self.items():
            if predicate(k, v):
                return True
        return False

    def filter(self, predicate: Callable[[Any, Any], bool]) -> Dict:
        new_dict = Dict()
        for k, v in self.items():
            if predicate(k, v):
                new_dict[k] = v
        return new_dict

    def first_key(self, predicate: Callable[[Any, Any], bool], default: Any = None):
        for k, v in self.items():
            if predicate(k, v):
                return k
        return default

    def first_value(self, predicate: Callable[[Any, Any], bool], default: Any = None):
        for k, v in self.items():
            if predicate(k, v):
                return v
        return default

    def is_empty(self):
        return len(self)

    def items(self):
        return pyfunctional.List(super(Dict, self).items())

    def keys(self):
        return pyfunctional.List(super(Dict, self).keys())

    @staticmethod
    def load_json(file_name):
        with open(file_name, 'r') as fp:
            _json = json.load(fp)

            if isinstance(_json, dict):
                return pyfunctional.Dict(_json)
            return None

    def map(self, transform: Callable[[Any, Any], Any]) -> pyfunctional.List:
        return pyfunctional.List([transform(k, v) for k, v in self.items()])

    def map_keys(self, transform: Callable[[Any, Any], Any]) -> Dict:
        return Dict({transform(k, v): v for k, v in self.items()})

    def map_values(self, transform: Callable[[Any, Any], Any]) -> Dict:
        return Dict({k: transform(k, v) for k, v in self.items()})

    def save_json(self, file_name: str):
        with open(file_name, "w") as fp:
            json.dump(self, fp)

    def values(self):
        return pyfunctional.List(super(Dict, self).values())
