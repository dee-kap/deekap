---
title: "Personal project for learning GitHub API"
date: Wed, 13 Aug 2014 02:11:00 +0000
draft: true
tags: ["Uncategorized"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Couple of weeks ago on a rainy weekend I started hacking on a project to learn GitHub API. I decided to use AngularJS to interact with the API and within few hours it started to take some shape. I write a lot of throw away code which gets safely tucked in a temp directory but this I thought was a bit special. So I thought I will write a bit about it. Here it goes.

I plan to refactor the code significantly as I make progress on this project. The [repository](https://github.com/deepak-kapoor/ng-git) for this project is on [GitHub](https://github.com/deepak-kapoor/ng-git) for the world to see. Before I get into what I did, I will show you a screenshot of the running application. ![Screen Shot 2014 08 13 at 11 13 01 am](http://kapoor.io/wp-content/uploads/2014/08/Screen-252520Shot-2525202014-08-13-252520at-25252011.13.01-252520am-300x284.png "Screen Shot 2014-08-13 at 11.13.01 am.png") What you see here is repositories of Mozilla on Github. Elements on the page will become more clear as you read this post further. If you wish to run the application on your machine then clone the [repository](https://github.com/deepak-kapoor/ng-git), go to the location where you cloned it and run `grunt serve`. You will need to have grunt-cli installed on your machine. Now I will talk a bit about how I built this application. To get going I used the awesome [Yo](http://yeoman.io/) scaffolding tool to generate an AngularJS app. [Yo](http://yeoman.io/) combined with [Grunt](http://gruntjs.com/) and [Bower](http://bower.io/) is a must have toolset for web developers. I highly recommend that you look into these tools. Once I had the application generated, I simply ran `grunt server` to run the application. Because I have other apps running on port 9000, I made a change to my Gruntfile.js to run my application on port 9001.```

`
connect: {  
      options: {  
        port: 9001,  
        // Change this to '0.0.0.0' to access the server from outside.  
        hostname: 'localhost',  
        livereload: 35728  
      }, `

````Yo generates a basic AngularJS app which displays the famous Alo Alo page when you run it for the first time. As I picked bootstrap while generating the app, I decided to look for a nice theme for my application. I found one called [Slate](http://bootswatch.com/slate/) at Bootswatch. I am a fan of dark themes and this one looked pretty good to me.

As you saw earlier in the screenshot of the main page, I am displaying information about repositories in rectangular containers I called tiles. Here is an example of a tile.

![Screen Shot 2014 08 13 at 11 42 53 am](http://kapoor.io/wp-content/uploads/2014/08/Screen-252520Shot-2525202014-08-13-252520at-25252011.42.53-252520am.png "Screen Shot 2014-08-13 at 11.42.53 am.png") You can see that it shows the name of the repository, number of stars, number of forks and some other information like when the repository was created, updated and published. This application talks to GitHub API and whenever I talk to an external service I like to create a AngularJS service as a wrapper. For that I created githubService.js which exposes two methods `LoadRepoTilesByName` and `LoadRepoTilesByUrl`. **LoadRepoTilesByName** takes in the GitHub user name and a sort to be applied. This then calls **LoadRepoTilesByUrl** and returns a promise. You will see that the url adds two query string parameters **per\_page** which is used to limit the number of objects returned by GitHub and the **sort** which can be name, created date or updated date. Let's look at how I use this service. Top part of the page where you see an input box and Search button is implemented as a directive. This is simple directive which packs in a lot of punch. The view part is a form which contains the input box and the button.```

`
<form class="navbar-form navbar-left" role="search">
  <div class="form-group">
    <input type="text" class="form-control" placeholder="Search" ng-model="username">
  </div>
  <button class="btn btn-default" ng-click="search()">Search</button>
</form>
`

```The controller for this directive implements two functions to get data from GitHub.```

`
$scope.loadTiles = function (sort) {
  githubService.LoadRepoTilesByName($scope.username, sort)
    .then(function (data) {
      $scope.reposData = data;
      $scope.reposFound = data.repos.length > 0;
      configurePreviousNext();
      $scope.currentSort = sort;
      console.log(data.repos);
    }, function (error) {
      console.log(error);
    });

}

$scope.search = function () {
  $http.get('https://api.github.com/users/' + $scope.username)
    .success(function (data) {
      $scope.user = data;
      $scope.loaded = true;
    })
    .error(function () {
      $scope.userNotFound = true;

    })

  $scope.loadTiles($scope.currentSort);

};
`

```Other functions in searchForm directive configure previous and **next** links. I will talk a bit more these links in a minute. **LoadTilesNext** and **LoadTilesPrevious** load the next or previous set of tiles. Now a bit about these next and previous links. In my githubService I have a function called **getPagerLinks**. This function returns the links used for pagination. I had to grok the API a bit to understand how these works. GitHub has provided excellent documentation here at [Traversing with Pagination](https://developer.github.com/guides/traversing-with-pagination/). Basically these links are returned in HTTP headers. Tiles themselves are implemented as a directive. I like to keep my code structured this way so that it is easy to modify and test without breaking a lot of things. I think I will stop here and get back to writing some more code. This little hack has become a rather interesting project to which I plan to devote some of my free time. There is a lot to be done to get it to an agreeable state. I will keep posting as I make progress.
````
