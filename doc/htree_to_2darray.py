import numpy as np
np.set_printoptions(linewidth=150)

def sweep_space(m):
    rows = 4**m
    cols = m
    words = np.zeros((rows, cols), dtype=int)
    cycle = 1
    for j in xrange(cols):
        for i in xrange(rows):
            words[i,j] = (i / cycle) % 4
        cycle *= 4
    return words[:,::-1]

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


def test_addr_1of4_to_ij(m):
    """Tests addr_1of4_to_ij"""
    addrs = sweep_space(m)
    addrs_str = [''.join(map(str,addr)) for addr in addrs]
    ijlen = 2**m
    
    addr_1of4_grid = np.zeros((ijlen, ijlen), dtype='|S{}'.format(m))
    
    for addr, addr_str in zip(addrs, addrs_str):
        i, j = addr_1of4_to_ij(addr)
        addr_1of4_grid[i,j] = addr_str
    
    return addr_1of4_grid

def test_addr_ij_to_1of4(m):
    """Tests addr_ij_to_1of4"""
    addrs = sweep_space(m)
    addrs_str = [''.join(map(str,addr)) for addr in addrs]
    ijlen = 2**m
    
    addr_1of4_grid = np.zeros((ijlen, ijlen), dtype='|S{}'.format(m))
    
    for i in xrange(ijlen):
        for j in xrange(ijlen):
            addr_1of4 = addr_ij_to_1of4((i, j), m)
            addr_1of4_grid[i,j] = ''.join(map(str, addr_1of4))
    
    return addr_1of4_grid

for m in xrange(6):
    # print test_addr_1of4_to_ij(m)
    # print test_addr_ij_to_1of4(m)
    assert np.all(test_addr_1of4_to_ij(m) == test_addr_ij_to_1of4(m))
