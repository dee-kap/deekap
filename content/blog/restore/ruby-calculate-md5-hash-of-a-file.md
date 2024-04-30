---
title: "Ruby - Calculate MD5 hash of a file"
date: Fri, 04 Jul 2014 10:44:00 +0000
draft: false
tags: ["Ruby"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

Ruby makes calculating MD5 hash easy peasy.

Here I am calculating MD5 hash of a file I have.

```

`
require 'digest/md5'

md5 = Ditest::MD5.new
digest = md5.hexdigest(File.read('/Users/deepak/s3/coco.jpg'))

puts digest # => "ed00890f2e661a94fdf046c503d0ce34"
`

```

Code above can be shortened to this

```

`
require 'digest/md5'

digest = Digest::MD5.hexdigest(File.read('/Users/deepak/s3/coco.jpg'))

puts digest # => "ed00890f2e661a94fdf046c503d0ce34"
`

```

It can be further shortened to this. I prefer doing it this way because the entire file is not read into memory at once but as blocks.

```

`
require 'digest/md5'

digest = Digest::MD5.file('/Users/deepak/s3/coco.jpg')

puts digest # => #
`

```

Gotta love Ruby :)
