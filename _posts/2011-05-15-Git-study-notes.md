---
layout: post
title: Git学习笔记
tags: Git
categories: Technology
public: true
---
## Ignoring directories in Git repos
Create a file named .gitignore in your projects directory. Ignore directories by entering the directory name into the file (with a slash appended):
~~~
dir_to_ignore/
~~~

## 撤销修改
`git checkout -- file`：丢弃工作区的修改

`git reset HEAD file`：把暂存区的修改撤销掉，重新放回工作区

`git reset HEAD -- .`: 把暂存区的所有修改撤销掉，重新放回工作区

## 远程仓库
### Generating a new SSH key
substituting in your email address.
~~~
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
~~~
or
~~~
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa.github -C "your_email@example.com"
~~~
Adding a new SSH key to your GitHub account
~~~
cat ~/.ssh/id_rsa.github.pub | clip
~~~
or
~~~
xclip -i -selection clipboard ~/.ssh/id_rsa.github.pub
~~~
Testing your SSH connection
~~~
ssh -T git@github.com
~~~
### 添加远程库
clone a repository with:
~~~
git clone git@github.com:jiandewu/jiandewu.github.io.git
~~~
关联一个远程库：
~~~
git remote add origin git@server-name:path/repo-name.git
~~~
关联后第一次推送master分支的所有内容：
~~~
git push -u origin master
~~~
此后，每次本地提交后，只要有必要，就可以使用命令
~~~
git push origin master
~~~
推送最新修改