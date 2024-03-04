#!/bin/sh

echo "$(sed 's/${GW_A6SA_HOST}/'$GW_A6SA_HOST'/g' /etc/prometheus/prometheus.yml)" > /etc/prometheus/prometheus.yml
echo "$(sed 's/${GW_A6SA_METRICS_PORT}/'$GW_A6SA_METRICS_PORT'/g' /etc/prometheus/prometheus.yml)" > /etc/prometheus/prometheus.yml
echo "$(sed 's/${GW_A6DC_HOST}/'$GW_A6DC_HOST'/g' /etc/prometheus/prometheus.yml)" > /etc/prometheus/prometheus.yml
echo "$(sed 's/${GW_A6DC_METRICS_PORT}/'$GW_A6DC_METRICS_PORT'/g' /etc/prometheus/prometheus.yml)" > /etc/prometheus/prometheus.yml
echo "$(sed 's/${GW_KGDC_HOST}/'$GW_KGDC_HOST'/g' /etc/prometheus/prometheus.yml)" > /etc/prometheus/prometheus.yml
echo "$(sed 's/${GW_KGDC_METRICS_PORT}/'$GW_KGDC_METRICS_PORT'/g' /etc/prometheus/prometheus.yml)" > /etc/prometheus/prometheus.yml
echo "$(sed 's/${GW_KGSA_HOST}/'$GW_KGSA_HOST'/g' /etc/prometheus/prometheus.yml)" > /etc/prometheus/prometheus.yml
echo "$(sed 's/${GW_KGSA_METRICS_PORT}/'$GW_KGSA_METRICS_PORT'/g' /etc/prometheus/prometheus.yml)" > /etc/prometheus/prometheus.yml

/bin/prometheus $@