---
title: "Linux - Number of Files in Directory"
date: Wed, 03 Jul 2013 03:18:00 +0000
draft: false
tags: ["Linux"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

The command to get the number of files in a directory is.`ls –l | grep ^- | wc –l`If you are here just to get the command then no need to read further. However if you’d like to understand a bit more then read on. At home I have a media centre which runs XMBC on Ubuntu. I was in mood for doing an audit on the content I have and I came across a need to find the number of files in a directory. On \*nix my first preference is to do things from command line. Hence this post. In this post I will show you how to get a count of files in a directory. You can pick any directory you like. /var/log is always a good place to find some files you can mess with. Or you can create a bunch of files to follow along. This way our numbers will match and will be less confusing. Execute following commands. These will create some directories and a bunch of empty files.```
mkdir testdir  
mkdir testdir/dir1  
touch testdir/hello  
touch testdir/goodmorning  
touch testdir/goodafternoon  
touch testdir/bye

`` Running a simple `ls -la` command gives us the list of all files and directories ![image](http://kapoor.io/wp-content/uploads/2013/07/image-300x65.png "image") A helpful option if you want to see the files listed per line is `-1`. If we run `ls -1` we get the following output. ![image](http://kapoor.io/wp-content/uploads/2013/07/image1-300x58.png "image") With the output above we can simply count the number of lines and we have the count of files. Counting lines can be done by using `wc -l` command. The `-l` option prints the count of newlines. Let’s see what happens if we execute this command. ``
ls –1 | wc –l
`` The result is **5**. This is not accurate. If you are working with the files we created earlier in this post then you will see that we have 4 files and one directory. We are only interested in the count of files. This can easily be achieved by using some simple `grep` magic and rather than using `-1` option on `ls` command, we will use `-l` option. Command below does the job. ``
ls –l | grep ^- | wc –l
```The command above deserves some love. What we are doing is first get a list of all files and directories then we `grep`them to filter out only files. In the output of`ls -l`, files start with **–** and directories start with **d**. We finally use the `wc` command and use the option which prints the count of newlines. And there you have it, the count of files in a directory.
