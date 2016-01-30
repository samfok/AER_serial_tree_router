#!/bin/csh

rm -f a.prs
source setup.csh
cflat -DLAYOUT=true test/deserial_ring.act > a.prs
echo "source test/deserial_ring.scr" | \
prsim a.prs | \
sed -r -e "s/.*vec //" -e "s/.*\[n\]//" -e "s/x/ x/"
