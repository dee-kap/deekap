---
title: "Programmatically Take Screenshot Using C#"
date: Thu, 26 Feb 2009 01:00:00 +0000
draft: false
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

To do this you will need to add references to System.Drawing and System.Windows.Forms. Make sure that you have following using statements:`using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Windows.Forms;`In your method add this code. It will take a screenshot of your primary screen and save it to a file.```
Bitmap bitmap = new Bitmap(Screen.PrimaryScreen.Bounds.Width,
Screen.PrimaryScreen.Bounds.Height);
Graphics graphics = Graphics.FromImage(bitmap as Image);
graphics.CopyFromScreen(0, 0, 0, 0, bitmap.Size);
bitmap.Save(@"c:tempscreenshot.bmp", ImageFormat.Bmp);

```

```
