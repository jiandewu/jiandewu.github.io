---
layout: post
title: How do I auto-start jekyll?
tags: jekyll
categories: Technology
public: true
---
## Ubuntn 12.04

Your Software's files will spread across the filesystems, but you'll want to provide a simple and consistent interface to let the user at least start and stop it. Subsystems architecture promotes this ease-of-use, also providing a way (non obrigatoria) to be automatically started on system initialization. You just have to create your /etc/init.d script following a standard to make it functional.

~~~
#!/bin/sh
#
# /etc/init.d/jekyllmyblog
# Subsystem file for "jekyllmyblog" server
#
# chkconfig: 2345 95 05
# description: jekyllmyblog server daemon
#
# processname: jekyllmyblog
# config: /etc/jekyllmyblog/jekyllmyblog.conf
# config: /etc/sysconfig/jekyllmyblog
# pidfile: /var/run/jekyllmyblog.pid

# source function library
. /etc/rc.d/init.d/functions

# pull in sysconfig settings
[ -f /etc/sysconfig/jekyllmyblog ] && . /etc/sysconfig/jekyllmyblog

RETVAL=0
prog="jekyllmyblog"

start() {
	echo -n $"Starting $prog:"
	
	jekyll serve --watch --detach --source /media/sf_DropShare/Myblog/xxx.github.io --host 0.0.0.0
	
	RETVAL=$?
	[ "$RETVAL" = 0 ] && touch /var/lock/subsys/$prog
	echo
}

stop() {
	echo -n $"Stopping $prog:"

	killproc $prog -TERM
	RETVAL=$?
	[ "$RETVAL" = 0 ] && rm -f /var/lock/subsys/$prog
	echo
}

reload() {
	echo -n $"Reloading $prog:"
	killproc $prog -HUP
	RETVAL=$?
	echo
}

case "$1" in
	start)
		start
		;;
	stop)
		stop
		;;
	restart)
		stop
		start
		;;
	reload)
		reload
		;;
	condrestart)
		if [ -f /var/lock/subsys/$prog ] ; then
			stop
			# avoid race
			sleep 3
			start
		fi
		;;
	status)
		status $prog
		RETVAL=$?
		;;
	*)
		echo $"Usage: $0 {start|stop|restart|reload|condrestart|status}"
		RETVAL=1
esac
exit $RETVAL
~~~

You don't have to worry about managing the symbolic links in /etc/rc.d/rcN.d. The chkconfig command makes it for you, based on the control comments defined in the beginning of your script.

~~~
sudo chkconfig --add jekyllmyblog
sudo chkconfig --del jekyllmyblog
~~~

## Ubuntu 16.04

Created a shell script in `/etc/init.d/` called "jekyll-autorun" that looks like this:

~~~
#!/bin/sh

### BEGIN INIT INFO
# Provides: jekyll-autorun
# Required-Start: $local_fs $remote_fs $network $syslog $named
# Required-Stop: $local_fs $remote_fs $network $syslog $named
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# X-Interactive: false
# Short-Description: jekyll-autorun service
### END INIT INFO

# enable and run jekyll-autorun
systemctl enable jekyll-autorun.service
systemctl start jekyll-autorun.service

# update site
systemctl restart jekyll-autorun.service
~~~

Created a service in `/lib/systemd/system/` called "jekyll-autorun.service" that looks like this:

~~~
[Unit]
Description=jekyll autorun
ConditionPathExists=|/media/sf_DropShare/Myblog/xxx.github.io

[Service]
WorkingDirectory=/media/sf_DropShare/Myblog/xxx.github.io
ExecStart=/usr/local/bin/jekyll serve --incremental --watch --detach --source /media/sf_DropShare/Myblog/xxx.github.io --host 0.0.0.0
SyslogIdentifier=jekyll-autorun

[Install]
WantedBy=multi-user.target
~~~