---
title: "AWS - SDK for Ruby Unable to find AWS credentials"
date: Wed, 02 Jul 2014 01:44:00 +0000
draft: false
tags: ["Cloud"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Today while working with AWS SDK for Ruby I came across this error

> (AWS::Errors::MissingCredentialsError) Missing Credentials.

AWS SDK will go through different ways to get credentials. One of them is to look at environment variables and the other is to look for credentials file in .aws directory. While setting up AWS CLI on my machine I ran `aws configure` command which created .aws/config file. So what's with this credentials file?

It turns out that config is the legacy location to store credentials. All I need to do is create a symlink to the new location.

```

`
cd ~/.aws && ln -s config credentials
`

```

I do not get the Missing Credentials error anymore. What I have talked about here is also discussed in [docs by Amazon](http://docs.aws.amazon.com/AWSSdkDocsRuby/latest/DeveloperGuide/ruby-dg-setup.html).
