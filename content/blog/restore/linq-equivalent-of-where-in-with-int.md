---
title: "LINQ Equivalent Of Where IN With Int"
date: Mon, 05 Jan 2009 07:55:04 +0000
draft: false
tags: ["Microsoft"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Earlier I wrote a post showing how to write a [LINQ query which gets transformed into a T-SQL query with a "Where In" clause](https://bitofbinary.com//2008/08/25/linq-equivalent-of-where-in/). I had a comment on the post by Steve saying that the approach only works with strings. In this post I will show you a similar query which works with Integers.

Let's say that we want to select rows from Products table in Northwind database where ProductId matches 3, 7, 8, 10. Our query should include the Where IN clause. Something like this:

```
SELECT \*
FROM Products
WHERE ProductID in (3, 7, 8, 10)
```

Of course Select \* is not a good way to write any Query but this is just to convey a point. LINQ query which will work with integers and give me a Where IN looks like this:

```
List<int> productIds = new List<int> { 3, 7, 8, 10 };

using (NorthwindDataContext context = new NorthwindDataContext())
{
  var query = from p in context.Products
    where productIds.Contains(p.ProductID)
    select p;
}
```

This results in the following T-SQL query:

```
exec sp\_executesql N'SELECT \[t0\].\[ProductID\], \[t0\].\[ProductName\], \[t0\].\[SupplierID\],
\[t0\].\[CategoryID\], \[t0\].\[QuantityPerUnit\], \[t0\].\[UnitPrice\], \[t0\].\[UnitsInStock\],
\[t0\].\[UnitsOnOrder\], \[t0\].\[ReorderLevel\], \[t0\].\[Discontinued\]
FROM \[dbo\].\[Products\] AS \[t0\]
WHERE \[t0\].\[ProductID\] IN (@p0, @p1, @p2, @p3)',N'@p0 int,@p1 int,@p2 int,@p3 int',
@p0=3,@p1=7,@p2=8,@p3=10
```
