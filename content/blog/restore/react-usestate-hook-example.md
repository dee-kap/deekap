---
title: "React useState Hook Example"
date: Wed, 24 Jul 2019 03:21:37 +0000
draft: false
tags: ["React"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

React hooks are a great way to work with many React features without writing classes. I think classes have no place in JavaScript, but that is a topic for another post. In this post, I'd like to show you how to use the **useState** hook to build a simple tabs component. In our component, we will use the state to keep track of the active tab. If you have worked with React and state, you would have done it using classes. We will not use a class but instead, our component will be purely functional. Our component implements features of a simple tab control. When a user clicks on a tab item, it is expected that the clicked item will be visually highlighted. This is what it will look like.

![](https://deekap.com/wp-content/uploads/2019/07/usestate-tabs.gif)

The first thing we need to do within our component is to call **useState** method like this.

```javascript
const [activeTab, setActiveTab] = React.useState("fruits");
```

This line needs an explanation. What we are looking at here is an elegant use of [array destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Array_destructuring). We are executing the **useState** function which is part of React. The function returns us an array of two items. The first one holds our state variable which we are calling activeTab. The second is a function which we will use to update this state. Another thing to notice is that we are passing an argument to the **useState** function. This is our initial state. It can be an object, an array or anything we like. In this example, it happens to be a string. We are telling React to create a state variable and call it activeTab and tell it the function you will use to change the state. **activeTab** is the variable which will store the state and **setActiveTab** will be used to change it. Another important bit is that when using the useState hook, we give it the initial state. In this case, it is the string _fruits_. What we are saying is that for this component the initial state value for activeTab will be _fruits._ Next, we use the state in our render function to render a list of tab items

```jsx
<ul>
  <li
    onClick={() => setActiveTab("fruits")}
    className={activeTab === "fruits" ? "active" : ""}
  >
    Fruits
  </li>
  <li
    onClick={() => setActiveTab("vegetables")}
    className={activeTab === "vegetables" ? "active" : ""}
  >
    Vegetables
  </li>
  <li
    onClick={() => setActiveTab("junk")}
    className={activeTab === "junk" ? "active" : ""}
  >
    Junk
  </li>
</ul>
```

The **onClick** on the list handler calls the **setActiveTab** to change the state to whichever tab is clicked. We also use the **activeTab** state variable to assign the active CSS class on the item. This is to give it the visual appearance of a selected tab. There is some repetition here which I don't like, the code can be simplified to look less DRY

```jsx
<ul>
  {TabItem("fruits", "Fruits")}
  {TabItem("vegetables", "Vegetables")}
  {TabItem("junk", "Junk")}
</ul>
```

The **TabItem function** will return us the list item as we want

```javascript
function TabItem(tab, label) {
  return (
    <li
      onClick={() => setActiveTab(tab)}
      className={activeTab === tab ? "active" : ""}
    >
      {label}
    </li>
  );
}
```

Here is the full code for the component

```jsx
import React from "react";
import ReactDOM from "react-dom";

import "./styles.css";

function App() {
  const [activeTab, setActiveTab] = React.useState("fruits");

  function TabItem(tab, label) {
    return (
      <li
        onClick={() => setActiveTab(tab)}
        className={activeTab === tab ? "active" : ""}
      >
        {label}
      </li>
    );
  }

  return (
    <div className="App">
      <ul>
        {TabItem("fruits", "Fruits")}
        {TabItem("vegetables", "Vegetables")}
        {TabItem("junk", "Junk")}
      </ul>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
```

This is the CSS used

```css
.App {
  font-family: sans-serif;
}

ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  justify-content: center;
  border-bottom: 2px solid rgb(0, 104, 22);
}

li {
  padding: 1rem;
  font-size: 120%;
  color: rgb(78, 77, 77);
  cursor: pointer;
}

.active {
  font-weight: bold;
  border-top: 2px solid rgb(0, 104, 22);
  border-left: 2px solid rgb(0, 104, 22);
  border-right: 2px solid rgb(0, 104, 22);
}
```

We can see that by using **useState** hook, we have eliminated the need to write a class when working with the state in React. The code looks much cleaner and a little bit more JavaScript-y Happy coding.
