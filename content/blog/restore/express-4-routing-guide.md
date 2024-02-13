---
title: 'Express 4 routing guide'
date: Fri, 24 Apr 2015 05:11:29 +0000
draft: false
tags: ['Node.js']
---

Introduction
------------

In this article we will look at routing with Express. Express is the most popular web framework built on node.js. Popularity of Express can be judged by looking at the number of downloads from npm registry which tells us that Express was downloaded more than 2.5 miliion times last month. Other than websites, Express also makes it easy to develop RESTFul services.

What is routing
---------------

Routing is one of the fundamental building blocks for any web framework. It is the mechanism which describes how a particular request will be served. For example when we go to http://kapoor.io we expect the home page to be displayed. There is some code which runs and gets data from a database, it then stiches the markup which is then sent to the client. Or it could simply say "Hello from HTTP" like this```
app.get('/', function(req, res) {
    res.send('Hello from HTTP');
}) 
```The code above will send the string "Hello from HTTP" to the client. But we are getting ahead of ourselves.

Setup
-----

If you'd like to work along with the code in this article then I suggest you create a directory and put some files in it. You will still be able to follow along if you do not do this. The script below will set things up for you```
mkdir route-demo
cd route-demo
touch app.js
touch package.json 
```Open package.json in your favourite text editor and paste this code```
{
    "name": "routing-demo"
} 
```Next run this command to install Express as a dependency `npm install express --save` I also like using colors for colorful console logs, so you may want to install colors `npm install colors --save` Open app.js and paste this code```
var express = require('express');
var colors = require('colors');

var port = process.env.PORT || 8080;

var app = express();

app.get('/', function(req, res) {
  res.send('Hello, How are things today?');
});

app.listen(8080);

console.log(colors.rainbow('Server listening on port: ' + port)); 
```This will give us enough code to start expanding our knowledge of routing in Express.

Diving into routing
-------------------

### Simple routes

In our code above we have used a simple route definition which says that for a HTTP GET request at / send the response as a string "Hello, How are things today?".```
app.get('/', function(req, res) {
  res.send('Hello, How are things today?');
}); 
```We can add more routes for example a HTTP GET request at /morning will produce the response "Good morning".```
app.get('/morning', function(req, res) {
  res.send('Good morning');
}); 
```This way we can create many routes for GET, POST, PUT etc. These routes can also be parameterized. For example we can use a name parameter in our /morning route to display "Good morning, ".```
app.get('/morning/:name/', function(req, res) {
  res.send('Good morning ' + req.params.name);
}); 
```

### Using Router

The approach above will work even for the most complex routing requirements. Express however provides a much cleaner way with express.Router(). Let's look at setting up a basic route with Router.```
var express = require('express');
var colors = require('colors');

var port = process.env.PORT || 8080;

var app = express();

var router = express.Router();

router.get('/', function(req, res) {
  res.send('I feel best at home');
})

app.use('/', router);

app.listen(8080);

console.log(colors.rainbow('Server listening on port: ' + port)); 
```In the code above we are setting up the router to send a response when the home location is accessed. We then tell our app to use this router for all paths `app.use('/', router)` Multiple routes can be setup like this```
var router = express.Router();

router.get('/', function(req, res) {
  res.send('I feel best at home');
})

router.get('/help', function(req, res) {
  res.send('Help me Help you');
})

app.use('/', router); 
```We can also parameterize our routes. This route accepts a name.```
router.get('/city/:name', function(req, res) {
  res.send(req.params.name + ' is the best city');
}) 
```Calling the above route with a parameter will produce the correct response. For example```
$ curl http://localhost:8080/city/Sydney
$ Sydney is the best city 
```

### Route Middleware

Rotues can also include middleware which is code which gets executed before a request is processed. In the example below, the middleware will print a message before any request is served.```
var router = express.Router();

router.use(function(req, res, next) {
  console.log(colors.green('About to process your request' + req.url));
  next();
})

router.get('/', function(req, res) {
  res.send('I feel best at home');
})

router.get('/help', function(req, res) {
  res.send('Help me Help you');
})

router.get('/city/:name', function(req, res) {
  res.send(req.params.name + ' is the best city');
}) 
```Router also has middleware for parameters which can be used to deal with parameters before a request is processed. For example a parameter can be validated by this middleware. In the example below, we can validate a city's name.```
router.use(function(req, res, next) {
  console.log(colors.green('About to process your request' + req.url));
  next();
})

router.param('name', function(req, res, next, name) {
  console.log(colors.blue('Validating city name'));
  next();
})


router.get('/city/:name', function(req, res) {
  res.send(req.params.name + ' is the best city');
})

app.use('/', router); 
```

### Structuring routes

Let's say we are developing a API for customers and pets. We can structure our routes like this```
var customerRouter = express.Router();

customerRouter.get('/', function(req, res) {
  res.send('Get a customer');
})

customerRouter.post('/', function(req, res) {
  res.send('Create a customer');
})

app.use('/customer', customerRouter); 
```Now requests to http://localhost:8080/customer will be handled by cutomerRouter. Similarly requests to http://localhost:8080/pet will be handled by petRouter.```
var petRouter = express.Router();

petRouter.get('/', function(req, res) {
  res.send('Get a pet');
})

petRouter.post('/', function(req, res) {
  res.send('Create a pet');
})

app.use('/pet', petRouter) 
```Here is the full code```
var express = require('express');
var colors = require('colors');

var port = process.env.PORT || 8080;

var app = express();

var customerRouter = express.Router();

customerRouter.get('/', function(req, res) {
  res.send('Get a customer');
})

customerRouter.post('/', function(req, res) {
  res.send('Create a customer');
})

var petRouter = express.Router();

petRouter.get('/', function(req, res) {
  res.send('Get a pet');
})

petRouter.post('/', function(req, res) {
  res.send('Create a pet');
})

app.use('/customer', customerRouter);
app.use('/pet', petRouter)

app.listen(8080);

console.log(colors.rainbow('Server listening on port: ' + port)); 
```This is a much better way to set things up. It is clean and makes understanding code easy.

### Conclusion

Routing is a basic capability a web framework must provide. Express 4 provides this capability with `express.Router()`. It can be uses to write basic routes and parameterized routes. Routes can also be structured in a cleaner way.