---
title: "AWS - Getting Started with CLI"
date: Tue, 01 Jul 2014 00:42:00 +0000
draft: false
tags: ["Cloud", "AWS"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Today I created a new Amazon AWS account with the goal of learning this beast inside out. Over next few and hopefully many days I plan to write more about AWS. I am doing this for learning and not teaching. I will write these posts as I would write notes when learning a new technology. Come along if you wish and enjoy the ride.

Account creation and verification process went without a hitch and the first thing I wanted to do was to access my account information from terminal. This post is mostly about that.

To install CLI run these commands

```
$ wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip
$ unzip awscli-bundle.zip
$ sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
```

Now that CLI is installed, it needs to be configured. Configuring CLI can be done by running `aws configure` command. There are four pieces of information I need to configure the CLI. These are AWS Access key, AWS Secret Access key, default region and default output format. The last one which is the output format is optional. If I do not supply a value then it defaults to json.

AWS recommends that I should create an IAM user as this is considered a best practice. When I access the credentials section of management console, I am presented with an info box which says that I should create an IAM user. For now I will go ahead and create a new access key. I will at some later point come back and understand how IAM works.

![Screen Shot 2014 07 01 at 10 56 32 am]()

After clicking Create New Access Key button, a popup appears which says that I should download my key file. This is the last chance I have to download the file. I better do this.

![Screen Shot 2014 07 01 at 11 00 25 am]()

After downloading my key file, I go back to the terminal and fire up `aws configure`. First thing it asks me is the access key, after that it prompts me to enter secret access key and then the default region.

I know that Sydney which is my hometown is one of the regions available to me. I will enter **ap-southeast-2** which is Sydney.

I will leave the output format blank so that it works with json which is the default output format.

Configuring the CLI by `aws configure` created a **.aws** directory in my home. Within this directory it created a file called config. This config file contains the values I entered.

AWS CLI is now all configured and ready to go.

As part of my learning, I will try to accomplish most tasks from either the command line or programmatically using Ruby.

I will retrieve a list of ec2 instances I am running. I do not have any instances but I just want to see if things are working as expected.

When I run `aws ec2 describe-instances` I see the following output which I will take it as saying that I do not have any instances.

```json
{
  "Reservations": []
}
```

Day 1 looks good. I was able to create an account, install and configure the command line interface and run a command successfully. Looking forward to day 2 when I will work with S3 storage.
