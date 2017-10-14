#!/bin/bash

# Upgrade to the last version
echo "######################################"
echo "# Distro upgrade to the last version #"
echo "######################################"
echo "This operation could take 30-60 minutes"
apt-get update -qq && apt-get upgrade -qq && apt-get dist-upgrade -qq
echo "######################################"
echo "#             Done                   #"
echo "######################################"
