---
title: "Use SqlConnection With LINQ to SQL"
date: Tue, 16 Sep 2008 01:25:00 +0000
draft: true
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

LINQ To SQL allows us to use a SqlConnection object to connect to a database. The way to use a SqlConnection is to pass it as a parameter to DataContext object. DataContext object has constructor which takes in a IDbConnection and SqlConnection implements this Interface. Here I create a SqlConnection object and use it to establish a connection to database.```

// Create a Connection String  
 string connectionString  
 = "Data Source=.;Initial Catalog=Northwind2;Integrated Security=True";

// Create a SqlConnection  
 using (SqlConnection connection = new SqlConnection(connectionString))  
 {  
 // Create DataContext and pass in the connection  
 using (NorthwindDataContext context = new NorthwindDataContext(connection))  
 {  
 var query = from c in context.Customers  
 select c.CompanyName;  
 foreach (var item in query)  
 {  
 Console.WriteLine(item);

      }
    }

}

```

```
