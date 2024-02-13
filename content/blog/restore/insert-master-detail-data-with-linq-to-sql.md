---
title: "Insert Master Detail Data With LINQ to SQL"
date: Wed, 08 Jul 2009 02:36:00 +0000
draft: false
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Best thing about writing a blog is interaction with members of developer community. I thoroughly enjoy answering questions which come my way through this site. Early in the morning today I saw a question by [Joey](http://www.joeyesq.com/). To avoid loosing details in paraphrasing, here is the exact question asked by Joey.

> I’m new to LINQ. If I had two tables “Customer” and “CustomerDetails”, how (using LINQ) can I insert to both of these tables? Do I need to create a “Customer” object as well as a “CustomerDetails” object?

In short the answer is yes. LINQ can insert to both tables, you will need to populate both Customer and CustomerDetails objects with data. I will now present an example to support my answer. What we have here is a one to many scenario which involves two tables linked through a Foreign Key. To serve as an example, I have modelled the tables like this. ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/07/image12.png "image") Each customer can have many nick names which are stored in CustomerDetails table. Let’s go ahead and generate LINQ To SQL entities. Please refer to [LINQ To SQL tutorial](http://www.debugrelease.com/linq-to-sql-tutorial/) if you want a refresher on how to generate LINQ To SQL entities. After dragging our tables to designer we can see that designer has recognised relationship we have between our tables. ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/07/image13.png "image") A quick glance over generated code confirms that we have a property of Type EntitySet<CustomerDetails> in our Customer class. ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/07/image14.png "image") Now let’s insert some data. The following code will insert one Customer record and two CustomerDetails records.`private void InsertData()
{
  string firstName = "LINQ";
  string lastName = "Dude";
  string nickName1 = "Cool";
  string nickName2 = "DataBuster";`using (CustomerDatabaseDataContext context = new CustomerDatabaseDataContext()) { // Create a Customer object Customer customer = new Customer { FirstName = firstName, LastName = lastName, // Create two CustomerDetails objects CustomerDetails = new System.Data.Linq.EntitySet<CustomerDetail>() { new CustomerDetail{NickName = nickName1}, new CustomerDetail{NickName = nickName2} } }; // We'd like to Insert our changes as new context.Customers.InsertOnSubmit(customer); // Submit changes to database context.SubmitChanges(); } } Code above produces following T-SQL```
exec sp_executesql N'INSERT INTO \[dbo\].\[Customer\](\[FirstName\], \[LastName\])
VALUES (@p0, @p1)

```SELECT CONVERT(Int,SCOPE_IDENTITY()) AS [value]',N'@p0 varchar(4),@p1 varchar(4)', @p0='LINQ',@p1='Dude' go exec sp_executesql N'INSERT INTO [dbo].[CustomerDetails]([CustomerId], [NickName]) VALUES (@p0, @p1) SELECT CONVERT(Int,SCOPE_IDENTITY()) AS [value]',N'@p0 int,@p1 varchar(4)', @p0=2,@p1='Cool' go exec sp_executesql N'INSERT INTO [dbo].[CustomerDetails]([CustomerId], [NickName]) VALUES (@p0, @p1) SELECT CONVERT(Int,SCOPE_IDENTITY()) AS [value]',N'@p0 int,@p1 varchar(10)', @p0=2,@p1='DataBuster' go In T-SQL above you can see that we are inserting one row for Customer and two rows for CustomerDetails. However in our C# we only called SubmitChanges once.

```
