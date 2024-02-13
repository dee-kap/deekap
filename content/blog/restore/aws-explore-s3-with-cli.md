---
title: "AWS - Explore S3 with CLI"
date: Tue, 01 Jul 2014 05:47:00 +0000
draft: false
tags: ["Cloud"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Today I feel like getting myself into one of the basic but very powerful storage service offered by Amazon called S3. S3 is a storage service which can store data. Data is stored in buckets and is accessible by end points. Each file is represented as an object which has an object id.

Create a bucket  
Files or objects in S3 are stored in buckets. First thing I should do is create a bucket. A bucket can be created by this command. I will create a bucket named deebucket

```

`
$ aws s3 mb s3://deebucket
`

```

Now bucket names are unique across S3. Not just my account but across all Amazon accounts. Let's see what happens if I create a bucket with existing name.

```

`
$ aws s3 mb s3://deebucket

make_bucket failed: s3://deebucket/ A client error (BucketAlreadyOwnedByYou) occurred when calling the CreateBucket operation: Your previous request to create the named bucket succeeded and you already own it.
`

```

The error I get tells me that I already own a bucket with that name.

What happens if I create a bucket with a name that I do not own. I will try to create a bucket with the name aws-cli. I know that a bucket with that name already exists and it was not created by me. Let's see what happens.

```

`
$ aws s3 mb s3://aws-cli

make_bucket failed: s3://aws-cli/ A client error (BucketAlreadyExists) occurred when calling the CreateBucket operation: The requested bucket name is not available. The bucket namespace is shared by all users of the system. Please select a different name and try again.
`

```

That is what I was expecting. Bucket names are unique across entire S3.

To get a list of my buckets I can run the ls sub-command like this

```

`
$ aws s3 ls

2014-07-01 13:54:02 deebucket
`

```

So I have only one bucket. I should try to put some files into that bucket by copying a locally stored file to my AWS S3 bucket. This can be done by aptly named cp command.

```

`
$ aws s3 cp coco.jpg s3://deebucket

upload: ./coco.jpg to s3://deebucket/coco.jpg
`

```

The command above copies a file called coco.jpg from my current directory into my S3 bucket. Options I give in this command are source and destination. The file I have copied is a cute cat photo and the cat looks like this.

![Coco](http://kapoor.io/wp-content/uploads/2014/07/coco-300x225.jpg "coco.jpg")

What happens if I copy the same file again? The file in my bucket gets overwritten with the new one.

I should copy few more files. In my local directory I have two more files sunset1.jpg and sunset2.jpg. I would like to copy the files that start with characters **sun** into my bucket using the wildcard technique but it turns out that **cp** is a single file operation. To get all my file across I can use the **sync** command which will sync the bucket with my local directory.

```

`
$ aws s3 sync . s3://deebucket

upload: ./sunset2.jpg to s3://deebucket/sunset2.jpg
upload: ./sunset1.jpg to s3://deebucket/sunset1.jpg
`

```

Now I have all my files from my local directory copied over to my S3 bucket.

To get a listing of all files in my bucket I can run this command

```

`
$ aws s3 ls s3://deebucket

2014-07-01 14:06:52      46674 coco.jpg
2014-07-01 14:16:15     105607 sunset1.jpg
2014-07-01 14:16:15      13214 sunset2.jpg
`

```

This is the same command which was used to get a list of buckets. If I pass in a bucket name then it gives me a listing of files within that bucket. Neat!

Next, I want to make my cute cat photo accessible to everyone. I could not find a way to do this from CLI so I will use the management console to grant permissions to my object.

After granting open/download to everyone, my cute cat is accessible at https://s3-ap-southeast-2.amazonaws.com/deebucket/coco.jpg

So today I was able to create S3 buckets and add files to that bucket. I also found out that bucket names are unique and there are certain operations which are single file operations for example cp.
