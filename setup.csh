#!/bin/csh

set SCRIPT_PATH = `lsof +p $$ | \grep -oE /.\*setup.csh`
set SCRIPT_PATH = `dirname $SCRIPT_PATH`

setenv ACT_PATH `echo $SCRIPT_PATH | sed s@/aer@@`
setenv ACT_HOME `echo $SCRIPT_PATH | sed s@/aer@@`
