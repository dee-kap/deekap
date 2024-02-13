---
title: "My Visual Studio Code Setup"
date: Fri, 19 Oct 2018 01:48:25 +0000
draft: false
tags: ["Tools", "VS Code"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

When Microsoft announced Visual Studio Code in 2015, I did not have good things to say about it. However, times have changed and Visual Studio Code is my preferred code editor these days. The editor has come a long way and it is commendable that Microsoft is serious about maintaining VS Code.

## Theme

The first thing I look for in an editor is support for themes and availability of good themes. VS Code gets five stars in this area. My preferred theme these days in [Night Owl](https://marketplace.visualstudio.com/items?itemName=sdras.night-owl) by [Sarah Drasnar](https://github.com/sdras). It looks beautiful on my 4k monitor. Yes, I'm _showing off_ :)

![](https://bitofbinary.com/wp-content/uploads/2019/05/vs-code-night-owl-1024x738.png)

I have also customised a few minor things. One of them is the current line highlight. This is from my settings.json

```
“workbench.colorCustomizations”: {
  “editor.lineHighlightBorder”: “#2e276d”,
  “editor.lineHighlightBackground”: “#1b1a25”
}
```

I feel that there is more art than science to themes and Night Owl is just perfect. Unless something better shows up, I will stick with this one.

## Extensions

Extensions for a code editor can be a hot topic. There are people who are against them and there are people who cannot see the world without them. I belong to the latter camp. Before I tell you about the extensions I use, enjoy this tweet by Damian Edwards.

![](https://bitofbinary.com/wp-content/uploads/2019/05/damianedwardstweet-1024x581.png)

In the past, I would install any extension which showed up and had good reviews. I have learned to break that habit and now I only install extensions which are must-have for me.

This is a list of extensions I use on a daily bases.

1.  [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)  I cannot praise this extension enough. It has all the usual stuff you'd expect such as creating commits, pushing code etc. The feature I like most is how it shows you the history for the line where your cursor is.
2.  [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) No need to say much about this one.
3.  [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) I do a lot of work on node.js and React. This extension shows you the code of modules you are importing.
4.  [Jest](https://github.com/jest-community/vscode-jest) is for my preferred unit testing framework. I use it not only for React but for all JavaScript unit testing
5.  [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) Can't see myself writing Python without this

That's it. Just five extensions (at present). I find these to do all the heavy lifting for me in my day-to-day work.

Working with Visual Studio Code is a charm. It feels comfortable and I don't feel like I have to fight the tool to get my job done. Can't see myself using anything else in near future.

Happy Learning!
