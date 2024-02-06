FROM apache/apisix:3.8.0-debian
COPY --chown=636:636 conf /usr/local/apisix/conf/

USER root
RUN apt install -y wget && \
    wget https://github.com/api7/adc/releases/download/v0.2.0/adc_0.2.0_linux_amd64.tar.gz && \
    tar -zxvf adc_0.2.0_linux_amd64.tar.gz && \
    mv adc /usr/local/bin/adc
RUN mkdir -p /home/apisix && \
    chown -R apisix:apisix /home/apisix

USER apisix
COPY adc.yaml /home/apisix/.adc.yaml 
COPY routes.yaml /home/apisix/routes.yaml
COPY docker-entrypoint.sh /docker-entrypoint.sh