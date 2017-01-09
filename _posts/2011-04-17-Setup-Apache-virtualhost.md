---
layout: post
title: Set Up Apache Virtual Hosts
tags: Apache
categories: Technology
public: true
---
In your web page root, create a file `apache.conf`. eg:

~~~
Alias "/bsmat" "/media/sf_DropShare/BSMAT/bsmatrelease/release"

<Directory "/media/sf_DropShare/BSMAT/bsmatrelease/release">
   Options Indexes FollowSymLinks
   AllowOverride None
   Require all granted
</Directory>
~~~

For Apache 2.4, add a line in `\etc\apache2\apache2.conf`

~~~
Include /media/sf_DropShare/BSMAT/bsmatrelease/release/apache.conf
~~~

Restart Apache to implement your changes:

~~~
sudo service apache2 restart
~~~

~~~
Listen 8092
<VirtualHost *:8092>
	ServerAdmin webmaster@localhost
	ServerName jdwu.me
	DocumentRoot /media/sf_DropShare/BSMAT/BSMATv0

        <Directory /media/sf_DropShare/BSMAT/BSMATv0>
        	Options Indexes FollowSymLinks MultiViews
        	AllowOverride All
        	Require all granted
        </Directory>

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
~~~

However, this is not over yet. At the moment, you are probably welcome with a forbidden error message.

This error is due to the owner and group of the web page folder. Apache expects the files to render to belong to the group `www-data`. If the folder belongs to the `vboxsf` user. you need add this user to the www-data group

~~~
nano /etc/group
~~~

and edit the line that says `vboxsf:x:1001:` to replace it with the following:

~~~
vboxsf:x:1001:www-data
~~~
[](http://jimmybonney.com/articles/configure_virtualbox_shared_folder_apache_virtual_host/)

Make sure the underlying file system permissions allow the User/Group under which Apache is running to access the necessary files. In the case where file system permission are at fault, remember that not only must the directory and files in question be readable, but also all parent directories must be at least searchable by the web server in order for the content to be accessible. For example `/home/httpd/theos.in/` must be searchable, enter:

~~~
sudo chmod +x /home/httpd/theos.in/
~~~