---
title: "Path Picker by Facebook"
date: Fri, 08 May 2015 02:19:22 +0000
draft: false
tags: ["Tools"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Path Picker is a little utility brought to us by Facebook. According to the official website

> PathPicker accepts a wide range of input -- output from git commands, grep results, searches -- pretty much anything.

On a mac Path Picker can be installed by using brew. To install on mac with brew. Run these commands```
brew udpate
brew install fpp

````![PathPickerInstallation](http://kapoor.io/wp-content/uploads/2015/05/PathPickerInstallation.png)

### What does it do?

I will go through some of the features of Path Picker. These features are mentioned on the README file for path picker [repository](https://github.com/facebook/pathpicker/)

> Parse all incoming lines for entries that look like files

To see how this works, I will work with angular.js repository which I have cloned on my machine. Let's run a simple command which gives all the files impacted by a commit```
git show --pretty="format:" --name-only 0681a54
```The command above will list all the files changed in commit 0681a54.```
src/ngAnimate/animateCss.js
src/ngAnimate/animateJs.js
test/ngAnimate/animateJsSpec.js
```If I pipe the output to Path Picker, I can then open the files from within terminal.```
git show --pretty="format:" --name-only 0681a54 | fpp
```![PathPickerListFiles](http://kapoor.io/wp-content/uploads/2015/05/PathPickerListFiles.png) Files can be opened in preferred editor by pressing ENTER. Path picker also has another trick up its sleeve. From the README

> PathPicker allows you to also execute arbitrary commands with the specified files

Working with the same command```
git show --pretty="format:" --name-only 0681a54 | fpp
```I can press c to get into command mode. ![PathPickerCommandMode](http://kapoor.io/wp-content/uploads/2015/05/PathPickerCommandMode.png) Here I can issue a shell command such as `cat | more` to see the contents of file. I can issue a the command `cat $F | wc -l` to count the number of lines in the file. Or a command like `cat $F | grep Firefox` to see if the string Firefox is present in the file. In a nutshell Path Picker is a nifty little utility which makes life a little easy when you spend a lot of time in Terminal.
````
