# use this script to generate data for the unit tests
import numpy as np

OFFSET = 512
N = 256 

mem_in = []
mem_row_select_out = []
mem_col_select_out = []
mem_bl_out = []
for i in xrange(N):
  mem_in += [i]
  mem_row_select_out += [i % 8]
  mem_col_select_out += [(i/8) % 8]
  mem_bl_out += [i/8*2%16 +(i%128)/64]

mem_in = np.array(mem_in) + OFFSET
mem_row_select_out = np.array(mem_row_select_out)
mem_col_select_out = np.array(mem_col_select_out)
mem_bl_out = np.array(mem_bl_out)

np.savetxt('unit_brain_aerv_mem.in', mem_in, '%d')
np.savetxt('unit_brain_aerv_mem_row_select.out', mem_row_select_out, '%d')
np.savetxt('unit_brain_aerv_mem_col_select.out', mem_col_select_out, '%d')
np.savetxt('unit_brain_aerv_mem_bl.out', mem_bl_out, '%d')
