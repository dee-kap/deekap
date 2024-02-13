---
title: "Dynamic sort with LINQ"
date: Mon, 04 Aug 2008 01:05:00 +0000
draft: false
featured_image: "dotnet.svg"
tags: [".NET"]
---

In this post I will show you how to perform dynamic sorting with LINQ. I will work with a simple collection of City class. City class is defined below.

```csharp

public class City
{
  public string Name { get; set; }
  public string Country { get; set; }
}
```

The collection is initialised using this code

```csharp
List cities = new List {
 new City{ Name = "Sydney", Country = "Australia" },
 new City{ Name = "New York", Country = "USA" },
 new City{ Name = "Paris", Country = "France" },
 new City{ Name = "Milan", Country = "Spain" },
 new City{ Name = "Melbourne", Country = "Australia" },
 new City{ Name = "Auckland", Country = "New Zealand" },
 new City{ Name = "Tokyo", Country = "Japan" },
 new City{ Name = "New Delhi", Country = "India" },
 new City{ Name = "Hobart", Country = "Australia" }
 };
```

A typical example of applying a sort will be to write such a query.

```csharp
var collection =
 from c in cities
 orderby c.Country
 select c;
```

Here we are sorting the collection on country. Note that this is static in nature. Code above as you can see can only sort by country. If I wanted to sort by city name then I’d be writing another query and maybe use a conditional construct such as if or switch and write a method which takes in a parameter. While this will work, it is not the best way to do it. LINQ gives us the ability to make our code dynamic. I can provide sort functionality for my query by writing a method which takes in a Func<TElement, TKey> delegate. This delegate is used by the OrderBy extension method. This is how I can write my method.

```csharp
public static void Sort(List cities, Func selector)
{
 var sortedCollection =
 from c in cities
 orderby selector(c)
 select c;

foreach (var item in sortedCollection)
 {
 Console.WriteLine(item.Name);
 }
}
```

This method can be called like this by passing in the cities collection which has been initialised earlier.

```csharp
Sort(cities, c => c.Name);
```

I can also sort by country without changing my query. To sort by country I just need to call my sort method like this.

```csharp
Sort(cities, c => c.Country);
```

LINQ is very powerful when you start using it on daily bases. It would not be very useful if everything was static. In this post I showed you how you can make your sorting code dynamic. Stay tuned for more LINQ goodness.
