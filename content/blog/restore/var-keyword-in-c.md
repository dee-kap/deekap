---
title: "Var Keyword in C#"
date: Tue, 06 Jan 2009 00:58:00 +0000
draft: false
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

I have a confession to make. When I saw **var** keyword for the first time I did not like it at all. My first opinion was that var was so variant like. Call me a control freak but I like to clearly see what I am declaring. And var was something I thought made the code less readable. However since I started working with LINQ I got into a habit of using var. I realised that it makes my life easy by letting the compiler figure things out for me. So in this post I will pay due respect to var keyword. Anything declared using var keyword is implicitly typed which means that compiler will determine the correct type based on what the variable is initialised to. Here I am declaring three variables x, y and z. All of them are initialised to different values which are also of different Types such as DateTime, string and List<T>.`var x = DateTime.Now;
var y = "Hello";
var z = new List();`Let’s examine the IL to verify that x, y and z are of Types they have been initialised to. ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/01/image3.png) Here you can see that x is of valuetype, y is a string and z is of type List<string>. I find this as neat little syntax sugar to which I have become addicted. Keep in mind that you cannot write a statement like this.```
var x;

```This will give an error while compiling. And it makes sense because the compiler does not know which Type it should consider x as. ![Compiler Error](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/01/image2.png)

```
