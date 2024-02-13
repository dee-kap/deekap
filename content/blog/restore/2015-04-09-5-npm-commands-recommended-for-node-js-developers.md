---
title: "5 npm commands recommended for node.js developers"
date: Thu, 09 Apr 2015 06:59:41 +0000
draft: false
featured_image: "nodejs.svg"
tags: ["Node.js"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

## Search for packages

npm allows you to search the npm registry from command line. When you execute the command for the first time it builds an index. If you are searching for package(s) which have something to do with png file you can run `$ npm search png` This will find all packages which have png in its metadata. [![npm-search-png](http://kapoor.io/wp-content/uploads/2015/04/npm-search-png.png)](http://kapoor.io/wp-content/uploads/2015/04/npm-search-png.png)

## Find owner of a package

npm owner command can be used to find owner(s) of a package. You can also add or remove owner but it requires you to be an owner npm owner command has three options

1.  ls - lists the owners of a package
2.  add - adds an owner
3.  rm - removes an owner from a package

To find the owner of a package e.g. express, run this command `$ npm owner ls express`

## Find outdated packages

Things move fast in node.js world. New packages are added daily and existing packages are updated frequently. To find out if you are using an outdated version of a package, run `$ npm outdated` It will look at your package.json file and inform you if a package is outdated. [![npm-outdated](http://kapoor.io/wp-content/uploads/2015/04/npm-outdated.png)](http://kapoor.io/wp-content/uploads/2015/04/npm-outdated.png)

## Go to Git repository of a package

To open the git repository url of a package from command line, you can use `$ npm repo [package name]`. This will launch the browser and navigate to the url of git repository.

## View registry information of a package

A handy command which allows you to view information stored in the registry for a package. `$ npm view strip-json-comments` I often use it to see when a package was last modified `$ npm view strip-json-comments | grep modified`  
npm has a cli interface which provides a rich functionality. In this post I have listed only 5 which I find somewhat interesting. I encourage you to look at the [official documentation](http://docs.npmjs.com/) to gain more understanding of different npm commands.
