---
title: "Remove Duplicate Lines From A Text File Using LINQ"
date: Fri, 12 Dec 2008 07:47:14 +0000
draft: false
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

A question was posted on c-sharpcorner forums asking how you would [remove duplicate lines from a text file](http://www.c-sharpcorner.com/Forums/ShowMessages.aspx?ThreadID=51446). It got me thinking about how this problem could be addressed using LINQ. Before I get into the solution, here is the problem statement.

#### The problem

I am trying to remove duplicate lines from a text file. To make things difficult the lines contain non unique timestamps but a unique reference number. Some of the duplicates amount to 10 lines whereas others can only be 2 lines. 1. Here are some examples of duplicates lines:<timestamp>,<reference>,<error message> 08:47:22,95847170050,Problem inputting data. 08:48:28,96672540040,More problems inputting data. 08:49:29,95847170050,Problem inputting data. 08:55:28,106622510040,Extra issues inputting data. 08:56:35,95847170050,Problem inputting data. 08:57:35,106622510040,Extra issues inputting data. 09:02:35,96672540040,More problems inputting data. 09:03:41,96672540040,More problems inputting data. 09:04:41,106622510040,Extra issues inputting data.

I want to delete all but KEEP the most recent duplicate line.

On the forum there is also some Java code which has been used as a solution. But I will ignore it so that I can approach it from a fresh perspective.

#### Solution The LINQ Way

Here is my approach to remove duplicate lines from a text file. Firstly, I read the contents of the file into a collection of Type List<Error> using an approach [I described in an earlier post](https://bitofbinary.com//2008/08/13/tutorial-reading-a-text-file-using-linq/) .

```csharp
var query = from e in
(from line in File.ReadAllLines(originalFile)
let errorRecord = line.Split(',')
let timestamp = errorRecord\[0\].Split(':')
select new Error()
{
 TimeStamp = new TimeSpan(
Convert.ToInt32(timestamp\[0\]),
Convert.ToInt32(timestamp\[1\]),
Convert.ToInt32(timestamp\[2\])),
Reference = errorRecord\[1\],
Message = errorRecord\[2\]
})
select e;
```

This is what my Error class looks like. This class maps to a record in the file.

```csharp
public class Error
{
public TimeSpan TimeStamp { get; set; }
public string Reference { get; set; }
public string Message { get; set; }
}

```

Once I have the collection loaded up from the file. I then use a LINQ query to select the results I want. This query uses combination of group by and aggregates to select the most current record for a reference number as per the original problem statement.

```csharp
var query = from e in errorCollection
group e by new { e.Reference, e.Message } into g
let MaxDate = g.Max(x => x.TimeStamp)
select new Error
{
TimeStamp = MaxDate,
Reference = g.Key.Reference,
Message = g.Key.Message
};

```

Finally I write the collection I get from the query above to another text file.

```csharp
List newList = query.ToList();

using (StreamWriter sw = new StreamWriter(processedFile))
{
newList.ForEach(x => sw.WriteLine(x.TimeStamp+","+x.Reference+","+x.Message));
sw.Close();
}

```

The code which loads the collection from the file can be optimized for performance but it does a good job when dealing with a reasonably small file. Below is the full code for my two methods.

```csharp
public void RemoveDuplicates(string originalFile, string processedFile)
{
List errorCollection = ReadFileIntoCollection(originalFile);

var query = from e in errorCollection
group e by new { e.Reference, e.Message } into g
let MaxDate = g.Max(x => x.TimeStamp)
select new Error
{
TimeStamp = MaxDate,
Reference = g.Key.Reference,
Message = g.Key.Message
};

List newList = query.ToList();

using (StreamWriter sw = new StreamWriter(processedFile))
{
newList.ForEach(x => sw.WriteLine(x.TimeStamp+","+x.Reference+","+x.Message));
sw.Close();
}
}

public List ReadFileIntoCollection(string originalFile)
{
List errorCollection = null;

var query = from e in
(from line in File.ReadAllLines(originalFile)
let errorRecord = line.Split(',')
let timestamp = errorRecord\[0\].Split(':')
select new Error()
{
TimeStamp = new TimeSpan(
Convert.ToInt32(timestamp\[0\]),
Convert.ToInt32(timestamp\[1\]),
Convert.ToInt32(timestamp\[2\])),
Reference = errorRecord\[1\],
Message = errorRecord\[2\]
})
select e;

errorCollection = query.ToList();
return errorCollection;
}

```

So this is my approach to remove duplicates from a text file using LINQ. This is just one example of how LINQ can be used to create creative solutions to some common programming problem. The power of LINQ lies in its simplicity which you can use to write beautiful code.
