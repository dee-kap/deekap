---
title: "LINQ Equivalent Of Where IN"
date: Mon, 25 Aug 2008 00:05:01 +0000
draft: false
tags: ["Microsoft"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Working with LINQ to SQL I came across a need of writing a LINQ query equivalent of  T-SQL "Where IN" clause. This is what T-SQL query looks like.```
SELECT CustomerID, CompanyName, ContactName, ContactTitle, Address,
City, Region, PostalCode, Country, Phone, Fax
FROM Customers
WHERE (Country IN ('UK', 'USA', 'Australia'))

```

#### How do I write Where IN in LINQ?

Below is the query which can be used for a "WHERE IN" scenario. Query 1 uses query syntax and Query 2 uses lambda expression. I am using using a DataContext for Northwind database. See [LINQ To SQL Tutorial](https://bitofbinary.com//2008/07/31/linq-to-sql-tutorial/) to see how to generate a DataContext.

##### LINQ Query 1

```

string\[\] countries = new string\[\] { "UK", "USA", "Australia" };
var customers =
from c in context.Customers
where countries.Contains(c.Country)
select c;

```

##### LINQ Query 2

```

string\[\] countries = new string\[\] { "UK", "USA", "Australia" };
var customers =
context.Customers
.Where(c => countries.Contains(c.Country));

```

```
