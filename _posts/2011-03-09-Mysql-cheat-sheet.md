---
layout: post
title: MySQL Command Line Cheat Sheet
tags: Mysql
categories: Technology
public: true
---

1. Access monitor: `mysql -u [username] -p;` (will prompt for password)

1. Select database: `use [database];`

1. Determine what database is in use: `select database();`

1. Show all tables: `show tables;`

1. Create new database: `create database [database];`

1. Show all databases: `show databases;`

1. Deleting databases: `DROP DATABASE [database];`

1. List all users: `SELECT User,Host FROM mysql.user;`

1. Create new user: `CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';`

1. Grant ALL access to user for * tables: `GRANT ALL ON database.* TO 'user'@'localhost';`

1. Delete user: `DROP USER 'username'@'localhost';`

1. Export a database dump (more info [here](http://stackoverflow.com/a/21091197/1815847)): `mysqldump -u [username] -p [database] > db_backup.sql`

1. Import a database dump (more info [here](http://stackoverflow.com/a/21091197/1815847)): `mysql -u [username] -p -h localhost [database] < db_backup.sql`

1. Logout: `exit;`