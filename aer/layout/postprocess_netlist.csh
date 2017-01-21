#!/bin/tcsh

set minargs = 1
set maxargs = 1
if ($# < $minargs | $# > $maxargs) then
  echo "usage: postprocess_netlist.csh <netlist>"
  echo "  Remember to run this on marvin, with ssh -X"
  exit 1
endif 

set netlist = $1

exit 0
