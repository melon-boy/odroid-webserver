#!/bin/bash

RES=0

##################### Functions definition
function check_result {
  echo "$RES"
  if [ "$1" -gt "0" ] ; then
    RES=1
    exit 1
  fi

}

# Upgrade to the last version
echo "######################################"
echo "# Distro upgrade to the last version #"
echo "######################################"
echo "This operation could take 30-60 minutes"
apt-get update -qq && apt-get upgrade -q -y && apt-get dist-upgrade -q -y
check_result $? "Error upgrading system"
echo "Installing needed packages for keyboard layout configuration"
apt-get install console-data kbd console-setup keyboard-configuration -q -y
check_result $? "Error installing keymap!"
dpkg-reconfigure keyboard-configuration
check_result $? "Error configuring keyboard!"
echo "OK"
exit $RES
echo "######################################"
echo "#             Done                   #"
echo "######################################"
