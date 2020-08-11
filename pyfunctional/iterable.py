from __future__ import annotations
import json
import pyfunctional

from typing import Any, Callable, TypeVar, Iterable

T = TypeVar("T")


class IndexIterator(object):

    def __iter__(self):
        return super().__iter__()

    def __getitem__(self, item):
        item = super().__getitem__(item)

        if isinstance(item, dict):
            item = pyfunctional.Dict(item)
        elif isinstance(item, list):
            item = pyfunctional.List(item)
        elif isinstance(item, set):
            item = pyfunctional.Set(item)
        elif isinstance(item, tuple):
            pass

        return item

    def __len__(self):
        return super().__len__()

    def all(self, predicate: Callable[[Any], bool]) -> bool:
        for item in self:
            if not predicate(item):
                return False
        return True

    def any(self, predicate: Callable[[Any], bool]) -> bool:
        for item in self:
            if predicate(item):
                return True
        return False

    def filter(self, predicate: Callable[[Any], bool]) -> IndexIterator:
        return type(self)(filter(predicate, self))

    def find(self, predicate: Callable[[Any], bool]) -> Any:
        return self.find_or_default(predicate, None)

    def find_or_default(self, predicate: Callable[[Any], bool], default: Any) -> Any:
        for item in self:
            if predicate(item):
                return item
        return default

    @classmethod
    def _flatten(cls, _iter: Iterable) -> list:
        new_list = list()
        for item in _iter:
            if hasattr(item, "__iter__"):
                new_list.extend(cls._flatten(item))
                continue
            new_list.append(item)
        return new_list

    def flatten(self) -> IndexIterator:
        return type(self)(self._flatten(self))

    def is_empty(self):
        return len(self) == 0

    @staticmethod
    def load_csv(file_name: str, delimiter=",", headers: bool = True):
        lines = None
        with open(file_name) as fp:
            lines = pyfunctional.List(fp.readlines()).map(lambda line: line.strip())

        if headers:
            keys = lines[0].split(delimiter)
            return lines[1:].map(lambda line: pyfunctional.List(line.split(delimiter)).zip_to(keys).to_dict())

        else:
            return lines[1:].map(lambda line: line.split(delimiter))

    @staticmethod
    def load_json(file_name: str):
        with open(file_name, 'r') as fp:
            _json = json.load(fp)

            if isinstance(_json, list):
                return pyfunctional.List(_json)
            return None

    def map(self, transform: Callable[[Any], Any]) -> IndexIterator:
        return type(self)(map(transform, self))

    def save_csv(self, file_name: str, delimiter=",", headers=True):
        if not self.is_empty():
            lines = []

            if isinstance(self[0], dict):
                lines.append(delimiter.join(self[0].keys())) if headers else None
                self.map(lambda x: lines.append(delimiter.join(pyfunctional.List(x.values()).map(str))))

            with open(file_name, "w") as f:
                f.write('\n'.join(lines))

    def save_json(self, file_name: str):
        with open(file_name, "w") as fp:
            json.dump(self, fp)

    def to_dict(self):
        return pyfunctional.Dict(self)

    def zip(self, _iterable: Iterable):
        return pyfunctional.List(zip(self, _iterable))

    def zip_to(self, _iterable: Iterable):
        return pyfunctional.List(zip(_iterable, self))
