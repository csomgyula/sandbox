from typing import List

def scint(n: int) -> List[int]:
    """
    Visszaadja azokat a helyiértékeket (indexeket), ahol 1-esek állnak a szám bináris reprezentációjában (Big Endian).
    """
    return [i for i in range(n.bit_length() - 1,-1,-1) if n >> i & 1 == 1]

# Pytest teszt
import pytest

@pytest.mark.parametrize("n, expected", [
    (10, [3, 1]),
    (11, [3, 1, 0]),
    (25, [4, 3, 0]),
    (1, [0]),
    (0, []),
    (255, [7, 6, 5, 4, 3, 2, 1, 0]),
    (1024, [10])
])
def test_scint(n, expected):
    assert scint(n) == expected