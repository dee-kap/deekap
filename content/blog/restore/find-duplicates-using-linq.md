---
title: "Find Duplicates Using LINQ"
date: Sat, 16 Aug 2008 02:18:45 +0000
draft: true
tags: ["Microsoft"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

How can we find duplicate occurrences of values in a collection? I will demonstrate this here using a collection of cities. City class looks like this:`public class City
{
public string Name { get; set; }
public string Country { get; set; }
}`Cities collection is initialised with this code:```
List cities =
new List
{
new City{ Name = "Sydney", Country = "Australia" },
new City{ Name = "Sydney", Country = "Australia" },
new City{ Name = "New York", Country = "USA" },
new City{ Name = "Paris", Country = "France" },
new City{ Name = "Milan", Country = "Spain" },
new City{ Name = "Melbourne", Country = "Australia" },
new City{ Name = "Auckland", Country = "New Zealand" },
new City{ Name = "Tokyo", Country = "Japan" },
new City{ Name = "New Delhi", Country = "India" },
new City{ Name = "Hobart", Country = "Australia" },
new City{ Name = "Boston", Country = "USA"}
};

`Objective is to find countries which occur more than once in the collection and while I am doing that I would also like to know the number of cities for that country. To do this I can use this query. I am using a foreach loop to output my results.`
var query =
from c in cities
group c by c.Country into g
where g.Count() > 1
select new { Country = g.Key, CityCount = g.Count()};

````
 foreach (var item in query)
{
Console.WriteLine("Country {0} has {1} cities", item.Country, item.CityCount);
}

```By running the above query I get this output which is correct as there are only two countries in the collection which have more than one city.
````
