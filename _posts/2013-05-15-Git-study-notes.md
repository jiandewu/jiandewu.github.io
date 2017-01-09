---
layout: post
title: Git Cheat Sheet
tags: Git
categories: Technology
public: true
---
## Ignoring directories in Git repos
Create a file named .gitignore in your projects directory. Ignore directories by entering the directory name into the file (with a slash appended):

~~~
dir_to_ignore/
~~~

Create a global .gitignore

You can also create a global .gitignore file, which is a list of rules for ignoring files in every Git repository on your computer. For example, you might create the file at ~/.gitignore_global and add some rules to it.

~~~
git config --global core.excludesfile ~/.gitignore_global
~~~

Or create `~/.config/git/ignore` file

## 撤销修改
`git checkout -- file`：丢弃工作区的修改

`git reset HEAD file`：把暂存区的修改撤销掉，重新放回工作区

`git reset HEAD -- .`: 把暂存区的所有修改撤销掉，重新放回工作区

If you ever find that you accidentally left something out of your last commit, be it a file or an extra change to a file that you just committed, don't worry. It can easily be fixed. 
All you have to do is stage the extra changes like you would for a normal commit:

~~~
git add .
git commit --amend
~~~

If you don't specify a commit message with -m you will be prompted with the previous commit message as a default.

## 分支管理
查看分支：`git branch`

创建分支：`git branch<name>`

切换分支：`git cheakout<name>`

创建+切换分支：`git cheakout -b <name>`

删除分支：`git branch - d <name>`

合并某分支到当前分支时加 `--no-ff` 参数：普通模式合并，合并后的历史有分支, eg:

~~~
git merge --no-ff -m "merge with no--ff" develop
~~~

## 标签管理
`git tag <name>`：新建一个标签（默认为HEAD，也可以指定commit id）

`git tag -a <tagname> -m "blablabla..."`：可以指定标签信息

`git tag -s <tagname> -m "blablabla..."`：可以用PGP签名信息

`git tag`：查看所有标签

`git push origin <tagname>`：推送一个本地标签

`git push origin --tags`：推送全部未推送过的本地标签

`git tag -d <tagname>`：删除一个本地标签

`git push origin :refs/tags/<tagname>`：删除一个远程标签


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

此后，每次本地提交后，只要有必要，就可以使用命令推送最新修改

~~~
git push origin master
~~~

其他

~~~
git remote -v
git remote rm destination
~~~