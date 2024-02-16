---
title: "Code Sample: Programmatically Download File Using C#"
date: Wed, 17 Sep 2008 01:26:00 +0000
draft: true
tags: [".NET"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

While browsing forums today I came across a question which asked for a solution to download a file from a web server programmatically. The solution is very simple and below is the code which achieves the goal. Here I am downloading a file asynchronously on Button Click.```

private void buttonDownloadFile_Click(object sender, EventArgs e)  
{  
 string url  
 = @"https://googledrive.com/host/0B6PDO8HPEQZNZWpTRms0ZWtlaUU/uploads/2008/08/image35.png";

        // Create an instance of WebClient
        WebClient client = new WebClient();

        // Hookup DownloadFileCompleted Event
        client.DownloadFileCompleted +=
        new AsyncCompletedEventHandler(client\_DownloadFileCompleted);

        // Start the download and copy the file to c:temp
        client.DownloadFileAsync(new Uri(url), @"c:tempimage35.png");

}

void client_DownloadFileCompleted(object sender, AsyncCompletedEventArgs e)  
 {  
 MessageBox.Show("File downloaded");  
 }

```You can also download the file synchronously using WebClient.DownloadFile() method.

```
