---
title: 'Deep Cloning In C#'
date: Mon, 01 Sep 2008 07:08:23 +0000
draft: false
tags: ['Uncategorized']
---

To make an object cloneable in .NET we should implement ICloneable interface. ICloneable is a simple interface with only one method Clone(). In this post I will show you how to make a deep clone of an object.```
class Program
    {
        static void Main(string\[\] args)
        {
            Customer c1 = new Customer
            {
                FirstName = "John",
                LastName = "Smith",
                Limit = new CreditLimit
                {
                    AccountOverdue = false,
                    ApprovedAmount = 1000
                }
            };

            Customer c2 = (Customer)c1.Clone();
            c2.FirstName = "Deepak";
            c2.LastName = "Kapoor";
            c2.Limit.AccountOverdue = true;
            c2.Limit.ApprovedAmount = 5000;
            Console.WriteLine("C1.FirstName = {0}, C2.FirstName = {1}", c1.FirstName, c2.FirstName);
            Console.WriteLine("C1.LastName = {0}, C2.LastName = {1}", c1.LastName, c2.LastName);
            Console.WriteLine("C1.Limit.AccountOverdue = {0}, C2.Limit.AccountOverdue = {1}",
                c1.Limit.AccountOverdue, c2.Limit.AccountOverdue);
            Console.WriteLine("C1.Limit.ApprovedAmount = {0}, C2.Limit.ApprovedAmount = {1}",
                c1.Limit.ApprovedAmount, c2.Limit.ApprovedAmount);
            Console.ReadKey();
        }
    }

    \[Serializable\]
    public class Customer : ICloneable
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public CreditLimit Limit { get; set; }

        #region ICloneable Members
        public object Clone()
        {
            object clone;
            using (MemoryStream stream = new MemoryStream())
            {
                BinaryFormatter formatter = new BinaryFormatter();
                // Serialize this object
                formatter.Serialize(stream, this);
                stream.Position = 0;
                // Deserialize to another object
                clone = formatter.Deserialize(stream);
            }
            return clone;
        }
        #endregion
    }

    \[Serializable\]
    public class CreditLimit
    {
        public int ApprovedAmount { get; set; }
        public bool AccountOverdue { get; set; }
    }
```In the code above I have a Customer class which has three properties. In the clone method I use a MemoryStream to serialize and then de-serialize to another object. One of the properties of customer class is called Limit which is of type CreditLimit. I have done this to illustrated deep cloning. As a test I write property values of the original customer class and its clone to console. Note that I modify values for the cloned object. That's all you need to do for cloning. Nice and simple.