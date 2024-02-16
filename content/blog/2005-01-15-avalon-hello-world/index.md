---
title: "Avalon Says Hello World in XAML"
date: 2005-01-15
draft: true
featured_image: "dotnet.svg"
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

## Introduction

This article walks you through building a simple Hello World Application in XAML using Avalon. It discusses the goodies required to build and run the application.

## Requirements

In order to build and run the application we will create here you will need the following:
• Visual Studio 2005 (This is a beta release, and can be downloaded from MSDN)
• Avalon CTP Release (This can be downloaded from MSDN subscriber’s download area)

## Developing the application

Follow these steps to build and run the application:

1. Start Visual Studio.NET 2005. Click File – New - Project

Figure 1

2. For Project Type Select “Avalon”, and for Template Select “Avalon Application”. Name Project “HelloWorld”

Figure 2

3. At this Stage you will have a screen which looks like Figure 3 below. The file Window1.xaml is the main window of your application. This is where we will write the User interface code. Replace the elements and paste the following code:

```xml
<LABEL id=label1 width="100%"></LABEL>
<BUTTON id=button1 content="Say Hello" click="ButtonClick"></BUTTON>
```

Figure 3

At this stage if you build your application you will get an error which says something like this “Error 1 'HelloWorld.Window1' does not contain a definition for 'ButtonClick'…”. This is because we have not yet written an event handler for the Click Event of the button.

4. Open the file “Window1.xaml.cs” and add this code within the Window1 class

```csharp
private void ButtonClick(object sender, RoutedEventArgs e)
{
label1.Content = "Hello World!";
}
```

5. Hit F5 and your project will now run with a window which looks like Figure 4 below

Figure 4

When you click the button, the label will display “Hello World”

## Summary

In this article we wrote a simple Hello World application which utilizes the Avalon Libraries. Even though this article was very simple, it gets you started with Avalon Development, and allows you to test the readiness of your development environment to build richer Avalon applications. In the future articles I will go in more details of Avalon, and describe the way things run behind the scenes.
