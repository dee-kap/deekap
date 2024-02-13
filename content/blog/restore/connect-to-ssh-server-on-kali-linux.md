---
title: 'Connect to ssh server on Kali Linux'
date: Tue, 03 Jun 2014 05:04:00 +0000
draft: false
tags: ['Kali', 'Linux']
---

For some of my work I run Kali in Virtual Box and I was getting a bit tired of switching between different windows on my mac host. So I thought I will ssh into my Kali box and enjoy the iTerm eye-candy. The version of Kali I have running which is 1.07 has openssh server installed but the service is not running by default. To run the service I ran this command  
  
`service ssh start`  
  
What if I did not have openssh server?  
  
That can easily be taken care of. Remember that Kali is based on debian so openssh server can be installed by running this command  
  
`apt-get install openssh-server`  
  
To verify that openssh server is installed run  
  
`service --status-all`  
  
If the output contains **\[ - \] ssh** then ssh is not installed.