---
title: "Dynamic Sort With LINQ to SQL"
date: Wed, 19 Nov 2008 00:50:00 +0000
draft: false
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Sometime ago I wrote a post showing how to do [dynamic sort with LINQ](http://www.debugrelease.com/dynamic-sort-with-linq/). That approach worked well with LINQ To Objects. Today I spotted a [question on the forums](http://forums.asp.net/p/1349895/2753778.aspx) where Levi asked a question about doing dynamic sorts with LINQ To SQL. My earlier approach will work once all the data is retrieved on the client side. This of course is not an ideal way. A  better option is to do sorting on database. Here is the question as it was posted on the forum.

![C# Visual Studio .Net Code](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image11.png)

#### I thought this will work

My initial reaction was to modify the code I wrote earlier to dynamically create a query. This is what I did. ![C# Visual Studio .Net Code](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image12.png) and I used this code to call my method ![C# Visual Studio .Net Code](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image13.png) LINQ To SQL is not able to generate a query and instead throws an exception when I try to access the results in debugger. ![C# Visual Studio .Net Code](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image14.png)

#### So what can be done?

The key here is to generate the query dynamically. And we can  use the built-in Expression type to do just that. So I gave it another go with this code. ![C# Visual Studio .Net Code](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image15.png) This method takes in a column name to sort by and returns  IQueryable<T>. It works but looks like a lot of effort and appears miles away from any kind of normal LINQ code. Fortunately I can achieve the same results with this code.  ![C# Visual Studio .Net Code](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image16.png) To sort by Title, I can call the method like this.  ![C# Visual Studio .Net Code](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image17.png) This gives me exactly what I want and partially answers the question posted on the forum. Partially, because I have not addressed dynamic grouping. I assume that it is doable with a similar approach.
