---
layout: post
title: Install Apache, MySQL, PHP on Ubuntu
tags: Linux Mysql Apache PHP
categories: Technology
public: true
---
## Install Apache and Allow in Firewall

~~~
sudo apt-get update
sudo apt-get install apache2
~~~

### Set Global ServerName to Suppress Syntax Warnings

checking your Apache configuration for syntax errors:

~~~
sudo apache2ctl configtest
~~~

Open up the main configuration file with your text edit:

~~~
sudo nano /etc/apache2/apache2.conf
~~~

Inside, at the bottom of the file, add a ServerName directive, pointing to your primary domain name. If you do not have a domain name associated with your server, you can use your server's public IP address:

>/etc/apache2/apache2.conf

~~~
. . .
ServerName server_domain_or_IP
~~~

Save and close the file when you are finished.

Next, check for syntax errors by typing:

~~~
sudo apache2ctl configtest
~~~

Restart Apache to implement your changes:

~~~
sudo systemctl restart apache2
~~~

### Adjust the Firewall to Allow Web Traffic

Make sure that UFW has an application profile for Apache like so:

~~~
sudo ufw app list
~~~

If you look at the Apache Full profile, it should show that it enables traffic to ports 80 and 443:

~~~
sudo ufw app info "Apache Full"
~~~

Allow incoming traffic for this profile:

~~~
sudo ufw allow in "Apache Full"
~~~

That’s it. To check if Apache is installed, direct your browser to your server’s IP address (eg. http://127.0.0.1). The page should display the words “It works!"

## Install MySQL

~~~
sudo apt-get install mysql-server
~~~

If you want to run a simple security script that will remove some dangerous defaults and lock down access to your database system a little bit. Start the interactive script by running:

~~~
sudo mysql_secure_installation
~~~

Setting the SQL Mode

The default SQL mode in MySQL 5.7 includes these modes: ONLY_FULL_GROUP_BY, STRICT_TRANS_TABLES, NO_ZERO_IN_DATE, NO_ZERO_DATE, ERROR_FOR_DIVISION_BY_ZERO, NO_AUTO_CREATE_USER, and NO_ENGINE_SUBSTITUTION.

If you want to disable permanently error sql_mode=only_full_group_by do those steps:

~~~
sudo nano /etc/mysql/my.cnf
~~~

Add this to the end of the file

~~~
[mysqld]  
sql_mode = "STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
sudo service mysql restart
~~~

This will disable ONLY_FULL_GROUP_BY for ALL users

~~~
mysql> SELECT @@secure_file_priv;
~~~

Disable secure-file-priv MySQL Ubuntu. Edit the file /etc/mysql/mysql.conf.d/mysqld.cnf and add the following line at the end:

~~~
secure_file_priv=""
~~~

## Install PHP

We're going to include some helper packages as well, so that PHP code can run under the Apache server and talk to our MySQL database:

~~~
sudo apt-get install php libapache2-mod-php php-mcrypt php-mysql
~~~

Currently, if a user requests a directory from the server, Apache will first look for a file called index.html. We want to tell our web server to prefer PHP files, so we'll make Apache look for an index.php file first.

To do this, type this command to open the dir.conf file in a text editor with root privileges:

~~~
sudo nano /etc/apache2/mods-enabled/dir.conf
~~~

It will look like this:

>/etc/apache2/mods-enabled/dir.conf

~~~
<IfModule mod_dir.c>
    DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm
</IfModule>
~~~

We want to move the PHP index file highlighted above to the first position after the DirectoryIndex specification

After this, we need to restart the Apache web server in order for our changes to be recognized. You can do this by typing this:

~~~
sudo systemctl restart apache2
~~~

We can also check on the status of the apache2 service using systemctl:

~~~
sudo systemctl status apache2
~~~

### Install PHP Modules

To enhance the functionality of PHP, we can optionally install some additional modules.

To see the available options for PHP modules and libraries, you can pipe the results of apt-cache search into less, a pager which lets you scroll through the output of other commands:

~~~
apt-cache search php- | less
~~~

If we decided that php-cli is something that we need, we could type:

~~~
sudo apt-get install php-cli
~~~

### Test PHP

Create the file at that location by typing:

~~~
sudo nano /var/www/html/info.php
~~~

Put the following text inside the file:

>info.php

~~~
<?php
phpinfo();
?>
~~~

he address you want to visit will be:

>http://your_server_IP_address/info.php

## Install phpMyAdmin

~~~
sudo apt-get install phpmyadmin apache2-utils
~~~

During the installation, phpMyAdmin will walk you through a basic configuration. Once the process starts up, follow these steps:

1. Select Apache2 for the server
1. Choose YES when asked about whether to Configure the database for phpmyadmin with dbconfig-common
1. Enter your MySQL password when prompted
1. Enter the password that you want to use to log into phpmyadmin

After the installation has completed, add phpmyadmin to the apache configuration.

~~~
sudo nano /etc/apache2/apache2.conf
~~~

Add the phpmyadmin config to the file.

>Include /etc/phpmyadmin/apache.conf

Restart apache:

~~~
sudo service apache2 restart
~~~

You can then access phpmyadmin by going to youripaddress/phpmyadmin.