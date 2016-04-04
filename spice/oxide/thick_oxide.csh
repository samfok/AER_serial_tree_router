#!/bin/tcsh

# convert to thick oxide models and parameters
if ($1 =~ eg*) then
  sed -i -e "s/xM3_ b a Vdd vpsub pfet W=0.135U L=0.03U/xM3_ b a Vdd vpsub egpfet W=0.160U L=0.150U/" $1 
  sed -i -e "s/xM10_ b a GND vnsub nfet W=0.09U L=0.03U/xM10_ b a GND vnsub egnfet W=0.160U L=0.150U/" $1 
endif

if ($1 =~ eg*eg*) then
  sed -i -e "s/xM4_ c b Vdd vpsub pfet W=0.135U L=0.03U/xM4_ c b Vdd vpsub egpfet W=0.160U L=0.150U/" $1 
  sed -i -e "s/xM11_ c b GND vnsub nfet W=0.09U L=0.03U/xM11_ c b GND vnsub egnfet W=0.160U L=0.150U/" $1 
endif

# add separate power rail
sed -i -e "s/xM3_ b a Vdd/Vdd2 Vdd2 0 dc 1.0v\n.print in(vdd2)\n&/" $1 
# connect neuron inverters to separate power rail
sed -i -e "s/xM3_ b a Vdd/xM3_ b a Vdd2/" $1 
sed -i -e "s/xM4_ c b Vdd/xM4_ c b Vdd2/" $1 
sed -i -e "s/xM5_ aext_2__xp_00_1 c Vdd/xM5_ aext_2__xp_00_1 c Vdd2/" $1 
