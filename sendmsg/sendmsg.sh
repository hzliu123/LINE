#! /bin/bash

export PYTHONPATH=/home/ubuntu/LINE:$PYTHONPATH

# push and change to the directory this script resides
pushd `dirname $0`
python sendmsg.py "$1" "$2" "$3" "$4"
popd
