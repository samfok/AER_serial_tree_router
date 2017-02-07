#!/bin/tcsh

set minargs = 1
set maxargs = 1
if ($# < $minargs | $# > $maxargs) then
  echo "usage: postprocess_netlist.csh <netlist>"
  exit 1
endif 

set netlist = $1

# sed -i 's/^\(M.*\)/x\1/' ${netlist} || exit 1 # add params for LVS
sed -i 's/\(xtile__aer.*\)aer_brain_aer_TILE_AER/\1TileAER/' ${netlist} || exit 1 # unmangle TileAER name
# sed -i '/\.subckt TOP.*/{N;d}' ${netlist} || exit 1 # expose top level subckt contents
# sed -i '$d' ${netlist} || exit 1 # delete last line from top level subckt definition

exit 0
