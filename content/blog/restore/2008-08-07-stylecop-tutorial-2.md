---
title: "StyleCop tutorial"
date: Thu, 07 Aug 2008 01:08:00 +0000
draft: false
featured_image: "dotnet.svg"
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

[StyleCop](http://code.msdn.microsoft.com/sourceanalysis) is a source analysis tool for C#. It can be used for analysing source code as opposed to compiled assemblies which is the area for FxCop. StyleCop is currently in version 4.2 and can be downloaded [here](http://code.msdn.microsoft.com/sourceanalysis). In this tutorial I will show you how to use StyleCop. I will create a simple console application and use StyleCop to analyse the source. This killer app just initialises a class and prints out few properties. Below is the code for the application.

```csharp
public class Customer
{
 public string FirstName { get; set; }
 public string LastName { get; set; }
 public string Address { get; set; }
 public CustomerStatus Status { get; set; }
 public override string ToString()
 {
  string result = string.Format
   ("First Name = {0}nLast Name = {1}nAddress = {2}nStatus = {3}"
   , FirstName, LastName, Address, Status);
  return result;
 }
}

public enum CustomerStatus
{
 Active,
 InActive
}

class Program
{
 static void Main(string\[\] args)
 {
  Customer customer = new Customer
  {
   FirstName = "John",
   LastName = "Smith",
   Address = "1 George Street, Sydney",
   Status = CustomerStatus.Active
  };
  Console.WriteLine(customer.ToString());
  Console.ReadKey();
 }
}
```

I can run source code analysis on the entire project via Tools menu or an individual file by right clicking on the class file.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/08/image6.png)

By running source analysis on Program.cs I get 34 violations.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/08/image7.png)

Depending on your style or your coding standards, you will either agree or disagree with detected violations. For example in the result above I do not agree with rule SA1200 “All using directives must be placed inside of the namespace”. I have never declared my using statements inside the namespace and I do not intend to do so in future. So what can I do? I can easily modify the rule set. Let’s see how we can do this. By default StyleCop is installed at C:Program FilesMicrosoft Source Analysis Tool for C#. A quick glance over the contents of this folder look like this.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/08/image8.png)

Notice the second last file which is Settings.SourceAnalysis. Double clicking it opens up the SourceAnalysisSettingsEditor where I can select/deselect the rules.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/08/image9.png)

I can turn off rule SA1200 “All using directives must be placed inside of the namespace” and then if I run analysis again, my result set will not show it as a rule violation.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/08/image10.png)

As you can see from screenshots above that rules are categorised into different categories such as Documentation Rules, Layout Rules, Naming Rules etc. This makes is easy work with rules in a logical way.

### Conclusion

StyleCop is a light weight source code analysis tool which fills in the necessary gap. One of the benefits of StyleCop can be realised while conducting code reviews. Lately StyleCop has had its own share of controversy, but it is good that Microsoft is paying attention to this nifty tool which could attract a significant user base. StyleCop can be downloaded [here](http://code.msdn.microsoft.com/sourceanalysis).
