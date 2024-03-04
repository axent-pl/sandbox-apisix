#!/usr/bin/env bash
set -Eeo pipefail

# added {{{
echo "$(sed 's/${KC_HOST}/'$KC_HOST'/g' /opt/kong/kong.yaml)" > /opt/kong/kong.yaml
echo "$(sed 's/${KC_PORT}/'$KC_PORT'/g' /opt/kong/kong.yaml)" > /opt/kong/kong.yaml
echo "$(sed 's/${ETL_KG_HOST}/'$ETL_KG_HOST'/g' /opt/kong/kong.yaml)" > /opt/kong/kong.yaml
echo "$(sed 's/${ETL_KG_PORT}/'$ETL_KG_PORT'/g' /opt/kong/kong.yaml)" > /opt/kong/kong.yaml
echo "$(sed 's/${UPSTREAM_HOST}/'$UPSTREAM_HOST'/g' /opt/kong/kong.yaml)" > /opt/kong/kong.yaml
echo "$(sed 's/${UPSTREAM_PORT}/'$UPSTREAM_PORT'/g' /opt/kong/kong.yaml)" > /opt/kong/kong.yaml

load_config() {
  SECONDS=0
  echo "[INFO ][axent-pl]: startup started"
  while true; do
    DURATION=$SECONDS
    if ! kong health 2>/dev/null; then
      echo "[INFO ][axent-pl]: healthcheck failed, retrying..."
      sleep 1
    else
      echo "[INFO ][axent-pl]: healthcheck successful"
      echo "[INFO ][axent-pl]: startup done in $DURATION seconds"
      break
    fi
  done
  if [[ "$KONG_DATABASE" == "postgres" ]]; then
    echo "[INFO ][axent-pl]: sync started"
    SECONDS=0
    deck gateway sync /opt/kong/kong-decoupled.yaml
    DURATION=$SECONDS
    echo "[INFO ][axent-pl]: sync done in $DURATION seconds"
  fi
}
load_config &
# }}}

# usage: file_env VAR [DEFAULT]
#    ie: file_env 'XYZ_DB_PASSWORD' 'example'
# (will allow for "$XYZ_DB_PASSWORD_FILE" to fill in the value of
# "$XYZ_DB_PASSWORD" from a file, especially for Docker's secrets feature)
file_env() {
  local var="$1"
  local fileVar="${var}_FILE"
  local def="${2:-}"
  # Do not continue if _FILE env is not set
  if ! [ "${!fileVar:-}" ]; then
    return
  elif [ "${!var:-}" ] && [ "${!fileVar:-}" ]; then
    echo >&2 "error: both $var and $fileVar are set (but are exclusive)"
    exit 1
  fi
  local val="$def"
  if [ "${!var:-}" ]; then
    val="${!var}"
  elif [ "${!fileVar:-}" ]; then
    val="$(< "${!fileVar}")"
  fi
  export "$var"="$val"
  unset "$fileVar"
}

export KONG_NGINX_DAEMON=${KONG_NGINX_DAEMON:=off}

if [[ "$1" == "kong" ]]; then

  all_kong_options="/usr/local/share/lua/5.1/kong/templates/kong_defaults.lua"
  set +Eeo pipefail
  while IFS='' read -r LINE || [ -n "${LINE}" ]; do
      opt=$(echo "$LINE" | grep "=" | sed "s/=.*$//" | sed "s/ //" | tr '[:lower:]' '[:upper:]')
      file_env "KONG_$opt"
  done < $all_kong_options
  set -Eeo pipefail

  file_env KONG_PASSWORD
  PREFIX=${KONG_PREFIX:=/usr/local/kong}

  if [[ "$2" == "docker-start" ]]; then
    kong prepare -p "$PREFIX" "$@"

    # remove all dangling sockets in $PREFIX dir before starting Kong
    LOGGED_SOCKET_WARNING=0
    for localfile in "$PREFIX"/*; do
      if [ -S "$localfile" ]; then
        if (( LOGGED_SOCKET_WARNING == 0 )); then
          printf >&2 'WARN: found dangling unix sockets in the prefix directory '
          printf >&2 '(%q) ' "$PREFIX"
          printf >&2 'while preparing to start Kong. This may be a sign that Kong '
          printf >&2 'was previously shut down uncleanly or is in an unknown state '
          printf >&2 'and could require further investigation.\n'
          LOGGED_SOCKET_WARNING=1
        fi
        rm -f "$localfile"
      fi
    done

    ln -sfn /dev/stdout $PREFIX/logs/access.log
    ln -sfn /dev/stdout $PREFIX/logs/admin_access.log
    ln -sfn /dev/stderr $PREFIX/logs/error.log

    exec /usr/local/openresty/nginx/sbin/nginx \
      -p "$PREFIX" \
      -c nginx.conf
  fi
fi

exec "$@"
