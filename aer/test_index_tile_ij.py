from index_tile_ij import *
import numpy as np
np.set_printoptions(threshold=np.nan, linewidth=np.nan)

M = 4
N = 4**M
L = 2**M
x = np.zeros((L, L))

for n in xrange(N):
    i, j = addr_flat_to_ij(n, M)
    print n, addr_flat_to_1of4(n, M), (i, j)
    x[i, j] = n

print x
