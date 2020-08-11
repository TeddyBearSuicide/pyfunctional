from __future__ import annotations

import pyfunctional
from pyfunctional.iterable import IndexIterator


class Tuple(IndexIterator, tuple):

    def to_list(self) -> pyfunctional.List:
        return pyfunctional.List(self)

    def to_set(self) -> pyfunctional.Set:
        return pyfunctional.Set(self)
