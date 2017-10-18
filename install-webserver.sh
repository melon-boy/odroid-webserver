#!/bin/bash


RES=0

##################### Functions definition
function check_result {

  if [ "$1" -gt "0" ] ; then
    RES=1
    echo $2
    exit 1
  fi

}

echo "##########################################"
echo "# Webserver installation & configuration #"
echo "##########################################"
# Install nginx server with php and mysql
echo "Webserver --> Installing mysql and php5-mysql"
apt-get install mysql-server php5-mysql -qq
check_result $? "Error installing mysql"
# Password root for mysql => same as root user
echo "Webserver --> Configure mysql database"
mysql_install_db
/usr/bin/mysql_secure_installation
echo "Webserver --> Installing nginx server"
apt-get install nginx -qq
check_result $? "Error installing nginx server"
echo "Webserver --> Starting nginx service"
service nginx start
check_result $? "Error starting nginx service"
echo "Webserver --> Installing php for nginx"
apt-get install php5-fpm -qq
check_result $? "Error installing php for nginx"
echo "Webserver --> Configuring php for nginx"
cp -f ./etc/php5/fpm/php.ini /etc/php5/fpm/.
cp -f ./etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/.
echo "Webserver --> Restarting php for nginx service"
service php5-fpm restart
check_result $? "Error restarting php for nginx service"
echo "Webserver --> Configuring nginx with php"
cp -f ./etc/nginx/sites-available/default /etc/nginx/sites-available/.
echo "Webserver --> Restarting nginx service"
service nginx restart
check_result $? "Error restarting nginx service"
echo "######################################"
echo "#             Done                   #"
echo "######################################"

exit $RES
