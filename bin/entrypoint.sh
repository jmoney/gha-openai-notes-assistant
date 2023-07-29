#!/bin/sh

set -x
python3 /app/main.py --assistant $1 --file $2 > $3