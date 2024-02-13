---
title: "Introduction to WinFX"
date: 2005-01-13
featured_image: "dotnet.svg"
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

## Introduction

This article introduces you to the next generation of APIs from Microsoft called WinFX. It discusses how WinFX complements the existing .NET framework and how WinFX is totally fresh technology and not just wrappers around Win32.

When Windows XP came out one thing that was on the mind of a lot of people was: what’s next? Well Microsoft came up with that answer at PDC 2004 and the answer was Longhorn. If you are not aware; Longhorn is the code name for the next windows release, sorry next windows client release. Once again as usual we are bound to see Microsoft Marketing Machine in action to sell this version of windows, and sell it better than the previous ones. Now in order to do that, techies have to come out with something new and cool and of the type not yet seen in any of the Windows, and I am not just talking about a cool solitaire or next version of Paint. No no no! they have to do a much better job than this. And I think they are doing it. With the PDC release which was a Community Technology Preview of Longhorn, users were able to see some if not all of the cool stuff which will come with Longhorn. One of those cool things which got the developer community excited is WinFX (pronounced "Win Effects").

## So what is this WinFX thing?

Well to answer this question we can take two approaches, one is that we take a historical trip to the old days of DOS and trace the time-line to .NET. Other is that we start with .NET and go from there-on. I am not much of a history buff, so I will take the second approach. In year 2000 (the year when Sydney hosted the Olympics) Microsoft started generating buzz about .NET. While everyone...okay everyone who has something to do with computers...talked about .NET, and I could not get a concrete answer to the question: What is .NET? Of course I have the answer now. Although my answer is open to debate, here it is anyway. .NET is long overdue framework from Microsoft, which enforces the use of object-oriented programming for windows platform, has a rich class library which increases productivity by providing developers with an enormous amount of groundwork already done for them, uses a lot of XML, and has a lot of other very useful bells and whistles. A very important fact about .NET is that most of the classes provided by the framework are wrappers around Win32. Did I say Win32? Yes I did. While it’s all managed code and we have the power of mighty Garbage Collector at our disposal, most of it is still calling Win32 functions. Note that I have used "most" twice in my last sentence, because there are classes which do not call Win32.

Now what I feel that in order to deliver the true object-oriented promises of .NET at OS level Microsoft has to do a lot of work in the base APIs. WinFX is a major milestone in that direction. WinFX does not sit on top of Win32; it provides the base services through newly written managed APIs.

## What’s in WinFX

Two of the major pillars of WinFX are Presentation and Communication. Presentation services are provided by the libraries code named "Avalon", and the communication side is taken care by "Indigo".

Another major actor in WinFX plot is Longhorn. Actually Longhorn is the one who started all this. WinFX will be an integral part of Longhorn. During late 2004 Microsoft released a CTP release of Avalon for Windows XP and Windows Server 2003. Note that at the time of this writing this release is only available to MSDN subscribers. This means that even though WinFX is a part of Longhorn, it will be available to Windows XP and Windows 2003 in the near future perhaps before Longhorn ships.

## Who will use WinFX

I remember when Win32 came out and most of us were very happy with our old 16 bit stuff. Initial reaction to Win32 was that while it’s powerful, utilizes the processor to its full potential, and is a better way of doing things, why would we change our existing applications. Now as I said this was an initial reaction, of course over the time everyone did move over to Win32 in some for or another. I feel that similar will happen with WinFX, but this time the reaction will be a short-lived one. If you look at the services provided by WinFX then there is no reason to hold on.

WinFX will be used for applications which provide a rich user experience. By rich user experience I mean high quality graphics, sound 3D etc. Avalon also has various classes related to documents, sound and video. Avalon will make it easy to integrate video and sound into applications by providing the required plumbing all written in managed code and under a uniform framework.

Another pillar or WinFX which is Indigo will be used by applications which based on the web-services architecture. Over the years there have been many frameworks from Microsoft to deal with communication between applications. Indigo takes a step further by providing the best of all under one banner.

## In Summary

WinFX is a set of Managed APIs which do not rely on Win32. WinFX will be available for Windows XP, and Windows 2003. WinFX will be an integral part of the next version of Windows code named "Longhorn".

You can find out the latest information on WinFX at the Longhorn Developer Center on MSDN. http://msdn.microsoft.com/longhorn
