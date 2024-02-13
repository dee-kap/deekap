---
title: "Enum Support With LINQ to SQL and SqlMetal"
date: Tue, 18 Nov 2008 00:47:00 +0000
draft: false
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

As a programmer I love my enums. I find code written using enums to be more readable than without them. However, there has been and there still is a disconnect between lookup tables in a database and enums in code. One has to restore to some creative trickery to get them working in harmony. Recently while working on a project which involves using LINQ To SQL, I came up with a process which gives me the best of both worlds i.e. using lookup tables in database and enums in code. I am documenting my solution here. Hopefully it will help you.



#### The problem

In my database I have two tables. To make things simple I will call them Customer and CustomerStatus. Customer table stores information about a customer and CustomerStatus table is a lookup table which will store values such as "Active" and "Inactive". ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image6.png) For CustomerStatus I would like to use an enum in code. This can be done using the designer as explained [here](http://geekswithblogs.net/robp/archive/2008/05/19/using-c-enumerations-as-linq-to-sql-entity-properties.aspx). But I would like to use SqlMetal to automate code generation. SqlMetal does not have any options which can be used to solve my problem.

#### My Solution

My solution is to generate dbml file using SqlMetal, then run a custom process which modifies dbml to make it enum ready and finally generate code using SqlMetal looking over dbml file. ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image7.png)

##### Step 1

Step 1 is to generate a dbml file from database using SQLMetal with a statement like this: SqlMetal /server:. /database:CustomerDb /dbml:CustomerDb.dbml /namespace:CustomerApp In the dbml file I look at the column element generated for CustomerStatusID in Customer Table node. I find that it’s Type is set to System.Int32 ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image8.png)

##### Step 2

Step 2 involves writing a process which could just be a simple console application. This process looks for usage of lookup table’s Id colum in main table and replaces the value of Type attribute with corresponding enum. I am following a naming convention so that my enums are all suffixed with Enum and in database the foreign key field on my main table is named <lookup table name> + Id. ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image9.png)

##### Step 3

Generate code with SqlMetal. Use the option which works with a dbml file. Here is a sample statement: SqlMetal /code:Customer.cs /map:CustomerDb.map CustomerDb.dbml

Generated code now uses the enum for CustomerStatusId property rather than System.Int32

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/11/image10.png)

##### Step 4

A batch file can be created to tie this all up. Batch file will do the following things:

1.  Run SqlMetal to generate dbml file
2.  Run the process which modifies dbml file as mentioned in step 2
3.  Generate code using SqlMetal from dbml file

Doing this allows me to work with enums in my code and at the same use lookup tables in database. As an addition a simple process can also be written which can populate lookup tables with the values from enums.
