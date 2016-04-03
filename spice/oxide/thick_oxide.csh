#!/bin/tcsh

echo $1
if ($1 =~ eg*) then
  sed -i -e "s/xM3_ b a Vdd vpsub pfet W=0.135U L=0.03U/xM3_ b a Vdd vpsub egpfet W=0.160U L=0.150U/" $1 
  sed -i -e "s/xM10_ b a GND vnsub nfet W=0.09U L=0.03U/xM10_ b a GND vnsub egnfet W=0.160U L=0.150U/" $1 
endif

if ($1 =~ eg*eg*) then
  sed -i -e "s/xM4_ c b Vdd vpsub pfet W=0.135U L=0.03U/xM4_ c b Vdd vpsub egpfet W=0.160U L=0.150U/" $1 
  sed -i -e "s/xM11_ c b GND vnsub nfet W=0.09U L=0.03U/xM11_ c b GND vnsub egnfet W=0.160U L=0.150U/" $1 
endif
