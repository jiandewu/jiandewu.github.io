---
layout: post
title: Git之Cherry-Picking用例
tags:
- Git
categories: Technology
public: true
---

First of all, use `git log` to see exactly which commit you want to pick. An example:

~~~
dd2e86 - 946992 - 9143a9 - a6fd86 - 5a6057 [master]
            \
             76cada - 62ecb3 - b886a0 [feature]
~~~

In this case, `62ecb3` is the cherry and you want to pick it!

~~~
$ git checkout master
$ git cherry-pick 62ecb3
~~~

That’s all. `62ecb3` is now applied to the master branch and commited (as a new commit) in master. cherry-pick behaves just like merge.

You could also just grab a file from the feature branch:

~~~
$ git checkout master
$ git checkout feature -- filename
~~~

That'll get you the same version of the file that exists in the feature branch, but note that it won't pull in the history of changes to the file.

### 参考
1. [Cherry-Picking specific commits from another branch](https://ariejan.net/2010/06/10/cherry-picking-specific-commits-from-another-branch/)