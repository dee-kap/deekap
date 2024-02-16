---
title: "Node.js - Make npm work behind proxy"
date: Wed, 08 Jan 2014 00:23:00 +0000
draft: true
tags: ["Node.js"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Installing node.js modules in a corporate environment can be problematic if your connection to the world is via a proxy. I experienced this while setting up a node.js environment at one of my client's office. I always use my personal machine which is a mac but often I have to work with folks who use Windows. Anyhow this is not a mac vs PC post. Just wanted to say that because at the end I talk about the location of npm config file.

To configure proxy server for npm run these commands.

```

npm config set proxy http://YourProxyServerAddress:port
npm config set https-proxy http://YourProxyServerAddress:port

```

On Windows npm uses a hidden file named .npmrc for configuration. This file is in the local user folder something like c:usersyourname on Windows 7. If the file does not exist then it will be created when `npm config` command is executed.
