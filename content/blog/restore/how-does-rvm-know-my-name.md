---
title: "How does RVM know my name?"
date: Fri, 30 May 2014 06:20:00 +0000
draft: false
tags: ["Ruby"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Today while installing RVM on my newly minted Kali VM, I found something which caught my attention. After running `curl -ssl https://get.rvm.io | bash -s stable --ruby` I saw after few lines this

![Screen Shot 2014 05 30 at 2 23 29 pm](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-30-at-2.23.29-pm.png "Screen Shot 2014-05-30 at 2.23.29 pm.png")

It knows who I am. And I am installing RVM in a VM on which I don't have anything which can identify me as Deepak Kapoor. So how does RVM know my name. A mystery which I thought must be solved.

First thing I did was cloned the git repository for RVM which can be found at https://github.com/wayneeseguin/rvm.

After that it was simply opening the folder in git and using ack to grok the code.

It turns out that there is a function in scripts/function/installer which displays the "Thank you message". Below is the code for the discovered function.

```
display\_thank\_you()
{
  typeset name=""
  if builtin command -v git > /dev/null 2>&1
  then name="$(git config user.name 2>/dev/null )"
  fi
  : ${name:=${SUDO\_USER:-}}
  : ${name:=${USERNAME:-}}
  : ${name:=${USER:-}}
  : ${name:=$(id | \_\_rvm\_sed -e 's/^\[^(\]\*(//' -e 's/).\*$//')}
  case "${name}" in
    (root) name="Administrator" ;;
    ("")   name="User"          ;;
  esac

  rvm\_out "
\# ${name},
#
\#   Thank you for using RVM!
\#   We sincerely hope that RVM helps to make your life easier and more enjoyable!!!
#
\# ~Wayne, Michal & team.
"
}

```

It can be seen that in the third line of this function it is reading my name from gitconfig. So it turns out that my initial hypothesis of the machine not having anything to identify turned out to be wrong. Mystery solved.
