#! /bin/bash

export PYTHONPATH=/home/joe/Documents/LINE:$PYTHONPATH

# push and change to the directory this script resides
pushd `dirname $0`

# text are passed via parameters. it can include space.
# "$@" ensures each parameters are quoted as well
python sendmsg.py "$@"
popd
