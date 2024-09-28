---
title: "Teaching Ruby One Post at a Time"
date: 2024-02-06
featured_image: "ruby.png"
tags: ["Ruby"]
draft: true
---

Lately, I have been talking a lot about Ruby on Rails and how it is one of the best frameworks for developing web applications with junior developers I'm mentoring these days.

I have seen some great interest from them and a desire to learn Ruby and then Ruby on Rails. I often show them a snippet of code or demonstrate how a particular problem can be solved in Ruby. This is now happening on almost daily basis and it has motivated me to creates these posts in which I will write about how something can be done using Ruby.

There is no structure to these. The posts are based on whatever comes to my mind or questions I was asked.

So in the tradition of learning a programming language, I will start with printing hello world on the screen.

There are two ways to print something on the screen.

The first one is

```ruby
print "Hello World!"
```

output in IRB

```bash
Hello World!=> nil
```

And the second way is

```ruby
puts "Hello World!"
```

output in IRB

```bash
Hello World!
=> nil
```

So what is the difference?

**puts** which is short for put string **will add a newline** after the output.

If we were printing an array then each element will printed on a new line

```ruby
puts ["a", "b", "c"]
```

```bash
a
b
c
=> nil
```

**print** will **not add a newline** and in the case of an array, it will be printed as a single string

```ruby
print ["a", "b", "c"]
```

```bash
["a", "b", "c"]=> nil
```

You can also join me on my [Discord Server](https://discord.gg/QXWg4VvK) to ask me questions about Ruby or engage in programming related chit-chat.

#13
