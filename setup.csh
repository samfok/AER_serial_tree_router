#!/bin/csh

set SCRIPT_PATH = `lsof +p $$ | \grep -oE /.\*setup.csh`
set SCRIPT_PATH = `dirname $SCRIPT_PATH`

setenv ACT_PATH $SCRIPT_PATH"/act:$SCRIPT_PATH/act/lib"
setenv ACT_HOME $SCRIPT_PATH"/act:$SCRIPT_PATH/act/lib"
