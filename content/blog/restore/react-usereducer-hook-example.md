---
title: "React useReducer Hook Example"
date: Fri, 02 Aug 2019 01:30:35 +0000
draft: false
tags: ["React"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

In this post, we will look at **useReducer** hook in React. useReducer is not too different from **useState** hook which I wrote about in an [earlier post](/react-usestate-hook-example/). useReducer similar to useState provides a mechanism to work with state in React functional components. It does give us something which useState does not. And that is the dispatch functionality. Being a heavy user of Redux, I like the dispatch pattern and I was happy to see useReducer working with it. Let's look at an example in which we will write a simple tab component. We will keep track of the active tab in component state. The behaviour will be something like this. ![](https://bitofbinary.com/wp-content/uploads/2019/07/usestate-tabs.gif) To begin with, there is an initial state which looks like this

````javascript
const initialState = [
  {
    name: "fruits",
    label: "Fruits",
    active: true
  },
  {
    name: "vegetables",
    label: "Vegetables",
    active: false
  },
  {
    name: "junk",
    label: "Junk",
    active: false
  }
]; `The initial state is an array of tab items where each item has a name, label (used for the text of tab item), and an active state which we use to display the active tab. Within our component first call is made to **React.useReducer** function which returns us two things. **First** is the **state** and the **second** is a **dispatch** function. We will use this dispatch to trigger an action which will call our reducer to modify the state. Can you see some similarity here with Redux? Don't worry if you have not worked with Redux. You are not missing on anything.`const [state, dispatch] = React.useReducer(reducer, initialState); `Another thing to note is that when we call the useReducer function we pass two parameters. A reducer and initial state. The reducer here is a function which will do the actual work of making a tab item active. Here is the reducer function`const reducer = (state, action) => {
  if (action.type === "ACTIVATE_TAB") {
    return state.map(item => {
      item.active = item.name === action.payload;
      return item;
    });
  }
  return state;
}; `Here if our **action.type** matches the string "ACTIVE_TAB" we make the tab active (the one which was supplied in **action.payload**). Finally, we return the state. Below is the full code for our component```
import React from "react";
import ReactDOM from "react-dom";

import "./styles.css";

const initialState = [
{
name: "fruits",
label: "Fruits",
active: true
},
{
name: "vegetables",
label: "Vegetables",
active: false
},
{
name: "junk",
label: "Junk",
active: false
}
];

const reducer = (state, action) => {
if (action.type === "ACTIVATE_TAB") {
return state.map(item => {
item.active = item.name === action.payload;
return item;
});
}
return state;
};

const App = () => {
const [state, dispatch] = React.useReducer(reducer, initialState);

const TabItems = state.map(item => {
return (
<li
onClick={() => dispatch({ type: "ACTIVATE_TAB", payload: item.name })}
className={item.active ? "active" : ""} >
{item.label}
</li>
);
});

return (
<div className="App">
<ul>{TabItems}</ul>
</div>
);
};

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
`And the css`
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

```While working with state, I often end up using useReducer hook. I think the dispatch pattern makes the code cleaner. Happy coding.

````
