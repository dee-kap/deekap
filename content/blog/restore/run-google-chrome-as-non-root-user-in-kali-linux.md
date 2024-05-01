---
title: "Run Google Chrome as non root user in Kali Linux"
date: Thu, 05 Jun 2014 02:04:00 +0000
draft: false
tags: ["Linux"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

This post is about running Google's Chrome browser in Kali linux as a no-root user. Before I get into it, I would like to say that you can run Chrome as root and there are plenty of tutorials showing you how to do that. Just Google it.

Back to the focus of this post.

To run Chrome as non-root first thing we need is a non-root account. This can easily be created by

`useradd -m cuser`

Next you need to use gksu to start chrome as **cuser** which was just created. The command is

`gksu -u cuser google-chrome`

This will start Chrome.

I often start Chrome from Applications menu. But what I have described above will not make the shortcut on Applications menu work.

![Chromeshortcutkali](http://sydlog.io/wp-content/uploads/2014/06/chromeshortcutkali.png "chromeshortcutkali.png")

For that you have to do this.

Go to Applications -> System Tools -> Preferences -> Main Menu

![Mainmenu](http://sydlog.io/wp-content/uploads/2014/06/mainmenu.png "mainmenu.png")

You can modify menu items here. Select Internet and then Google Chrome. Click on properties and modify the command to be

`gksu -u cuser /usr/bin/google-chrome-stable %U`

**cuser** is our non-root user we created earlier.

Clicking Applications -> Internet -> Google Chrome should now launch Chrome.

Have fun.
