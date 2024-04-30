---
title: "Tutorial Reading A Text File Using LINQ"
date: Wed, 13 Aug 2008 05:00:14 +0000
draft: false
featured_image: "dotnet.svg"
tags: [".NET", "C#", "LINQ"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

### Introduction

At times us developers have to deal with delimited text files in our applications. Such files have been around since yonks and I often come across data import/export tasks where delimited files are used. Till now the common way in .NET has been to read each line and then extract data using some sort of creative string functions within for loops. But there is another way by using LINQ. In this tutorial I will show you how to use LINQ to read such data. By the end of tutorial you will appreciate how easy and logical it is to use LINQ for reading data from delimited text files.

### Sample Data

I will use a sample file which contains a data about customers. When working with text files we must know the number of columns and the data contained in each column. Below is a list of columns in their right order for our file.

1.  First Name
2.  Last Name
3.  Job Title
4.  City
5.  Country

The file itself will contain this data. I have pulled this out of Employees table in Northwind database. ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/08/image23.png)

### Reading Data

Before we start reading our csv file we will create a class which will hold a record we will read from our csv file. For this I will create a customer class which looks like this. I know I pulled data from Employees table so just imagine that data above is customer data. Employees can also be customers ;)

```csharp
public class Customer
{
string Firstname { get; set; }
string Lastname { get; set; }
string JobTitle { get; set; }
string City { get; set; }
string Country { get; set; }
}
```

### Reading Entire File

Now we are ready to read data from our file using LINQ. Using this code we can read the entire file. I am also using a foreach statement to output the results.

```csharp
var query =
  from line in File.ReadAllLines(filePath)
let customerRecord = line.Split(',')
select new Customer() {
  Firstname = customerRecord[0],
    Lastname = customerRecord[1],
    JobTitle = customerRecord[2],
    City = customerRecord[3],
    Country = customerRecord[4]
};

foreach(var item in query) {
  Console.WriteLine("{0}, {1}, {2}, {3}, {4}",
    item.Firstname, item.Lastname, item.JobTitle, item.City, item.Country);
}
```

File.ReadAllLines() returns an array of lines and we then use the split function of array to split it by a comma. Its just that simple.

##### Reading selected records

We can use this code to read all customers who live in UK.

```csharp
var query =
  from c in
  (from line in File.ReadAllLines(filePath) let customerRecord = line.Split(',')
    select new Customer() {
      Firstname = customerRecord[0],
        Lastname = customerRecord[1],
        JobTitle = customerRecord[2],
        City = customerRecord[3],
        Country = customerRecord[4]
    })
where c.Country == "UK"
select c;
```

This code can be used to read customers who have sales in their job title.

```csharp
var query =
  from c in
  (from line in File.ReadAllLines(filePath) let customerRecord = line.Split(',')
    select new Customer() {
      Firstname = customerRecord[0],
        Lastname = customerRecord[1],
        JobTitle = customerRecord[2],
        City = customerRecord[3],
        Country = customerRecord[4]
    })
where c.JobTitle.Contains("Sales")
select c;
```

I am sure that above queries can be polished by using a bit more syntax sugar but I am just too excited to see LINQ working with a csv file.

### Conclusion

LINQ makes it extremely simple to work with delimited text files. Once we have the records from a csv file in an object we can use all the power of LINQ to query our hearts out on such files. This functionality is available to us via LINQ to objects and we do not need another flavour of LINQ to achieve this. Stay tuned for more posts on LINQ.
