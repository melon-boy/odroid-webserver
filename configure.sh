#!/bin/bash

HOST=""
IP=""
MASK=""
GW=""

##################### Functions definition
function abort {
  echo "ABORTED"
  exit 1
}

function get_opts {

  PARAM1=$1
  PARAM2=$2

  OPTIONS=h:i:m:g:
  LONGOPTIONS=hostname:,ip:,mask:,gateway:

  PARSED=$(getopt --options=$OPTIONS --longoptions=$LONGOPTIONS --name "$PARAM1" -- "$PARAM2")

  eval set -- "$PARSED"

  while true; do
    case "$1" in
        -h|--hostname)
           HOST="$2"
           echo "getopt HOST: $HOST"
           shift 2
           ;;
        -i|--ip)
           IP="$2"
           shift 2
           ;;
        -m|--mask)
           MASK="$2"
           shift 2
           ;;
        -g|--gateway)
          GW="$2"
          shift 2
          ;;
        --)
          shift
          break
          ;;
        *)
          abort
          ;;
      esac
  done


}

function _wait {

  COUNT=$1

  for i in `seq 1 $COUNT` ;
  do
      echo "Next task comming in $(($COUNT+1-$i)) seconds. (Ctrl+c to interrupt execution)"
      sleep 1
  done

}

function _reboot {

  COUNT=$1

  for i in `seq 1 $COUNT` ;
  do
      echo "Reboot in $(($COUNT+1-$i)) seconds. (shutdown -c in other terminal to cancel.)"
      sleep 1
  done

  shutdown -r
}

function check_result {

  RES=$1

  if [ "$RES" -eq "0" ] ; then
    echo "OK"
  else
    echo "Errors encountered while the script execution."
    abort
  fi
}

function print_usage {

  echo "Usage:"
  echo "./configure.sh --hostname HOSTNAME [--ip IP --mask MASK --gateway GW]"
  echo "More info at https://github.com/melon-boy/odroid-webserver/README.md"

}

##################### Main execution
# Parse arguments
get_opts $0 $@
echo "HOST: $HOST"
if [ -z $HOST ] ; then
  echo "Hostname parameter missing."
  print_usage
  abort
fi

if [ ! -z $IP ] ; then
  if [ -z $MASK ] || [ -z $GW ] ; then
    echo "Network configuration is not complete. Some parameters are missing."
    print_usage
    abort
  fi
fi

# Execution of diferent scripts to configure the distro.
./dist-upgrade.sh
check_result $?
_wait 10
# securization with hostname, ip address, mask and gateway parameters.
./securization.sh $HOST $IP $MASK $GW
check_result $?
_wait 10
./install-ffmpeg.sh
check_result $?
_wait 10
./install-pkgs.sh
check_result $?
_wait 10
./install-webserver.sh
check_result $?
echo "Finished! Scripts developed by M. Espinosa (c) 2017"
# Reboot needed in 10 seconds
echo "Reboot is needed: please run apt-get autoremove after system starts."
_reboot 10