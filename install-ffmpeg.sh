#!/bin/bash

RES=0

##################### Functions definition
function check_result {

  if [ "$1" -gt "0" ] ; then
    RES=1
    exit 1
  fi

}

# Install ffmpeg
echo "######################################"
echo "#   ffmpeg software installation     #"
echo "######################################"
echo "Fetching needed packages ..."
apt-get install ffmpeg -qq
check_result $?
echo "######################################"
echo "#             Done                   #"
echo "######################################"

exit $RES
