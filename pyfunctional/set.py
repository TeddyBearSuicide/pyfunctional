from __future__ import annotations

import pyfunctional
from pyfunctional.iterable import IndexIterator


class Set(IndexIterator, set):

    def to_list(self) -> pyfunctional.List:
        return pyfunctional.List(self)

    def to_tuple(self) -> pyfunctional.Tuple:
        return pyfunctional.Tuple(self)

