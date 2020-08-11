from __future__ import annotations

import pyfunctional
from pyfunctional.iterable import IndexIterator


class List(IndexIterator, list):

    def to_set(self) -> pyfunctional.Set:
        return pyfunctional.Set(self)

    def to_tuple(self) -> pyfunctional.Tuple:
        return pyfunctional.Tuple(self)
