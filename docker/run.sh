#!/bin/bash

set -e

ACTION=$1
shift
PARAMS=$*
BRANCH="latest"

SCRIPT_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
cd $SCRIPT_DIR

if [[ "$OSTYPE" != "darwin"* ]] && [[ $(cat /proc/sys/vm/max_map_count) -lt 262144 ]]; then
  sudo sysctl -w vm.max_map_count=262144
fi

if [ -f /.dockerenv ]; then
    echo "Cannot run $0 inside a docker container"
    exit 2
fi

BRANCH=$(echo $BRANCH | sed 's/\///g')
export BRANCH
echo "Tag Name: $BRANCH"
COMPOSE="docker-compose -f docker-compose.yml $COMPOSE_ARGS"

usage() {
  PROG=`basename $0`
  echo "$PROG [<options>]"
  echo "    build [<service>] - Build docker containers"
  echo "    console - Build and connect to console"
  echo "    console_only - Connect to console"
  echo "    up - Start docker containers"
  echo "    start [<service>] - Start docker containers"
  echo "    stop [<service>] - Start docker containers"
  echo "    restart [<service>] - restart docker containers"
  echo "    rm [<service>] - Remove docker containers"
  echo "    logs [ [<service>] [<args>] - show logs of container"
  echo "    ports - show hosts and posts"
  echo "    apitest - run only apitest"
  echo "    migration - run only migration"
}

docker_build() {
  local service=$1
  $COMPOSE build $BUILD_ARG $service
}

docker_up() {
  $COMPOSE build $BUILD_ARG
  $COMPOSE up --remove-orphan --detach
}

docker_start() {
  local service=$1
  $COMPOSE start $service
}

docker_stop() {
  local service=$1
  $COMPOSE stop $service
}

docker_restart() {
  local service=$1
  $COMPOSE restart $service
}

docker_console() {
  local args=$@
  docker_up
  docker_console_only ${args[@]}
}

docker_console_only() {
  local cmd=${@:-/bin/bash}
  docker_run console ${cmd[@]}
}

_docker_test() {
  PARAM=$1
  set +e
  docker_console bash ./bin/test.sh  $PARAM
  local result=$?
  set -e
  if [ $result -ne 0 ]; then
      echo "ERROR: $PARAMS failed"
      docker_logs '*' '--tail=10'
      echo "ERROR: $PARAMS failed"
      exit $result
  fi
}

docker_migration() {
    _docker_test migration
    docker_console
}

docker_run() {
  local service=$1
  shift
  local cmd=$@
  docker_build $service
  $COMPOSE run $service ${cmd[@]}
}

docker_ps() {
  $COMPOSE ps
}

docker_rm() {
  local service=$1
  docker_stop $1
  $COMPOSE rm -f -v $service
}

docker_logs() {
  local service=$1
  local args='-f --tail=100'
  if [ ! -z "$service" ]; then
    shift
    args=$@
  fi
  if [ $service = '*' ];then
      unset service
  fi
  $COMPOSE logs ${args[@]} $service
}

docker_ports() {
  for c in `$COMPOSE ps -q`; do
    name=`docker inspect --format='{{index .Config.Labels "com.docker.compose.service"}}' $c`
    IFS=':' read -a ports <<< `docker inspect --format='{{range $p, $conf := .Config.ExposedPorts}}{{$p}}:{{end}}' $c | grep 'tcp' | sed -E 's/[^0-9:]//g'`
    for port in $ports; do
      echo "$name:$port"
    done
  done
}

case "x$ACTION" in
  xbuild|xup|xconsole|xconsole_only|xrun|xstart|xstop|xrestart|xrm|xps|xlogs|xports|xapitest|xpush|xmigration)
    docker_${ACTION} ${PARAMS[@]}
      ;;
  *) usage
    exit 1
    ;;
esac
