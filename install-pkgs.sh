#!/bin/bash

RES=0

##################### Functions definition
function check_result {

  if [ "$1" -gt "0" ] ; then
    RES=1
  fi

}

echo "########################################"
echo "# Packages deps installation           #"
echo "########################################"
# Install python
echo "Packages --> Preparing Python installation ..."
apt-get install python3 python-pip -q
check_result $?

# ffmpeg_pywrapper
echo "Packages --> ffmpeg_pywrapper for python ..."
python ./pkg/ffmpeg_pywrapper/setup.py install
check_result $?

echo "######################################"
echo "#             Done                   #"
echo "######################################"

exit $RES
