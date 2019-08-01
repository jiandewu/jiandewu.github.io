---
layout: post
title: Pure Ubuntu setup
tags: Linux
categories: Technology
public: true
---

## Make Ubuntu to run without GUI

You have to un-install the only display manager installed to your system. It would be lightdm display manager. so to remove it execute this command:

~~~
sudo apt-get remove lightdm
~~~

Then restart your system with:

~~~
sudo reboot
~~~

Your system will start in CLI mode. You may have to press Ctrl+Alt+F1 to go to CLI tty1 mode.

Revert Back to GUI Mode

Again install the display manager to get the display. Use following command to do so:

~~~
sudo apt-get install lightdm
~~~

and restart your system.

## Installation of OpenSSH in Linux

To install OpenSSH, open a terminal and run the following commands with superuser permissions.

~~~
$ sudo apt-get install openssh-server openssh-client
~~~

Do you like to make your openssh server display a nice login banner? You can do it by modifying the content of /etc/issue.net file and adding the following line inside the sshd configuration file.

~~~
Banner /etc/issue.net
~~~

## VirtualBox 端口转发
宿主机和宿主机网络中的任何主机都不能直接访问虚拟主机，但是VirtualBox 提供了端口转发，使得我们可以设置特定的端口供实体网络访问。宿主机IP地址就127.0.0.1

## Mount VirtualBox Shared Folder on Ubuntu
Mounting VirtualBox shared folders is easy on Linux guest OS. If you enabled Auto-mount while creating shared folder then it should automatically be mounted to /media/USER/sf_ShareName or /media/sf_ShareName, depending on your guest OS.

You may encounter permissions issues when trying to access VirtualBox shared folder on Ubuntu (or other Linux distros).

To mount VirtualBox shared folder on Ubuntu and access everything within the shared folder as the user, you will have to manually add the user to `vboxsf` group using the following command:

~~~
sudo usermod -a -G vboxsf username
~~~

Of course, replace username with your username. Once done, the user will have read/write access to the VBox shared folder. For easy access / convenience, you may create a symbolic link to the mounted shared folder in your home folder:

~~~
sudo ln -s /media/sf_Share ~/Share
~~~

Note that /media/sf_Share could be /media/USER/sf_Share depending on how your Linux OS mounts VBox shared folder. Also, replace USER with your username. Once done, you will have a symbolic link created to the Vbox VM shared folder in your home directory

Manual mounting, use the following command:

~~~
mount -t vboxsf [-o OPTIONS] sharename mountpoint
~~~
eg:

~~~
sudo mount -t vboxsf -o rw,uid=33,gid=33 DropShare /media/sf_DropShare
~~~

To mount a shared folder during boot, add the following entry to `/etc/fstab`:

~~~
sharename  mountpoint  vboxsf  defaults 0  0
~~~

eg:

~~~
DropShare  /media/sf_DropShare  vboxsf  rw,uid=33,gid=33  0  0
~~~

`/etc/fstab` needs to have TABS not single spaces between all of the entries

In order for `/etc/fstab` to run correctly at boot time vboxsf kernel module needs to be loaded BEFORE it runs. So you need to add `vboxsf` on its own line in `/etc/modules`.

## Resize a VirtualBox guest Linux VDI Disk

1. Make a copy of the VDI file – just in case (“MyLinux.vdi” -> “MyLinuxCopy.vdi“)
2. ```O:\>VBoxmanage modifyhd MyLinux.vdi --resize 102400```
this will re-size the drive to 100 GB. Pick a value that suits you. Note, your vdi file will not change in size at this point.
1. use GParted for this. Go to http://gparted.sourceforge.net/livecd.php and download a GParted Live on CD ISO file.
2. Finally, boot your original “MyLinux” Virtual Machine and all should be in order, so that when you do a “df -k”

