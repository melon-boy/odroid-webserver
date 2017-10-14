# odroid-webserver

## Description

A set of scripts to automate the installation and configuration of a web server composed by "nginx", "php5", "mysql" and "python" packages for **Odroid XU3/XU4 Debian jessie distribution** packed by meveric.

## Image download

Debian Jessie image from meveric is disponible for download [here](https://forum.odroid.com/viewtopic.php?f=96&t=17542).

## Scripts usage

### Get projet folder from git

* Login as user **root** into your Odroid installation.
* Install git package:

	```
	root@odroid-jessie:~# apt-get install git
	```
* Clone git repository:

	```
	root@odroid-jessie:~# git clone https://github.com/melon-boy/odroid-webserver
	```

### Parameters

Main script **configure.sh** gets some parameters:

* --hostname HOSTNAME: Replace HOSTNAME with your desired host name. This parameter is mandatory.
* --ip IP: Replace IP with your static ip address.
* --mask MASK: Replace MASK with your network mask.
* --gateway GW: Replace GW with your gateway ip address.  

If the **--ip** parameter is supplied **--mask** and **--gateway** parameters are mandatory.

If primary network configuration configuration is not supplied, network is configured in **dhcp** mode.

### Exemples

Script execution with **static network** configuration:

```
root@odroid-jessie:~/odroid-webserver/master# ./configure.sh --hostname foo-odroid --ip 192.168.1.30 --mask 255.255.255.0 --gateway 192.168.1.1
```

Script execution with **dhcp network** configuration:

```
root@odroid-jessie:~/odroid-webserver/master# ./configure.sh --hostname foo-odroid
```

**NOTA:** This configuration could take beetwen 30-60 minutes depending on your internet bandwith.

### Webserver test

In order to test our new server we can create an **index.php** file with **phpinfo()** function and point to the web address from our favourite navigator as follows:

```
root@odroid-jessie:~# echo "<?php phpinfo(); ?>" > /var/www/html/index.php
```

Finally, from our navigator we type:

```
http://<webserver ip address>/index.php
```

Our info php page has to be shown.

## What does the scripts do to my newly linux system?

The scripts do several things in order to hace the system updated and installed with needed packages.

Here is a list of things that the scripts do:

* Update and upgrade installation to the last packages version.
* Set new hostname.
* Change to custom network configuration.
* Creation of a new user **op** with password **toor**. This user is added to the sudoers group, so you have not to use **root** user.
* Install **Python** packeges.
* Install **ffmpeg** package.
* Install and configure **mysql** server and **php5** for **mysql**.
* Install and configure **nginx** webserver with **php5** support.

## Credits

Scripts created and tested by M. Espinosa © 2017 (themelonboy@themelonboy.com)
