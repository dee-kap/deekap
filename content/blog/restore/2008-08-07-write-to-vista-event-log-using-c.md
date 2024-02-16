---
title: "Write To Vista Event Log Using C#"
date: Thu, 07 Aug 2008 05:37:20 +0000
draft: true
featured_image: "dotnet.svg"
tags: [".NET", "C#"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Event Log is a central place to log application events. These events can be errors, warnings or just information. Each event log entry in Windows Vista has a level of event, date and time the event occurred, source of event, an event Id and a task category. While event logs such as Application, System, Security exist by default, you can also create your own event log. ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/08/image11.png) You can also write to event log from your own application using **System.Diagnostics.EventLog** class. The best practice is to check if the source exists. If it does not then you should create it before you write to it.

```csharp
string source = "EventLog Demo";
if (!EventLog.Exists(source))
    EventLog.CreateEventSource(source, "Application");
```

We can now safely write to event log with a statement like this.

```csharp
EventLog.WriteEntry(source, "Writing Error", EventLogEntryType.Error, 7);
```

In the above statement I am writing an event of type error. There are five EventLogEntryType values available. Event viewer will show the appropriate icon depending on the entry type. ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/08/image12.png) After executing the code we can verify that my event entry is viewable in Event Viewer. ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/08/image13.png) Writing application events into Event Log should be a standard message/error logging practice for any application. Windows provides this standard location where it records its own events and this is where you look first when troubleshooting. Thus it makes perfect sense to use this for your own custom applications.
