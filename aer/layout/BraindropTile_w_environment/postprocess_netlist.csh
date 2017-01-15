#!/bin/tcsh

set minargs = 1
set maxargs = 1
if ($# < $minargs | $# > $maxargs) then
  echo "usage: postprocess_netlist.csh <netlist>"
  echo "  Remember to run this on marvin, with ssh -X"
  exit 1
endif 

set netlist = $1

sed -i 's/^M/xM/' ${netlist} || exit 1 # fix transistor instance names
sed -i '1s/^/*defines a testbench for the BraindropTile\n\n/' ${netlist} || exit 1 # header
sed -i 's/aer_brain_aer_TILE_NRN_MEM/BraindropTileNeuronsMemory/' ${netlist} || exit 1 # align instance name
sed -i '/\.subckt TOP.*/{N;d}' ${netlist} || exit 1 # expose top level subckt contents
sed -i '$d' ${netlist} || exit 1 # delete last line from top level subckt definition

exit 0
