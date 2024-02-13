#!/bin/bash

python3 tools/test/prepare.py 2>/dev/null | ../axent/httpster/bin/httpster -duration=5s -threads=4