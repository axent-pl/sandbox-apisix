#!/bin/sh

python3 /app/prepare.py 2>/dev/null | /app//bin/httpster -duration=1m -threads=4 1>/app/results/results.csv