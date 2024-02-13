---
title: "Test REST APIs with Frisby"
date: Fri, 17 Apr 2015 00:22:02 +0000
draft: false
tags: ["Node.js"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

## Introduction

As software developers we strive for exellence in our craft. This means writing software we and our clients are proud of. One way to ensure such exellence is to test everything. Even better is to write tests which can test our code for us commonly known as unit tests or end-to-end tests. I prefer the term automated tests. This article is about automated testing of REST APIs with Frisby. [Frisby](http://frisbyjs.com/) is a node.js package created by [Vance Lucas](http://vancelucas.com/).

> Frisby is a REST API testing framework built on node.js and Jasmine that makes testing API endpoints easy, fast, and fun

I will use some examples to demonstrate how tests can be created with Frisby. You will gain most from this article if you are already convinced on the benefits of automated testing and have some knowledge of [Jasmine](http://jasmine.github.io/) or any other JavaScript based testing library.

## Installing Frisby

Frisby is a node.js package so node.js must be installed. Node.js installer can be downloaded from [nodejs.org](https://nodejs.org/). Once node.js running, Frisby can be installed with npm. This is how most node.js packages are installed. The command to install Frisby is```
npm install -g frisby

````

Creating tests
--------------

I will use jsontest.com as an example API. Ideally I would be testing my own API. All frisby tests start with `var frisby = require('frisby')` The variable name can be anything but convention is to name the variable same as the package name which in this case is frisby. Tests script are conventionally names something\_spec.js or something-spec.js. For this article I can name my script jsontest-spec.js

Anatomy of a Frisby test
------------------------

Frisby tests start by calling `frisby.create()` method with a sensible description passed in. Next we specify the verb we are testing. For example if we are testing HTTP GET then the code will be```
frisby.create('Ensure that what I expect happens')
.get('http://api.killerapp.com/user/1')
```We can then test the expected status```
frisby.create('Ensure that what I expect happens')
.get('http://api.killerapp.com/user/1')
.exptectStatus(200)
```Other expectation can be also be chained. A list of expectations are:

1.  expectStatus
2.  expectHeader
3.  expectHeaderContains
4.  expectJSON
5.  expectJSONTypes
6.  expectJSONLength
7.  expectBodyContains

### toss

In order to conclude the test `toss()` method should be added at the end of chain.```
frisby.create('Ensure that what I expect happens')
.get('http://api.killerapp.com/user/1')
.exptectStatus(200)
.toss():
````

## Example tests

This example shows a test I would write to test a service which returns my IP address. I am using API jsontest.com as my test candidate.`var frisby = require('frisby')
.get('http://ip.jsontest.com/')
.expectStatus(200)
.expectJSONTypes({ 'ip': String })
.toss(); `This test also verifies that right content-type header is returned by the API. Again as an example I am using http://ip.jsontest.com/?mime=4 as my end-point. This url returns the content-type as text/html. More example for jsontest can be found at http://www.jsontest.com/```
var frisby = require('frisby');

frisby.create('Ensure that IP address is returned')
.get('http://ip.jsontest.com/?mime=4')
.expectStatus(200)
.expectHeaderContains('Content-Type', 'text/html')
.expectJSONTypes({ 'ip': String })
.toss();

```

Running tests
-------------

Frisby uses jasmine-node to run tests. jasmine-node can be installed by running `npm install -g jasmine-node`. Once installed tests can be run by executing `jasmine-node` jasmine-node can be run with many options such as verbose output, use junitreport etc. These options can be found by running `jasmine-node --help`.

Conclusion
----------

I hope this article gave you enough introduction to Frisby. I like the clean strucuture of Frisby tests. I find them to be easily readable and easy to write. Drop me a line if you have any questions. I am availabe on Twitter [@\_DeepakKapoor](https://twitter.com/_DeepakKapoor), or connect with me on [LinkedIn](http://au.linkedin.com/in/kapoordeepak).
```
