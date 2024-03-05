#!/bin/sh

# 

if [ "$1" = "httpster" ];
then
    TEST_DURATION=$2
    TEST_THREADS=$3
    python3 /app/prepare.py 2>/dev/null | /app/bin/httpster -duration=$TEST_DURATION -threads=$TEST_THREADS 1>/app/results/results.csv
elif [ "$1" = "wrk" ];
then
    TEST_DURATION=$2
    TEST_THREADS=$3
    TEST_CONNECTIONS=$4
    TEST_ORIGIN=$5
    TEST_TOKEN=$(python3 /app/prepare_token.py)
    GW_SERVICE_HOST=adagio-angora.gateway.bank
    GW_SERVICE_PATH=/anything/of-foo
    wrk --duration $TEST_DURATION --threads $TEST_THREADS --connections $TEST_CONNECTIONS -H "Authorization: ${TEST_TOKEN}" -H "Host: $GW_SERVICE_HOST" $TEST_ORIGIN$GW_SERVICE_PATH >/app/results/results-wrk.csv
fi