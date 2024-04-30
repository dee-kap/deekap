---
title: "Menus in Avalon"
date: 2005-02-05
draft: false
featured_image: "dotnet.svg"
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

## Introduction

In this article I will show you how to create menus in Avalon using. This article is for beginners who are getting started with Avalon. I will show you how to write the menus in XAML and how to add Access keys to your menus. Enjoy.

## About Menus

Menus as we all know assist us in performing various functions such as opening an existing file, creating a new file, exiting an application and many more. Working with Windows you must be familiar with the consistent look-and-feel that Windows applications have. Menus such as Edit – Cut – Copy – Paste are used frequently in working with any application. From a developer’s perspective there has been something new for menu creation in almost every version of tools out of Microsoft. Avalon adheres to the tradition and introduces some new elegant techniques of its own. You can now create advance menus using XAML. So let’s get started with the menus.

## Simple Menu

Below is the code which creates a very simple menu File - New - Open - Exit.

```xml
<Menu Background="White">
  <MenuItem Header="File">
  <MenuItem Header="New"></MenuItem>
  <MenuItem Header="Open"></MenuItem>
  <MenuItem Mode="Separator"></MenuItem>
  <MenuItem Header="Exit"></MenuItem>
  </MenuItem>
</Menu>
```

Figure 1: Simple Menu

Note that to apply a separator bar we now set the Mode property as compared to earlier method where the text was set as a “-“. Along with Separator bars, other modes available are Default and Checkable. By default the mode for any MenuItem is Default.

## MenuItem with Sub items

Each MenuItem has an Item property which can contain more MenuItems. Below is the code which displays a menu with sub menu items.

```xml
<Menu Background="White">
  <MenuItem Header="File">
    <MenuItem Header="New"></MenuItem>
    <MenuItem Header="Open"></MenuItem>
    <MenuItem Mode="Separator"></MenuItem>
    <MenuItem Header="Recent Files">
      <MenuItem Header="File 1"></MenuItem>
      <MenuItem Header="File 2"></MenuItem>
      <MenuItem Header="File 3"></MenuItem>
      <MenuItem Header="File 4"></MenuItem>
    </MenuItem>
    <MenuItem Mode="Separator"></MenuItem>
    <MenuItem Header="Exit"></MenuItem>
  </MenuItem>
</Menu>
```

Figure 2: MenuItem with sub-menus

## Menu Access Keys

Access keys are used to navigate to a menu item when pressed with ALT key. This is how you assign access keys in XAML. In the code below note that the text for a menu item such as “File” has been modified to “ile” as the first character is an access key, and is displayed along with the remaining text forming the full caption “File”. You can see that character “F” is underlined which is a standard way to display an access key in a menu.

```xml
<Menu Background="White">
  <MenuItem>

    <MenuItem.Header>
      <Text><AccessKey Key="F"></AccessKey>ile</Text>
    </MenuItem.Header>

    <MenuItem>
      <MenuItem.Header>
        <Text><AccessKey Key="N"></AccessKey>ew</Text>
      </MenuItem.Header>
    </MenuItem>

    <MenuItem>
      <MenuItem.Header>
        <Text><AccessKey Key="O"></AccessKey>pen</Text>
      </MenuItem.Header>
    </MenuItem>

    <MenuItem Mode="Separator"></MenuItem>

    <MenuItem>
      <MenuItem.Header>
        <Text><AccessKey Key="E"></AccessKey>xit</Text>
      </MenuItem.Header>
    </MenuItem>

  </MenuItem>
</Menu>
```

Figure 3: Menus with access keys

## Summary

This article showed how to create simple menus with XAML. There is much more to menus than what you have just seen. In the future I will write more on how advanced UI effects can be applied to menus, and how we can create menus at runtime.
