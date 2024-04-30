---
title: "LINQ To SQL Tutorial"
date: Thu, 31 Jul 2008 05:27:04 +0000
draft: false
featured_image: "dotnet.svg"
tags: [".NET", "LINQ"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

### Introduction

With .NET Framework 3.5 Microsoft released Language Integrated Query aka LINQ. LINQ enables developers to query data sources using a query like syntax with both C# and VB.NET. These data sources can be collections, SQL Server databases, XML, DataSets etc. Other than what is supplied by Microsoft, LINQ is also extensible. This means that you can query data sources beyond what Microsoft ships. Examples of such implementations are LINQ To Flickr, LINQ To Amazon, LINQ to Google etc. In this article I will show you how you can use LINQ To SQL to perform CRUD operations on a SQL Server database. I will use Northwind database and build an ASP.NET application to demonstrated the capabilities of LINQ To SQL. You can download Northwind database [here](http://www.microsoft.com/downloads/details.aspx?FamilyID=06616212-0356-46A0-8DA2-EEBC53A68034&displaylang=en).

### Toolset for this article

1.  Visual Studio 2008
2.  .NET Framework 3.5 (This is already installed if you have Visual Studio 2008)
3.  SQL Server 2005 (You can also work with SQL Server Express)

### Solution Structure

For this article we will need two projects. One is a data layer (created as a Class Library)which we will generate and the other is an ASP.NET Web Application. The solutions structure looks like this in Solution Explorer. ![LINQ](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/07/image-thumb3.png)

### Creating Data Layer

Before we generate our data layer we must create a new connection in Server Explorer which points to Northwind database. ![LINQ](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/07/image-thumb8.png) We will now generate our data layer using LINQ To SQL. To do this you need to add a new item to the data layer project of type LINQ to SQL Classes. We will name it Northwind as shown below. ![LINQ](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/07/image41.png) After adding a LINQ to SQL Class we are presented with a designer surface. Here we can simply drag the tables which will become part of our data layer. For this article we will drag all tables on the designer by selecting them all in one go. Our designer should look like this after dragging all tables on it. ![LINQ](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/07/image30-thumb.png) We should now build our solution to make sure everything is okay. And that's it. We have successfully generated our data layer. In Solution Explorer we can see that we have two new files namely Northwind.dbml.layout and Northwind.designer.cs. We can also see that references required to compile and run our code have been added by Visual Studio. ![LINQ](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/07/image36.png) The .cs file contains the code for our data layer. Let's examine the code that has been generated for us. We will look at the Region class.

```csharp
[Table(Name="dbo.Region")]
public partial class Region : INotifyPropertyChanging, INotifyPropertyChanged
```

The class itself is decorated with Table attribute and the Name property has been assigned the actual table name we have in our database. Region class also implements INotifyPropertyChanging and INotifyPropertyChanged interfaces. These interfaces are used for databinding. Region class also contains one property per column. Let's look at the RegionDescription property.

```csharp
[Column(Storage="\_RegionDescription", DbType="NChar(50) NOT NULL", CanBeNull=false)]
public string RegionDescription {
  get {
    return this.\_RegionDescription;
  }
  set {
    if ((this.\_RegionDescription != value)) {
      this.OnRegionDescriptionChanging(value);
      this.SendPropertyChanging();
      this.\_RegionDescription = value;
      this.SendPropertyChanged("RegionDescription");
      this.OnRegionDescriptionChanged();
    }
  }
}
```

Columns are decorated with Column attribute and values are passed in for Storage, DbType and CanBeNull which indicates if the column can be null or not.

### Using Data Layer

Now that we have generated our data layer. We will work on ASP.NET web application where we will use our data layer. To keep things simple we will create a web forms to search for customers and display search results. We will also create a web form to insert new customers. Let's start by creating our web form for customer search. For this we will use the Default.aspx page. We will place few controls on the web form. These controls will give us search parameters and a button which will do the search and display results when clicked. This is what the form will look like after placing our controls. ![LINQ](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/07/image-thumb13-thumb.png) We will also place a GridView control on our form to display search results. We will now put in some code in our button's click event handler to do the search and display results in GridView. Make sure that we have a reference to Data Layer project, System.Data.Linq and appropriate using statement. Here is what our button click event handler will contain.

```csharp
protected void buttonSearch_Click(object sender, EventArgs e) {
  using(NorthwindDataContext context = new NorthwindDataContext()) {
    var customers =
      from c in context.Customers
    select c;

    gridViewCustomers.DataSource = customers;
    gridViewCustomers.DataBind();

  }
}
```

This code will query the customers table in northwind database and will return all customers. We will now modify it slightly to accept customer name and company name as parameters for our query. After modification our event handler looks like this.

```csharp
protected void buttonSearch_Click(object sender, EventArgs e) {
  using(NorthwindDataContext context = new NorthwindDataContext()) {
    var customers =
      from c in context.Customers
    where(c.ContactName.Contains(textBoxCustomerName.Text.Trim()) &&
      c.CompanyName.Contains(textBoxCompanyName.Text.Trim()))
    select c;

    gridViewCustomers.DataSource = customers;
    gridViewCustomers.DataBind();
  }
}
```

Our search results will now be filtered. Let us now created a data entry form for customers.  We will insert a new web form in our ASP.NET project and call it CustomerEntry. To start with we will make sure that our form contains fields required to insert a customer. Our form after completion will look like this. ![LINQ](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/07/image.png) We expect a new row to be inserted into customers table when Save Customer button is clicked. This code achieves data insertion into customers table for us.

```csharp
protected void buttonSave_Click(object sender, EventArgs e) {
  using(NorthwindDataContext context = new NorthwindDataContext()) {
    Customer customer = new Customer {
      CustomerID = textBoxCustomerID.Text,
        CompanyName = textBoxCompanyName.Text,
        ContactName = textBoxCustomerName.Text,
        ContactTitle = textBoxTitle.Text,
        Address = textBoxAddress.Text,
        City = textBoxCity.Text,
        Region = textBoxRegion.Text,
        PostalCode = textBoxPostalCode.Text,
        Country = textBoxCountry.Text,
        Phone = textBoxPhone.Text,
        Fax = textBoxFax.Text
    };

    context.Customers.InsertOnSubmit(customer);
    context.SubmitChanges();
  }
}
```

Similarly an existing row in database can be updated by first retrieving the data and then submitting it via DataContext.

### Conclusion

In this tutorial we have not written a single SQL statement to retrieve or insert data into a database. This is the beauty of LINQ To SQL. Further our retrieval code while in C# looks a lot like a query. We can already appreciate the benefits of such a streamlined and unified approach in dealing with data.
