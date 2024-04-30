---
title: "Upgrade node.js on mac"
date: Tue, 21 Apr 2015 04:19:30 +0000
draft: false
tags: ["Node.js"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

One way to upgrade node.js on your machine is to download the latest installer from [node.js website](http://nodejs.org). The other is to update node.js from CLI which is my preferred way. To upgrade node.js we should have [n](https://www.npmjs.com/package/n) installed. `npm install -g n` Clean npm cache `npm cache clean -f` Install latest node.js stable version `sudo n stable` That's all folks.
