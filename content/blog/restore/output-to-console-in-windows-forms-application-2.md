---
title: "Output to Console in Windows Forms Application"
date: Tue, 01 Sep 2009 02:45:00 +0000
draft: false
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

This post shows you how to output data to a Console in a Windows Forms Application. I use this technique religiously when developing Windows Forms applications. Debugging is much simpler when you can see information on what your application is doing in a Console. Of course the onus is on you as developer to output data which will help you. In this post I will use a simple Windows Forms application which adds two numbers.

![Windows Forms](http://kapoor.io/wp-content/uploads/2009/09/image.png "Windows Forms")

By default a Windows Forms application does not output to a Console even if you write a Console.Write() or Console.WriteLine(). This shortcoming can be addressed by using Win32 API. In your Windows Forms application you can declare a class which provides a wrapper around Win32 functions.

```
public class Win32
{
  /// <summary>
  /// Allocates a new console for current process.
  /// </summary>
  \[DllImport("kernel32.dll")\]
  public static extern Boolean AllocConsole();

  /// <summary>
  /// Frees the console.
  /// </summary>
  \[DllImport("kernel32.dll")\]
  public static extern Boolean FreeConsole();
}
```

A Console must be started to accept input and display our messages. This can be done by calling Win32.AllocConsole() function. For my example I will start the console in my form’s constructor.

```
public Form1()
{
  InitializeComponent();

  Win32.AllocConsole();
}
```

Now when I write to Console, I will see data appear in the console window which was started in my constructor.

```
private void Add(int num1, int num2)
{
  int result = num1 + num2;

  Console.WriteLine(
    string.Format("{0} + {1} = {2}", num1, num2, result));
}
```

![Console](http://kapoor.io/wp-content/uploads/2009/09/image1-300x135.png "Console")

As a good practice you should also close the console window by calling Win32.FreeConsole() method before your application exits.
