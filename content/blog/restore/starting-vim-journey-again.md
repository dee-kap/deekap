---
title: "Starting Vim Journey Again"
date: Fri, 11 Apr 2014 05:52:00 +0000
draft: false
tags: ["Tools", "Vim"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Every few months I talk myself into using Vim as my text editor. Mostly it happens after I have watched a presentation in which the presenter wows me with their code editing skills on Vim. I miss the main subject of the presentation because I get so wowed by their Vim ninja skills. This time the video was this [one minute demo](https://www.destroyallsoftware.com/screencasts) video by Gary Bernhardt.

This is not the first time I am going through this. In past I have tried to switch over to Vim few times. Each time I have left the adventure incomplete because of other things which kept me busy.

Based on my past experience I have found that Vim has slowed me down for first few days. This is because while I am writing code, I am also learning one of the most complex editors. It just feels like a hindrance while writing code. However, I am sold on the eventual benefits and with that idea, I am starting my journey again. Is it a fact or a myth that mastering Vim will make me do things faster is to be tested. It is possible that my initial hypotheses maybe total BS. More on that when time comes.

## The setup

Mac OSX comes with vim pre-installed but after reading and hearing praise about macvim, I decided to install it. I used homebrew to install MacVim. The command below did the job.

```
$ brew install mvim
```

First thing which came to my mind after installing MacVim was that I want it to look good. Thus started my research of plugins I should have. Rest of this article is mostly about the plugins I installed.

## Plugin management

Vim community is strong and there is a massive choice of plugins available. The number of plugins one can install can be daunting. My recommendation is to start with a small number of plugins and see how you feel. Then based on your requirements add more plugins.

While the plugin ecosystem for Vim has been strong, the weakness has been in the plugin management area. Thanks to [Pathogen](https://github.com/tpope/vim-pathogen) and [Vundle](https://github.com/gmarik/Vundle.vim), this weakness has been well addressed. If you are starting with Vim like me then you must install either one of these. At a high level these plugin managers work with git repositories of the respective plugins and take care of installation for you.

I decided to go with Vundle because I liked the way I can mention the plugins I would like to use and then run `:PluginInstall` and Vundle will install the plugins for me. The entire process is much simpler than copying plugin files manually.

## Plugins

Below is a collection of plugins I installed to get started. All of them address my needs. Most likely I will add more plugins but for now these will do.

### NerdTree

I want to see the directory structure of my project in the editor. I also want to search for files in the project.

[NerdTree](https://github.com/scrooloose/nerdtree) is the plugin I used to see the directory structure layed out in a tree view. Navigating directories in NerdTree is easy and files can be opened in split windows. Once installed NerdTree can be opened by `NERDTree` command which I have mapped to `<leader>nt`

One of the things I wish NERD Tree had was ability to do fuzzy search. For that I am using another plugin called Command-T. More on Command-T below.

![Nerdtree](http://sydlog.io/wp-content/uploads/2014/04/nerdtree.png "nerdtree.png")

## hybrid

While deciding on the theme I came across two themes [Tomorrow Night](https://github.com/chriskempson/vim-tomorrow-theme) and [Jellybeans](https://github.com/nanotech/jellybeans.vim). I was almost ready to go with Tomorrow Night when I came across hybrid. Hybrid theme combines colour palette from Tomorrow-Night, syntax scheme from Jellybeans and Vim code from Solarized. Just perfect for my taste.

[Hybrid link](https://github.com/w0ng/vim-hybrid)

## vim-airline

Default status bar in Vim is not the most funky. I came across two popular choices to jazz up the status bar. One was [Powerline](https://github.com/Lokaltog/vim-powerline) and the other is [vim-airline](https://github.com/bling/vim-airline). Powerline is written in Python and vim-airline is a light weight status bar written in Vim script. I decided to go with Vim-Airline because I found the instructions to be simpler. vim-airline uses power line fonts which should be installed so that correct glyphs are visible on the status bar.

![Vim statusbar](http://sydlog.io/wp-content/uploads/2014/04/vim-statusbar.png "vim-statusbar.png")

## vim-gitgutter

Git is one of the most important tools I use on daily basis. While editing code it is helpful to get some indication of lines that have changed, deleted or added. [Vim-gitgutter](https://github.com/airblade/vim-gitgutter) takes care of that. It uses common character symbols to indicate edit, add or delete.

![Vim gutter](http://sydlog.io/wp-content/uploads/2014/04/vim-gutter.png "vim-gutter.png")

## Command-T

One of the features of my current editor Sublime Text which impresses me is the quick lookup. I use it many times while writing code and I like its fuzzy search capabilities. For Vim I found [Command-T](https://wincent.com/products/command-t) plugin to find files using fuzzy lookup. In my vimrc I have the `CommandT` command mapped to `<leader>t` . One thing which I would like is highlight the results. I have not yet been able to find a way to do this.

![Comand t](http://sydlog.io/wp-content/uploads/2014/04/comand-t.png "comand-t.png")

## vim-javascript-sytax

Most of work these days in writing JavaScript and more specifically AngularJS. I wanted a plugin which does JavaScript properly. I found [vim-javascript-syntax](https://github.com/jelera/vim-javascript-syntax) for this.

## vim-indent-guides

I like to see my code properly indented. [Vim-Indent-Guides](https://github.com/nathanaelkane/vim-indent-guides) draws lines at each indentation level and allows me to quickly see the indentation.

## emmet-vim

Emmet is a plugin I am so used to in Sublime Text and had I not found one for Vim, it would have been a deal breaker. Once you start using Emmet which was earlier known as zen coding, you cannot live without it. Here is a simple example type `div>ul>li*5_` then hit `Ctrl + y + ,` and you get this html.

```
<div>
  <ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <_></_>
  </ul>
</div>

```

This is a very basic use of Emmet. There is a lot more that can be done with it. Take a look at [Emmet-Vim](https://github.com/mattn/emmet-vim) page for instructions.

## Where am I

These are enough to start using Vim again and I hope that this time I will stick with it. I started writing this post in morning and finished it up at night. During the day I used Vim all day and after few frustrations I found myself more comfortable navigating around files and navigating within code. Looks like a good start.
