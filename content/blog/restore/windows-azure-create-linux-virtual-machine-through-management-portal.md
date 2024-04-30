---
title: "Windows Azure - Create Linux Virtual Machine Through Management Portal"
date: Thu, 30 May 2013 03:16:00 +0000
draft: false
tags: ["Azure", "Cloud"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Windows Azure along with PaaS is also a full on IaaS cloud service. At the time of this writing you can create a variety of Windows VMs and Linux VMs. This post shows you how easy it is to create a Linux virtual machine on Windows Azure.  
Step 1  
Login to the [management portal](https://manage.windowsazure.com/)

[![image](http://kapoor.io/wp-content/uploads/2013/05/image_thumb-300x161.png "image")](http://kapoor.io/wp-content/uploads/2013/05/image_thumb.png)

Step 2  
Go to Virtual Machines  
[![image](http://kapoor.io/wp-content/uploads/2013/05/image_thumb1-300x160.png "image")](http://kapoor.io/wp-content/uploads/2013/05/image_thumb1.png)

Step  3  
Click on CREATE A VIRTUAL MACHINE  
You are presented with a form where you can fill in the details. For IMAGE select Ubuntu Server 13.04 or any other version if you like.

[![image](http://kapoor.io/wp-content/uploads/2013/05/image_thumb2-300x150.png "image")](http://kapoor.io/wp-content/uploads/2013/05/image_thumb2.png)

After clicking on CREATE A VIRTUAL MACHINE below the form, you will see your machine being provisioned.

[![image](http://kapoor.io/wp-content/uploads/2013/05/image_thumb3-300x162.png "image")](http://kapoor.io/wp-content/uploads/2013/05/image_thumb3.png)

In about 2-3 minutes the machine will be provisioned and the status will change to starting.

[![image](http://kapoor.io/wp-content/uploads/2013/05/image_thumb4-300x88.png "image")](http://kapoor.io/wp-content/uploads/2013/05/image_thumb4.png)

Once you see the status to say Running, you can click on the name of your virtual machine which will bring you to this page.

[![image](http://kapoor.io/wp-content/uploads/2013/05/image_thumb5-300x210.png "image")](http://kapoor.io/wp-content/uploads/2013/05/image_thumb5.png)

Congratulations. You now have a Linux virtual machine running on Windows Azure.
