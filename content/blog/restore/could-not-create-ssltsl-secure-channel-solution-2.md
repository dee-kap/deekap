---
title: "Could Not Create SSL/TSL Secure Channel Solution"
date: Fri, 20 Aug 2010 01:35:00 +0000
draft: false
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Could Not Create SSL/TLS Secure Channel is an error you my get when communicating with web services in a two way SSL scenario from ASP.NET application. Here is a guide which you can follow to resolve the issue. I spent fair bit of time on this and I am documenting my approach here for future reference. Make sure that you have proper certificates installed in the Local Machine certificate store. Because communication is two way SSL you will also have your private key installed. Because your communication occurs via ASP.NET application this is a permissions issue . Your ASP.NET applications runs under the identity configured in the App Pool.

You must grant permissions to that account under which your application is running to access the private key. Here’s how to do it. Download WinHttpCertCfg tool from this [link](http://www.microsoft.com/downloads/details.aspx?familyid=c42e27ac-3409-40e9-8667-c748e422833f&displaylang=en). Don’t worry about the system requirement on the page. I was able to run the tool successfully on Windows 7.

After installing the tool go to your command prompt and go to the directory where WinHttpCertCfg is installed. On my machine WinHttpCertCfg is installed at C:Program Files (x86)Windows Resource KitsTools. Run WinHttpCertCfg using this command. Substitute “IssuedToName” with the appropriate name for your certificate and same for “AccountName”. If your App Pool runs under NetworkService then that’s the account you’ll put in. **WinHttpCertCfg.exe -g -c LOCAL_MACHINEMY -s "IssuedToName" -a "AccountName"** This should take care of the permission issue and hopefully things will run as expected. In case this doesn’t work then investigate that your certificates are installed in the right store. I know you would have already done this but it doesn’t hurt to have another look. If all else fails then leave a comment and maybe I’ll also learn something new. In any case leave a comment :)
