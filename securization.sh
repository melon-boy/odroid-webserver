#!/bin/bash

HOST=$1
IP=$2
MASK=$3
GW=$4
USER='op'
PASS='toor'
RES=0

##################### Functions definition
function check_result {

  if [ "$1" -gt "0" ] ; then
    RES=1
  fi

}

echo "######################################"
echo "#            Securization            #"
echo "######################################"
# Change hostname for the cluster's master
echo "Securization --> Configuring master hostname to <$HOST>"
echo $HOST > /etc/hostname
sed -i -e "s/odroid-jessie/$HOST master/g" /etc/hosts
check_result $?
echo "Securization --> Network configuration"
# dhcp configuration
if [ -z $IP ] ; then
  cp -f ./etc/network/interfaces.dhcp /etc/network/interfaces

# static configuration
else
  cp -f ./etc/network/interfaces.static /tmp/interfaces
  check_result $?
  sed -i -e "s/IP_ADDRESS/$IP/g" /tmp/interfaces
  check_result $?
  sed -i -e "s/MASK/$MASK/g" /tmp/interfaces
  check_result $?
  sed -i -e "s/GATEWAY/$GW/g" /tmp/interfaces
  check_result $?
  cp -f /tmp/interfaces /etc/network/.
  check_result $?
  route add default gw $GW
  check_result $?
fi

echo "Securization --> Restarting networking service"
service networking restart
check_result $?
if [ "$?" -eq "0" ] ; then
  ifup eth0
fi

echo "Securization --> Installing previous dependencies"
apt-get install sudo whois -qq
check_result $?

echo "Securization --> Adding new user <op> with password <toor>"
useradd -p $(mkpasswd $PASS) -s /bin/bash -G sudo -d /home/$USER -m $USER
check_result $?

echo "######################################"
echo "#             Done                   #"
echo "######################################"


exit $RES
