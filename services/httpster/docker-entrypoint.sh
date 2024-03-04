#!/bin/sh

python3 /app/prepare.py
# 2>/dev/null | ../axent/httpster/bin/httpster -duration=2m -threads=4