from unittrial import run_tests

from pyfunctional import List, Tuple
from tests.dict import DictTests
from tests.iterable import IndexIteratorTests

if __name__ == '__main__':
    number_list = Tuple(List([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    run_tests([
        IndexIteratorTests(),
        DictTests()
    ])

