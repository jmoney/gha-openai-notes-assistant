#!/bin/sh

pushd /app
python3 main.py --assistant $1 --file $2 > /tmp/output.txt
popd
mv /tmp/output.txt $3