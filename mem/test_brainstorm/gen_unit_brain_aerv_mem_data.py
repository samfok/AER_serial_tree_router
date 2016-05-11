# use this script to generate data for the unit tests
import numpy as np

OFFSET = 512
N = 256

mem_in = []
mem_row_select_out = []
mem_col_select_out = []
mem_write_out = []
for i in xrange(N):
  mem_in += [i]
  mem_row_select_out += [i % 8]
  mem_col_select_out += [(i/8) % 8]
  mem_write_out += [i / 64]

mem_in = np.array(mem_in) + OFFSET
mem_row_select_out = np.array(mem_row_select_out)
mem_col_select_out = np.array(mem_col_select_out)
mem_write_out = np.array(mem_write_out)

np.savetxt('unit_brain_aerv_mem.in', mem_in, '%d')
np.savetxt('unit_brain_aerv_mem_row_select.out', mem_row_select_out, '%d')
np.savetxt('unit_brain_aerv_mem_col_select.out', mem_col_select_out, '%d')
np.savetxt('unit_brain_aerv_mem_write.out', mem_write_out, '%d')
