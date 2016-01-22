#!/bin/sh
SCRIPT_PATH="${BASH_SOURCE[0]}";
pushd `dirname ${SCRIPT_PATH}` > /dev/null
SCRIPT_PATH=`pwd -P`;
popd  > /dev/null

export ACT_PATH="$SCRIPT_PATH:$SCRIPT_PATH/lib"
export ACT_HOME="$SCRIPT_PATH:$SCRIPT_PATH/lib"
