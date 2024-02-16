---
title: "Playing with Microsoft Azure CLI on mac"
date: Tue, 20 May 2014 04:31:00 +0000
draft: true
tags: ["Cloud"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

I've been a user of Azure for sometime now and I have always worked through the web based management portal. The portal has served me well but today I am in mood for command line. I will install the CLI for Azure and play with it.

BTW: CLI stands for Command Line Interface. I know that you know what CLI stands for. For the record, I'm not trying to be a smart-ass. Rest of the post is off record.

Installing Azure CLI on Mac could not be any easier. Steps required are to download the dmg file and open it. Click on the icon to install the beauty.

![Screen Shot 2014 05 20 at 12 54 58 pm](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-20-at-12.54.58-pm.png "Screen Shot 2014-05-20 at 12.54.58 pm.png")

After installation, I run `azure` command on terminal and I am greeted by this sexy ASCII art.

![Screen Shot 2014 05 20 at 1 11 40 pm](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-20-at-1.11.40-pm.png "Screen Shot 2014-05-20 at 1.11.40 pm.png")

All good so far. Next thing I want to do is log into my account. For this I run `azure login` which prompts me for username and password. A message is displayed right after I enter correct credentials.

> If you choose to continue, Azure command-line interface will cache your authentication information. Note that this sensitive information will be stored in plain text on the file system of your computer at /Users/deepak/.azure/azureProfile.json. Ensure that you take suitable precautions to protect your computer from unauthorized access in order minimize the risk of that information being disclosed.  
> Do you wish to continue: (y/n)

I guess I can live with this for now so I will say yes. I am sure there is a better way than this but let's not worry about it for now.

What happens next is that I get an authentication error.

![Screen Shot 2014 05 20 at 1 18 50 pm](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-20-at-1.18.50-pm.png "Screen Shot 2014-05-20 at 1.18.50 pm.png")

From experience I know that most of the time I get an error is because I have done something wrong. Luckily the error tells me that I should look in azure.err file to see what went wrong. Let's do that.

```
Tue May 20 2014 13:17:07 GMT+1000 (EST):
{ \[Error: Server returned an unknown AccountType: undefined\]
  stack: \[Getter/Setter\],
  \_\_frame:
   { name: '\_\_7',
     line: 171,
     file: '/usr/local/azure/lib/commands/account.js',
     prev: undefined,
     active: false,
     offset: 35,
     col: 31 },
  rawStack: \[Getter\] }
Error: Server returned an unknown AccountType: undefined
    at Logger.createError (/usr/local/azure/node\_modules/adal-node/lib/log.js:196:13)
    at /usr/local/azure/node\_modules/adal-node/lib/token-request.js:366:35
    at UserRealm.\_parseDiscoveryResponse (/usr/local/azure/node\_modules/adal-node/lib/user-realm.js:234:3)
    at /usr/local/azure/node\_modules/adal-node/lib/user-realm.js:263:12
    at Request.\_callback (/usr/local/azure/node\_modules/adal-node/lib/util.js:116:5)
    at Request.self.callback (/usr/local/azure/node\_modules/adal-node/node\_modules/request/request.js:121:22)
    at Request.EventEmitter.emit (events.js:98:17)
    at Request. (/usr/local/azure/node\_modules/adal-node/node\_modules/request/request.js:978:14)
    at Request.EventEmitter.emit (events.js:117:20)
    at IncomingMessage. (/usr/local/azure/node\_modules/adal-node/node\_modules/request/request.js:929:12)
    at \_\_7 (/usr/local/azure/lib/commands/account.js:206:31)
```

Okay, so you will not tell me if I entered an incorrect username/password combination. You are just going to be an pain and say that AccountType is undefined. I have no idea what that means so the only option I have is to turn to Google. But hold on, I see that there is some information in the stack. I should look at /usr/local/azure/lib/command/account.js line 171 you say? Okay okay I will.

So Mr. Smarty-pants error that file account.js is minified by some half-baked minified. But I see your point. You are not giving me a fish but you are trying to teach me to fish. In /usr/local/azure/lib/commands/ directory I see that there is a account.\_js. That's where I should be looking, right? Okay, let's do that. I will search for the error text which is "Server returned an unknown AccountType: undefined". What? No match found! Okay I guess I should go with my initial instinct and Google it out. Thank you for zero fishes.

The first search results link points to a StackOverflow question which tells me that azure login method will only work with organisational account. I should use a .publishsettings file. Yes yes I know that you are thinking RTFM. I will do it now.

The doco says that I have to download a .publishsettings file and I can do that by executing `azure account download` command which will open a link in my default browser. And it does not lie. I am now in my management portal and the file is downloaded.

The .publishsettings file contains an encoded management certificate so it has to be kept secure. Point taken. Secure it shall be.

As per the documentation I need to run a `azure account import` command and pass it the path to my .publishsettings file. Let's do it.

I am happy to report no errors.

![Screen Shot 2014 05 20 at 1 39 06 pm](http://sydlog.io/wp-content/uploads/2014/05/Screen-Shot-2014-05-20-at-1.39.06-pm.png "Screen Shot 2014-05-20 at 1.39.06 pm.png")

What do I do to login now? It turns out that I don't need to login anymore. I can run commands and the authentication part will be taken care by the certificate I downloaded. As per the documentation I should also delete the .publishsettings file because when I ran `azure account import` a directory named .azure was created in my home which has a json file required to interact with Azure.

This makes me happy. Let's see if I can view subscription I have. Running the command `azure account list` shows me name, id and status of my subscription(s).

So far good.

I have a couple of websites and a couple of VMs running on azure. I will now try to get some information about them. The websites first.

Before I get into that, I must say that CLI for Azure is simple. There is a manageable number of commands which are organised in sensible topic, verb, options pattern. The image below taken from [here](http://blogs.msdn.com/b/interoperability/archive/2012/06/07/windows-azure-command-line-tool-for-mac-and-linux.aspx) explains what I mean.

![5633 SyntaxDiagram png 550x0](http://sydlog.io/wp-content/uploads/2014/05/5633.SyntaxDiagram.png-550x0.png "5633.SyntaxDiagram.png-550x0.png")

So getting back to my website. Following the simple (and it is a good thing) structure of azure commands I should be executing `azure site list`. And it works. How freaking awesome is that? The output is:

```
Name              Slot  Status   Location  Mode    URL
\----------------  ----  -------  --------  ------  -------------------------------------------------------
deepak-node             Running  West US   Free    deepak-node.azurewebsites.net
deepakkapoorblog        Running  West US   Shared  www.deepakkapoor.net,deepakkapoorblog.azurewebsites.net
```

Okay, I'm excited. Let's see if I can get some more information for my second site. I run `azure site show deepakkapoorblog`. Wheels turn for a second or so and then I am presented with some basic information about my site.

I will now turn to the VMs.

Starting with `azure vm list` I see that I have 3 VMs. It is also handy to see that two of them are not running.

```
Name       Status              Location  DNS Name
\---------  ------------------  --------  ----------------------------
uswin      StoppedDeallocated  East US   uswin.cloudapp.net
meanimage  StoppedDeallocated  West US   meanimage.cloudapp.net
nodeland   ReadyRole           East US   deepak-nodeland.cloudapp.net
```

I will be a bit naughty and shutdown a VM. I will shutdown nodeland with this command `azure vm shutdown nodeland`. Again the wheels turn and I get all OK back from Azure. Let's see if it really did shutdown with the `azure vm list` command. Yes it did.

```
Name       Status              Location  DNS Name
\---------  ------------------  --------  ----------------------------
nodeland   StoppedDeallocated  East US   deepak-nodeland.cloudapp.net
uswin      StoppedDeallocated  East US   uswin.cloudapp.net
meanimage  StoppedDeallocated  West US   meanimage.cloudapp.net
```

It looks like pretty much anything can be automated in Azure through scripts and I would like to explore it more by reading documentation. I am sure that there are people out there who already know how to do all Azurey things with CLI and I may turn to them to learn more. In the meantime I am enjoying learning by trial and error.
