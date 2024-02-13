---
title: 'ADO.NET Data Services With ASP.NET'
date: Tue, 28 Jul 2009 02:39:00 +0000
draft: false
tags: ['.NET']
---

### Introduction

In this tutorial we will look at how ADO.NET Data Services can be used to create services which are consumed by ASP.NET client. We will use Adventure works Lite database as an example to demonstrate the concepts. Code for this article can be downloaded at the bottom of the article. ADO.NET Data Services as the name says is a services layer between your application and an underlying data source. It uses REST principals to access and persist information to and from the data source. Services layer itself can be created very easily. Most of the work is done by Visual Studio for you. In this tutorial we will build an application for AdventureWorks Lite database. We will build a page which let’s a user browse through products. The reason for picking up AdventureWorks Lite as an example is so that we can work with a variety of data including images. If you do not have AdventureWorks Lite then you can download it [here](http://www.codeplex.com/Wiki/View.aspx?ProjectName=SqlServerSamples). For our application we will work with this data model  
  
  ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/07/image46.png "image")  

###   

### Creating Service

Creating a ADO.NET Data Service in Visual Studio is a no brainer. All we need to do is add a new item of type ADO.NET Data Service, give it an appropriate name and we are done.  
  
  ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/07/image47.png "image")  
  
Our ADO.NET Service will interact with some kind of data source and Entity Framework perfectly fits that purpose. We now need to create a EDM (Entity Data Model) which includes tables we want to interact with via our services. If you never worked with Entity Framework then [this quickstart](http://msdn.microsoft.com/en-us/library/bb399182.aspx) will get you going. By creating a service and our Entity Data Model we have put together two major components of our solution. Before we can hit F5 to see our service running, there are few things we need to put in place. We must tell our service that there is a Data Layer that we want it to use. Now all ADO.NET Data Services inherit from DataService<T> which can be found in System.Data.Services namespace. The code produced by Visual Studio for our service leaves a placeholder for <T> with a comment. All we need to do is specify the correct type. Our class declaration for our service should look like this.  
```
public class AdventureWorksService : DataService<AdventureWorksEntities>
```Here we have established integration between our service and our data source. Next thing we need to do is configure appropriate access levels for our service and its operations. Code below when executed initializes our service to have all possible access over all entities defined in our EDM and all access over all operations. Note the asterix, basically we are saying here that include all Entity Sets and all operations.  
```
public static void InitializeService(IDataServiceConfiguration config)  
{  
  config.SetEntitySetAccessRule("\*", EntitySetRights.All);  
  config.SetServiceOperationAccessRule("\*", ServiceOperationRights.All);  
}
```We are now ready to go and hit F5. If we set AdventureWorksService.svc as a start page and run our project we can see our service running. Now that we have our service running, we will start building our ASP.NET pages which will query our service, receive and display data.  
  
  ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/07/image48.png "image")  

###   

### Creating Proxy Objects

Our ASP.NET application will need to access the service through a proxy. Creating a proxy is very easy. After making sure that our service is running, we need to add a service reference to our serivce. This can be done this way.  
  
 ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/07/image49.png "image")  
  
 It is also a good idea to change the Namespace from ServiceReference1 to AdventureWorksService.  

### Creating Web Page To Display Data

We can now make calls to our service and retrieve data. First thing we need to do is load data from ProductCategory and bind it to a dropdown. But before that let’s have a look at what we will produce.  
  
  ![image](https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2009/07/image50.png "image")  
  
Getting back to binding our dropdown control. We should write a query which calls our service which in turns fetches data from database and delivers to us. One good thing about ADO.NET Data Services is that you can write LINQ queries with it. ADO.NET Data Services comes with a LINQ provider popularly known as LINQ To REST. Without LINQ support ADO.NET Data Services will be just too complicated and IMO useless. However LINQ support is limited. Here are things you cannot do:  

1.  You cannot write queries which involve joins or sub queries.
2.  You cannot create anonymous types in your queries.
3.  Aggregates such as Count, Min, Max are not available.
4.  There is no GroupBy support available.

Besides the list of can’t do above, LINQ To REST still makes working with ADO.NET Data Services much easier than otherwise. Following code will make a service call and bind our drop down.  
```
private void BindProductCategories()  
{  
  DataServiceQuery<ProductCategory> productCategories =  
    context.CreateQuery<ProductCategory>("/ProductCategory");  
  
  var query = from p in productCategories  
    orderby p.Name  
    select p;  
  
  ddlProductCategory.DataSource = query;  
  ddlProductCategory.DataBind();  
}
```We’d also like to refresh data in our grid when the user selects another category. This is done by BindProductsGrid method.  
```
private void BindProductsGrid()  
{  
  int productCategoryID = Convert.ToInt32(ddlProductCategory.SelectedValue);  
  
  DataServiceQuery<Product> products =  
    context.CreateQuery<Product>("/Product");  
  
  var query = from p in products  
    where p.ProductCategory.ProductCategoryID == productCategoryID  
    select p;  
  
  gdvProducts.DataSource = query;  
  gdvProducts.DataBind();  
}
```The way I bind the image is by using another page which just does Response.BinaryWrite. Here is the markup of default.aspx page which is the entire UI. You can play with it by downloading the entire solution. The markup is here just to make the post look good ;)  
```
<form id="form1" runat="server">  
  <div>  
    <div>  
      Product Category  
      <asp:DropDownList ID="ddlProductCategory" runat="server"  
        DataValueField="ProductCategoryID"  
        AutoPostBack="true"  
        DataTextField="Name"  
        OnSelectedIndexChanged="ddlProductCategory\_SelectedIndexChanged">  
      </asp:DropDownList>  
    </div>  
    <br />  
    Products  
    <br />  
    <div>  
      <asp:GridView ID="gdvProducts" runat="server"  
        CssClass="sample"  
        Width="600px"  
        AutoGenerateColumns="false"  
        OnRowCreated="gdvProducts\_RowCreated">  
        <Columns>  
          <asp:BoundField DataField="ProductNumber" HeaderText="Number" />  
          <asp:BoundField DataField="Name" HeaderText="Name" />  
          <asp:TemplateField>  
            <ItemTemplate>  
              <asp:Image ID="Image1" runat="server" ImageUrl='ImageHelper.aspx' />  
            </ItemTemplate>  
          </asp:TemplateField>  
        </Columns>  
      </asp:GridView>  
    </div>  
  </div>  
</form>
```

### Conclusion

This was a brief introduction to ADO.NET Data Services. We looked at how to create a service and consume it in a ASP.NET website. We also looked at some limitations of LINQ provider used by ADO.NET Data Services. In future posts I will talk about other features of ADO.NET Data Services.