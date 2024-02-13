---
title: "AWS - Download Upload file from S3 bucket using AWS SDK for Ruby"
date: Thu, 03 Jul 2014 10:25:00 +0000
draft: false
tags: ["Cloud"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

AWS SDK for Ruby can be used to copy files which are called objects in AWS terminology to and from S3 buckets. I feel like trying this out today. I already have the aws-sdk gem installed on my machine. Let's write the script.

### Upload/Copy file to S3 bucket

First thing I need in my script is

```

`
require 'aws-sdk'
`

```

After this I create an instance of S3 object and get the bucket I created earlier.

```

`
s3 = AWS::S3.new

bucket = s3.buckets['deebucket']
`

```

Now I can copy the file over to the bucket by using the `#write` method on S3Bucket object.

```

`
object_name = 'coco.jpg'
bucket.objects[object_name].write(:file => object_name)
`

```

### Download/Copy file from S3 bucket

S3Object also provides a `#read` method which can be used to read the file. In the code below I open a file for writing and in the block I write the file retrieved from S3 as a stream.

```

`
File.open(object_name, 'w') do |f|
  f.write(bucket.objects[object_name].read)
end
`

```

Simple enough to read and write S3 objects. There are better ways to conduct read and write operations. I would like to include some error handling and work with multiple objects. I will write a post once I have figured them out.
