from typing import List
        
class Complexity:
    def __init__(self):
        self.reset()
        
    def add_time(self, time):
        self.time  += time
        
    def add_space(self, space):
        self.space  += space
        
    def reset(self):  
        self.space = 0
        self.time  = 0
        
    def out(self):
        print(self)
        
    def __str__(self):
        return f"complexity: space: {self.space}, time: {self.time}"

complexity = Complexity()

def scint(n: int) -> List[int]:
    """
    Visszaadja azokat a helyiértékeket (indexeket), ahol 1-esek állnak a szám bináris reprezentációjában (Big Endian). Ez felfogható egyfajta számábrázolásnak is. Példa:
    
    - n: 10 -> scint: [3,1]   mert: 10 = 2^3 + 2^1
    - n: 25 -> scint: [4,3,0] mert: 25 = 2^4 + 2^3 + 2^1
    - n: 1  -> scint: [0]     mert: 1  = 2^1
    
    Peremfeltétel: A reprezentáció Big Endian volt eredetileg is. Prototípus nem kezeli a Little Endiant.
    """
    scint_n = [bit_pos for bit_pos in range(n.bit_length() - 1,-1,-1) if n >> bit_pos & 1 == 1]
    
    complexity.add_time( n.bit_length() )
    complexity.add_space( sum([bit_pos.bit_length() for bit_pos in scint_n]) )
    
    return scint_n

import pytest

@pytest.mark.parametrize("n, expected", [
    (10, [3, 1]),
    (25, [4, 3, 0]),
    (1, [0]),
    (0, []),
    (255, [7, 6, 5, 4, 3, 2, 1, 0]),
    (1024, [10]),
    (1024 + 256 + 32 + 1, [10, 8, 5, 0]),
    (2048 + 512 + 256 + 32 + 1, [11, 9, 8, 5, 0]),
    (16*2048 + 4*2048 + 512 + 256 + 32 + 1, [15, 13, 9, 8, 5, 0])
])
def test_scint(n, expected):
    complexity.reset()
    scint_n = scint(n)
    assert scint_n == expected
    print(f"num: {n}")
    print(f"scint: {scint_n}")
    complexity.out()
    print()
    
from collections import defaultdict

def scint_pos_stats(scints, bit_position_index):
    """Felépíti a statisztikát: hány szám tartozik egy adott helyiértékhez a listában."""
    bit_position_quantities  = defaultdict(int)
    bit_position_scints      = defaultdict(list)
    
    for scint in scints:
        bit_position = scint[bit_position_index]
        bit_position_quantities[bit_position] += 1
        bit_position_scints[bit_position].append(scint)
   
    complexity.add_time( len(scints) ) #?
    complexity.add_space( sum([bit_pos_qty.bit_length() for bit_pos_qty in bit_position_quantities.values()]) )
   
    return bit_position_quantities, bit_position_scints

@pytest.mark.parametrize("nums, idx, expecteds", [
    ( [8+2, 16+8+1, 8+1], 0, [(4,1), (3,2)] ),
    ( [8+2, 16+8+1, 8+1], 1, [(3,1), (1,1), (0,1)] )
])
def test_scint_pos_stats(nums, idx, expecteds):
    print(f"nums: {nums}")
    complexity.reset()
    
    scints   = [scint(num) for num in nums]
    print(f"scints: {scints}")
    complexity.out()
    
    stats, _ = scint_pos_stats(scints, idx)    
    print(f"stats[{idx}]: {stats}")
    complexity.out()
    
    for pos, stat in expecteds:
        assert stats[pos] == stat
    print()