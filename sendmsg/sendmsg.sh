#! /bin/bash

export PYTHONPATH=/home/ubuntu/LINE:$PYTHONPATH

cd /home/ubuntu/LINE/sendmsg
python sendmsg.py $1

