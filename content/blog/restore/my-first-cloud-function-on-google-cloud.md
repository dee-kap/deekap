---
title: "My first Cloud Function on Google Cloud"
date: Tue, 18 Jun 2019 01:43:36 +0000
draft: true
tags: ["Cloud", "Google"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Similar to AWS Lambda or Azure functions, Google Cloud has Cloud Functions. The idea behind Cloud Functions is to give users a serverless product which can be used for deploying functionality without worrying about servers. Functions can be invoked via HTTP or can be invoked in the background by another Google Cloud product. I decided to have a look and get a simple HTTP Function going.

## What is HTTP Function?

There are two types of functions in Google Cloud. Background functions and HTTP functions. Background functions are invoked by other Google Cloud services and HTTP functions can be invoked simply by making  HTTP request. I created a new Google Cloud Account and downloaded and installed [Cloud SDK](https://cloud.google.com/sdk/) on my mac. To get things going I decided to write a simple function which returns a string. In true developer style, I called it hello-world. I created a hello-world directory. Inside the directory, I created index.js which has the code for my function. Here are the contents of index.js```
exports.helloWorld = (request, response) => {
response.status(200).send("Hello World!);
};

````Not much happening here, other than the function returning string "Hello World"

Deployment
----------

Deploying the function was easy. This command did the job```
gcloud functions deploy helloWorld --trigger-http --runtime=nodejs10
```Let's break it down to understand the command.

1.  **gcloud** is the CLI tool you get when you install Google Cloud SDK
2.  **functions**: Cloud product which in this case is functions
3.  **helloWorld**: name of the function to be deployed
4.  **\--trigger-http**: function I am deploying will be invoked by HTTP
5.  **\--runtime=nodejs10**: The runtime for this function. Can be Python, Go or node

Running the command deploys the function. I can also go to the console and see the function I just created. ![](https://bitofbinary.com/wp-content/uploads/2018/06/google-function-hello-world.png) This was not hard at all. Invoking the function returns the string "Hello World!". The function can be invoked by clicking on the URL in the Trigger tab, or by issuing a simple cURL command. We have liftoff!
````
