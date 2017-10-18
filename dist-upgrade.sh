#!/bin/bash


##################### Functions definition
function check_result {
  echo "$RES"
  if [ "$1" -gt "0" ] ; then
    RES=1
    exit 1
  fi

}

KEYMAP=$1

# Upgrade to the last version
echo "######################################"
echo "# Distro upgrade to the last version #"
echo "######################################"
echo "This operation could take 30-60 minutes"
apt-get update -qq && apt-get upgrade -qq && apt-get dist-upgrade -qq
check_result $? "Error upgrading system"
if [ ! -z $KEYMAP ] ; then
  echo "Installing needed packages for keymap configuration"
  apt-get install console-data kbd -qq
  check_result $? "Error installing keymap!"
  loadkeys $KEYMAP
  check_result $? "Error setting keymap!"
fi
echo "######################################"
echo "#             Done                   #"
echo "######################################"
