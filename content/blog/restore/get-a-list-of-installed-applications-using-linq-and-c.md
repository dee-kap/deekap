---
title: "Get A List Of Installed Applications Using LINQ And C#"
date: Fri, 29 Aug 2008 23:59:50 +0000
draft: false
tags: ["Microsoft"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

To get a list of installed applications we need to look into registry. Microsoft.Win32 namespace contains objects which can be used to work with Windows Registry. In this post I will show you some code where I use the power of LINQ to retrieve and display a list of all applications installed on a machine. The basic idea is that we iterate through a collection of RegistryKey objects within LocalMachineSOFTWAREMicrosoftWindowsCurrentVersionUninstall. We then open the sub keys and get the DisplayName. Here is the code:```
static void DisplayInstalledApplications()
{
string registryKey =
@"SOFTWAREMicrosoftWindowsCurrentVersionUninstall";

using (Microsoft.Win32.RegistryKey key =
Registry.LocalMachine.OpenSubKey(registryKey))
{
var query = from a in
key.GetSubKeyNames()
let r = key.OpenSubKey(a)
select new
{
Application = r.GetValue("DisplayName")
};

    foreach (var item in query)
    {
      if (item.Application != null)
        Console.WriteLine(item.Application);
    }

}
}

```

I can also make this a bit more LINQed by removing the foreach loop. It just adds a bit more C# 3.0 flavour to the code and does the retrieval and writing to console in one line.

```

static void DisplayInstalledApplications2()
{
string registryKey =
@"SOFTWAREMicrosoftWindowsCurrentVersionUninstall";

using (Microsoft.Win32.RegistryKey key =
Registry.LocalMachine.OpenSubKey(registryKey))
{
(from a in key.GetSubKeyNames()
let r = key.OpenSubKey(a)
select new
{
Application = r.GetValue("DisplayName")
}).ToList()
.FindAll(c => c.Application != null)
.ForEach(c => Console.WriteLine(c.Application));
}
}

```

I hope you found this post useful.
```
