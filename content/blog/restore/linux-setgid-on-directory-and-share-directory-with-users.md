---
title: "Linux - Setgid on Directory and Share Directory With Users"
date: Thu, 25 Jul 2013 03:20:00 +0000
draft: true
tags: ["Linux"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

I came across a scenario which warranted using `setgid`. The requirement was to allow multiple users to create files and read files in a directory. I also wanted to ensure that this requirement can be easily met for any future users. I will explain what I did with a simple example. To make it simple we will work with two users and one directory. The directory will be called **shareddocs**. As there are multiple users involved, it is not a good idea to create it in home but some place like **/usr/share**. Only a user with superuser privileges can create a directory in /usr/share, so we will need to use `sudo`. On my machine I am the master of unixverse and I have permissions to sudo.

````
deepak@ubuntu:~$ sudo mkdir /usr/share/shareddocs
```Two users in this example are **deepak** and **chewbacca**. deepak already exists and we need to create chewbacca. If you are trying this at home then replace deepak with whatever your username is. Just remember that you will need to use sudo for some commands so make sure that the account you are using has appropriate permissions. Let’s create chewbacca and set chewbacca’s password.```
deepak@ubuntu:~$ sudo useradd chewbacca
deepak@ubuntu:~$ sudo passwd chewbacca
```Let’s also create a group called warriors.```
deepak@ubuntu:~$ sudo groupadd warriors
```Next we need to make deepak and chewbacca members of warrirors group.```
deepak@ubuntu:~$ sudo usermod -a -G warriors deepak
deepak@ubuntu:~$ sudo usermod -a -G warriors chewbacca
```To see groups a user belongs to, we can run this command.```
deepak@ubuntu:~$ groups chewbacca
```And now the fun starts. Logged in as deepak, let’s create a file in /usr/share/shareddocs```

deepak@ubuntu:~$ sudo touch /usr/share/shareddocs/story1.txt
```View permissions for /usr/share/shareddocs```

deepak@ubuntu:~$ ls -ld /usr/share/shareddocs/

drwxr-xr-x 2 root root 4096 Jul 24 22:43 /usr/share/shareddocs/
```Notice how both owner and group are root for /usr/share/sharedocs directory. Now if we try to create a file as chewbacca we will get an error.```

chewbacca@ubuntu:~$ touch /usr/share/shareddocs/story2.txt
touch: cannot touch 'story2.txt': Permission denied
```This is because only root has read and write permissions to the directory. We can fix the situation by first giving the group ownership to warriors group we created earlier.```
deepak@ubuntu:~$ sudo chown :warriors /usr/share/shareddocs/
```Now if we look at the permissions, we see that our directory is owned by warriors group.```
deepak@ubuntu:~$ ls -ld /usr/share/shareddocs/

drwxr-xr-x 2 root warriors 4096 Jul 24 22:43 /usr/share/shareddocs/
```So can chewbacca create a file now? Well not yet. We still need to enable write permission for the group.```
deepak@ubuntu:~$ sudo chmod 775 /usr/share/shareddocs/
```By executing the above command we have given read, write and execute to owner and the group.```
deepak@ubuntu:~$ ls -ld /usr/share/shareddocs/

drwxrwxr-x 2 root warriors 4096 Jul 24 22:43 /usr/share/shareddocs/
```chewbacca can now create files in /usr/share/shareddocs/```
chewbacca@ubuntu:~$ touch story2.txt
```One problem still remains. Files created by chewbacca are owned by group chewbacca. We want all files within the directory to be owned by **warriors** group. This is where `setgid` comes in. Finally! you say. Let’s run the following command.```
deepak@ubuntu:~$ sudo chmod g+s /usr/share/shareddocs
```From here on any files created by either deepak or chewbacca will be owned by warriors group. Now if deepak created story3.txt and chewbacca created story4.txt, they will both be owned by warriors group.```

\-rw-r--r-- 1 root root 16 Jul 25 15:26 story1.txt
\-rw-rw-r-- 1 chewbacca chewbacca 0 Jul 25 15:36 story2.txt
\-rw-rw-r-- 1 deepak warriors 0 Jul 25 15:42 story3.txt
\-rw-rw-r-- 1 chewbacca warriors 0 Jul 25 15:44 story4.txt
```Note that two files we created earlier are still not owned by warriors. They cannot be shared and we should just delete them. Let’s talk a bit more about `setgid`. The command sets group id bits. This means that any new files or directories created within the directory will inherit the same group as containing directory. To remove the group id bit we can use `g-s`.
````
