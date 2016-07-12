"""
addr formats and conversions
flat <=> 1of4 <=> ij
"""
import numpy as np
np.set_printoptions(linewidth=150)

def sweep_space(m):
    """Generate all addresses in m long 1of4 space"""
    rows = 4**m
    cols = m
    addrs = np.zeros((rows, cols), dtype=int)
    cycle = 1
    for j in xrange(cols):
        for i in xrange(rows):
            addrs[i,j] = (i / cycle) % 4
        cycle *= 4
    addrs = addrs[:,::-1]
    addrs_str = [''.join(map(str,addr)) for addr in addrs]
    return addrs, addrs_str

def addr_1of4_to_ij(addr_1of4):
    """Converts address from 1of4 to i,j"""
    words = len(addr_1of4)
    addrs = 4**words
    ijlen = 2**words
    addr_i = 0
    addr_j = 0
    for word in addr_1of4:
        ijlen /= 2
        addr_i += word%2 * ijlen
        addr_j += word/2 * ijlen
    return addr_i, addr_j

def addr_ij_to_1of4(addr_ij, words):
    """Converts address from i,j to 1of4"""
    i, j = addr_ij
    ijlen = 2**words
    addr_1of4 = []
    for w in xrange(words):
        ijlen /= 2
        addr_1of4.append(i/ijlen % 2 + 2*(j/ijlen % 2))
    return addr_1of4

def addr_1of4_to_flat(addr_1of4):
    """Converts address from 1of4 to flat"""
    addr_flat = 0
    words = len(addr_1of4)
    addrs = 4**words
    for word in addr_1of4:
        addrs /= 4
        addr_flat += word*addrs
    return addr_flat

def addr_flat_to_1of4(addr_flat, words):
    """Converts address from flat to 1of4"""
    flatlen = 4**words
    addr_1of4 = []
    for w in xrange(words):
        flatlen /= 4
        addr_1of4.append(addr_flat/flatlen % 4)
    return addr_1of4

def addr_flat_to_ij(addr_flat, words):
    """Converts address from flat to ij"""
    addr_i, addr_j = addr_1of4_to_ij(addr_flat_to_1of4(addr_flat, words))
    return addr_i, addr_j

def addr_ij_to_flat(addr_ij, words):
    """Converts address from flat to ij"""
    addr_flat = addr_1of4_to_flat(addr_ij_to_1of4(addr_flat, words))
    return addr_flat

def make_addr_1of4_grid_1of4_to_ij(m):
    """Builds a 2d grid of 1of4 addr by converting 1of4 addr to ij addr"""
    addrs, addrs_str = sweep_space(m)
    ijlen = 2**m
    addr_1of4_grid = np.zeros((ijlen, ijlen), dtype='|S{}'.format(m))
    for addr, addr_str in zip(addrs, addrs_str):
        i, j = addr_1of4_to_ij(addr)
        addr_1of4_grid[i,j] = addr_str
    return addr_1of4_grid

def make_addr_1of4_grid_ij_to_1of4(m):
    """Builds a 2d grid of 1of4 addr by converting ij addr to 1of4 addr"""
    addrs, addrs_str = sweep_space(m)
    ijlen = 2**m
    addr_1of4_grid = np.zeros((ijlen, ijlen), dtype='|S{}'.format(m))
    for i in xrange(ijlen):
        for j in xrange(ijlen):
            addr_1of4 = addr_ij_to_1of4((i, j), m)
            addr_1of4_grid[i,j] = ''.join(map(str, addr_1of4))
    return addr_1of4_grid

def make_addr_1of4_array_1of4_to_flat(m):
    """Builds an array of 1of4 addr by converting 1of4 addr to flat addr"""
    addrs_1of4, addrs_1of4_str = sweep_space(m)
    addr_1of4_array = np.zeros(4**m, dtype='|S{}'.format(m))
    for addr_1of4, addr_1of4_str in zip(addrs_1of4, addrs_1of4_str):
        addr_flat = addr_1of4_to_flat(addr_1of4)
        addr_1of4_array[addr_flat] = addr_1of4_str
    return addr_1of4_array

def make_addr_1of4_array_flat_to_1of4(m):
    """Builds an array of 1of4 addr by converting flat addr to 1of4 addr"""
    addrs_1of4, addrs_1of4_str = sweep_space(m)
    array_len = 4**m
    addr_1of4_array = np.zeros(array_len, dtype='|S{}'.format(m))
    for i in xrange(array_len):
        addr_1of4 = addr_flat_to_1of4(i, m)
        addr_1of4_array[i] = ''.join(map(str, addr_1of4))
    return addr_1of4_array

def test(m):
    addr_1of4_grid_1of4_to_ij = make_addr_1of4_grid_1of4_to_ij(m)
    addr_1of4_grid_ij_to_1of4 = make_addr_1of4_grid_ij_to_1of4(m)
    print addr_1of4_grid_1of4_to_ij
    print addr_1of4_grid_ij_to_1of4
    assert np.all(
        addr_1of4_grid_1of4_to_ij == addr_1of4_grid_ij_to_1of4)
    
    addr_1of4_array_1of4_to_flat = make_addr_1of4_array_1of4_to_flat(m)
    addr_1of4_array_flat_to_1of4 = make_addr_1of4_array_flat_to_1of4(m)
    print addr_1of4_array_1of4_to_flat
    print addr_1of4_array_flat_to_1of4
    assert np.all(
        addr_1of4_array_1of4_to_flat == addr_1of4_array_flat_to_1of4)

for m in xrange(6):
    test(m)
