---
title: "Execute Stored Procedure With ADO.NET Data Services"
date: Sun, 16 Aug 2009 02:42:00 +0000
draft: true
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

### Introduction

In an [earlier article](http://www.debugrelease.com/adonet-data-services-tutorial-with-aspnet/) I looked at how DO.NET Data Services can be used with ASP.NET. In this post I will talk about using ADO.NET Data Services to retrieve data via SQL Server stored procedure. Doing this is simple and I will follow a similar approach to hook everything up as I did in my [earlier post](http://www.debugrelease.com/adonet-data-services-tutorial-with-aspnet/). I have created a stored procedure which retrieves data from Employees table in Northwind database based on city name. Here is the script I used to create the procedure.

```
CREATE PROCEDURE \[dbo\].\[GetEmployeesByCity\]
    @City NVARCHAR(15)
AS

BEGIN

    SELECT \*
    FROM Employees
    WHERE City = @City

END

```

### Creating Data Model

ADO.NET Data Services sits between the client and a data source, so the first thing I’ll need is a data source. I will use Entity Framework to create my data source.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/08/image13.png "image")

To make things simple I will select Employees table only for my Entity Data Model.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/08/image14.png "image")

### Mapping Stored Procedure in EDM

My objective here is to retrieve data from a stored procedure. To this I need to expose the procedure through my data layer which I have created using Entity Framework. Mapping a stored procedure in Entity Framework can be done by following these steps. Open Model Browser (View –> Other Windows –> Model Browser). Right click on Stored Prodecures under NorthwindModel.Store and click Update Model from Database.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/08/image6.png "image")

Select the stored procedure (GetEmployeesByCity in this case) and click Finish.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/08/image7.png "image")

Go back to Model Browser and under stored procedure right click the stored procedure and click Create Function Import.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/08/image8.png "image")

Select Employees entity as the return type and click OK.

![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/08/image9.png "image")

Entity Model is now setup to execute the stored procedure and return results. It can be called like this.

````
NorthwindEntities entities = new NorthwindEntities();
var employees = entities.GetEmployeesByCity("London");
```My goal however is to retrieve data via ADO.NET Data Services so I’ll start creating my service.

### And Now With a Service

Because I’d like to access this data through my ADO.NET Data Service so the first thing I’ll do is create a service called NorthwindEmployeeService. I will add a new item to my project of type ADO.NET Data Service.

  ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/08/image10.png "image")

 Visual Studio creates a blank service with some scaffolding for me to get started. First thing I need to do is let my service know about my data source class and then configure appropriate rights to my entities and operations. To be simple I will just allow everything. Below is the code for my service after making changes.
````

public class NorthwindEmployeeService : DataService<NorthwindEntities>  
{  
 // This method is called only once to initialize service-wide policies.  
 public static void InitializeService(IDataServiceConfiguration config)  
 {  
 config.SetEntitySetAccessRule("\*", EntitySetRights.AllRead);  
 config.SetServiceOperationAccessRule("\*", ServiceOperationRights.All);  
 }  
}

```By default my service does not know that it should also work with a stored procedure. To do this i can write a method which will execute the procedure and return results. Such a method can look like this.

```

\[WebGet\]  
public ObjectResult<Employees> GetEmployeesByCity(string cityName)  
{  
 NorthwindEntities entities = new NorthwindEntities();  
 return entities.GetEmployeesByCity(cityName);  
}

```Method above tells the service to expose a GetEmployeesByCity method which can be called by clients. Note that the method is decorated with a WebGet attribute which indicates that this is a GET method which can be called by a web client.

### Running Service and Calling Stored Procedure

To see my service in action I can hit F5

  ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/08/image11.png "image")

 To see the results from the stored procedure I can use the following URL. http://localhost:16147/NorthwindEmployeeService.svc/GetEmployeesByCity?cityName=’London’ Here I am passing in the parameter as a query string which is accepted by my service and appropriate results are returned.

  ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/08/image12.png "image")

### Conclusion

In this article I used ADO.NET Data Services to execute a stored procedure and return results. I am not in favour of implementing a direct mapping between services and database and the design can be a little better whereby data layer can be sensibly abstracted away by service. However the idea was to demonstrate a concept. I hope you enjoyed reading this article.
```
