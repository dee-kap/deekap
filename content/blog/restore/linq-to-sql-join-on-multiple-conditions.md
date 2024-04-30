---
title: "LINQ To SQL Join On Multiple Conditions"
date: Tue, 16 Sep 2008 07:07:30 +0000
draft: false
tags: ["Microsoft"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Two tables have PostCode and CouncilCode as common fields. Lets say that we want to retrieve all records from ShoppingMall where both PostCode and CouncilCode on House match. This requires us to do a join using two columns. In LINQ such a join can be done using **anonymous types**. Here is an example.```
var query = from s in context.ShoppingMalls
join h in context.Houses
on
new { s.CouncilCode, s.PostCode }
equals
new { h.CouncilCode, h.PostCode }
select s;

`The code above gets translated into this SQL query.`
SELECT \[t0\].\[ShoppingMallId\], \[t0\].\[Address\],
\[t0\].\[PostCode\], \[t0\].\[CouncilCode\]
FROM \[dbo\].\[ShoppingMall\] AS \[t0\]
INNER JOIN \[dbo\].\[House\] AS \[t1\]
ON (\[t0\].\[CouncilCode\] = \[t1\].\[CouncilCode\])
AND (\[t0\].\[PostCode\] = \[t1\].\[PostCode\])

```And when the above query is executed it produces the results we want.

```
