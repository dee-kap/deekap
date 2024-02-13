---
title: "git log basic to advance"
date: Wed, 21 May 2014 03:33:00 +0000
draft: false
tags: ["Tools"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Git is just awesome and more awesome are the tools it comes with. Git log is one of those tools I use extensively throughout my day.

I started using git log in its vanilla form and then slowly as my understanding of git increased, I started using fancier git log commands. The last one is my current favourite and I have it as an alias in the config file.



`git log`

![](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-10.52.04-am1.png)

`git log --oneline`

![](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-10.52.56-am.png)

`git log --oneline -p`

![](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-11.42.28-am.png)

`git log --oneline --decorate`

![](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-11.28.37-am.png)

`git log--oneline --decorate --graph`

![](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-11.34.01-am.png)

`git log --oneline --decorate --graph -10`

![](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-11.38.30-am.png)

`git log --graph  
--pretty=format:'%Cred%h%Creset %C(cyan)%an%Creset -%C(blue)%d%Creset %s %Cgreen(%cr)%Creset'  
--abbrev-commit --date=relative`

![](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-11.41.28-am.png)

`git log --graph  
--pretty=format:'%Cred%h%Creset %C(cyan)%an%Creset -%C(blue)%d%Creset %s %Cgreen(%cr)%Creset'  
--abbrev-commit --date=relative --stat`

![](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-11.46.34-am.png)
