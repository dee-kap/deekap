---
title: "node.js EventEmitter example"
date: Tue, 05 May 2015 02:59:02 +0000
draft: false
tags: ["Node.js"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

## What is it?

Node.js comes with a core module called `events`. And EventEmitter is a class on the events object. EventEmitter has stability of 4 which means that API is frozen. In other words things in **events** are unlikely to change.

## What does it do?

EventEmitter is used to either raise or listen to events. Think of a typical User Interface in which a user clicks on a button and something happens. In events paralance we can say that the button rasies a click event and there is some code somewhere listening to this event and does what it has to do. Events are also useful on server side. For example we could write a library which reads a file and then raises an event which notifies the listener that file read operation is finished. The code which raises the event can also pass in the results to whoever is listening for the event. The results can be an error or contents of file which was read.

## How can I use it?

Let's build a example which gets a URL. It raises or to be more specific it emits an event if GET operation was successful or a failure.

```javascript
var EventEmitter = require("events").EventEmitter;
var emitter = new EventEmitter();
var http = require("http");

emitter.on("get_page", function (url) {
  http
    .get(url, function (res) {
      emitter.emit("page_get_successful");
    })
    .on("error", function () {
      emitter.emit("page_get_fail");
    });
});

emitter.on("page_get_successful", function (data) {
  console.log("page get was succesful");
});

emitter.on("page_get_fail", function () {
  console.log("page get failed");
});

emitter.emit("get_page", "http://bitofbinary.com");
```

In the code above look at the last line

```javascript
emitter.emit("get_page", "http://bitofbinary.com");
```

here we emit an event called **get_page**. We have a listener for this event in `emitter.on('get_page')`. When the event **get_page** is raised the listener gets into action and uses `http` module to fetch the URL for us. If the action is successful then an event is emitted **page_get_successful**. This is handled by the listener `page_get_successful`. Similarly if there was an error fetching the URL an event **page_get_fail** will be raised. This can be tested by fudging the URL passed in to **get_page** event like this `emitter.emit('get_page', 'http://bitofbinary.blah');`

EvenEmitter is heavily used in node.js by other modules. This can be seen in our example where we are listening to **error** event raised by http module.

```javascript
http
  .get(url, function (res) {
    emitter.emit("page_get_successful");
  })
  .on("error", function () {
    emitter.emit("page_get_fail");
  });
```

## Beyond basics

EventEmitter is packed with more methods than just simply raising and listening to events. For example if we want a listener to be invoked only once we can use `.once()` method of EventEmitter. Multiple listeners can also be attached to an event and they can all be removed by calling `.removeAllListener()` method.
