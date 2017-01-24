#!/bin/tcsh

set minargs = 1
set maxargs = 1
if ($# < $minargs | $# > $maxargs) then
  echo "usage: create_cdl.csh <source_netlist>"
  exit 1
endif 

set source_netlist = $1
set netlist = ${source_netlist:s/spi/cdl/}

cp ${source_netlist} ${netlist} || exit 1 # copy spice to cdl

sed -i 's/^\(M.*\)$/\1 nf=1 p_la=0 ptwell=0/' ${netlist} || exit 1 # add params for LVS
sed -i '/\.subckt TOP.*/{N;d}' ${netlist} || exit 1 # expose top level subckt contents
sed -i '$d' ${netlist} || exit 1 # delete last line from top level subckt definition

exit 0
