#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: run.sh <topology>"
    echo "(do not include the file extension, e.g., 'run.sh foo' to use foo.txt)"
else
    python3 ../run_topo.py ../"$1".txt "$1".log
fi
