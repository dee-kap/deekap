---
title: "Android - ListView Tutorial With Images and Text"
date: Tue, 07 Jan 2014 10:20:00 +0000
draft: false
tags: ["Android"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

### Introduction

In this post I will show you how to use a ListView widget to display both images and text. This is a common pattern used by many apps. If you are not familiar with ListView and would like a basic tutorial then please visit [this link](http://www.debugrelease.com/2013/06/19/android-listview-tutorial/). For this tutorial, we will build an app which displays a bunch of items along with an image. I will walk you through the process which will involve creating custom layouts for each item in ListView and creating a custom adapter. Here is a screenshot of what we will build. ![image](http://kapoor.io/wp-content/uploads/2014/01/image7-190x300.png "image")

### Project structure

First we will create an Android Application Module in IntelliJ or an Android application if you are using Eclipse. I use [IntelliJ Community Edition](http://www.jetbrains.com/idea/free_java_ide.html) for my Android development and I suggest that you should also have a look. I will name the package com.debugrelease.android.listviewwithimagesandtext ![SNAGHTML5aec1f5](http://kapoor.io/wp-content/uploads/2014/01/SNAGHTML5aec1f5-300x96.png "SNAGHTML5aec1f5") Other than the name of package and activity name I have not made any changes.

### Items

We need some items which we will display in the ListView. As we are also displaying images along with text, we will need some images. A good place to get some icons is [www.androidicons.com](http://www.androidicons.com/). They also have some icons available for free and those will be enough for this tutorial. Of course you can also use any other images you like. We will copy these images into the assets folder. You can also find the images in the [Github repository](https://github.com/deepak-kapoor/debug-release-android-samples). The project is located in ListViewWithImagesAndText folder. ![image](http://kapoor.io/wp-content/uploads/2014/01/image8-300x168.png "image")

### Model

We will create a new class which will act as the model for our list items. Let’s call this class Item. Here is the code.

```java
package com.debugrelease.android.listviewwithimagesandtext;

public class Item {

    public int Id;
    public String IconFile;
    public String Name;

    public Item(int id, String iconFile, String name) {

        Id = id;
        IconFile = iconFile;
        Name = name;

    }

}

```

We will also create a Model class which will provide us with an ArrayList of our items. Model class also has a method GetById which is used by the adapter. Here is the code for Model class.

```java
package com.debugrelease.android.listviewwithimagesandtext;

import java.util.ArrayList;

public class Model {

    public static ArrayList<Item> Items;

    public static void LoadModel() {

        Items = new ArrayList<Item>();
        Items.add(new Item(1, "ic\_action\_alarm\_2.png", "Alarm"));
        Items.add(new Item(2, "ic\_action\_calculator.png", "Calculator"));
        Items.add(new Item(3, "ic\_action\_google\_play.png", "Play"));
        Items.add(new Item(4, "ic\_action\_line\_chart.png", "Line Chart"));
        Items.add(new Item(5, "ic\_action\_location\_2.png", "Location"));
        Items.add(new Item(6, "ic\_action\_news.png", "News"));
        Items.add(new Item(7, "ic\_action\_stamp.png", "Stamp"));

    }

    public static Item GetbyId(int id){

        for(Item item : Items) {
            if (item.Id == id) {
                return item;
            }
        }
        return null;
    }

}

```

### Layouts

In the main.xml which is the layout used by MainActivity, we will place a ListView widget and set it’s layout_width and layout_height to wrap_content. ListView will also have a id set because we’ll need to reference it in code. Here are contents of main.xml

```xml

<?xml version="1.0" encoding="utf-8"?>

<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
 android:orientation="vertical"
 android:layout_width="fill_parent"
 android:layout_height="fill_parent">

    <ListView
            android:layout\_width="wrap\_content"
            android:layout\_height="wrap\_content"
            android:id="@+id/listView" />

</LinearLayout>

```

Now this is important. If we were just displaying text then there would be no need to create a custom layout, we could just use one from sdk resources. But since we are displaying more than text, we need to create a new layout which will be the template for each item. Let’s call it row.xml

```xml

<?xml version="1.0" encoding="utf-8"?>

<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:gravity="center_vertical"
android:minHeight="64dp">

    <ImageView
            android:id="@+id/imageView"
            android:layout\_width="32dp"
            android:layout\_height="32dp"
            android:layout\_alignParentLeft="true"
            android:layout\_marginLeft="9dp"
            android:layout\_alignParentTop="true"/>
    <TextView
            android:layout\_alignBottom="@+id/imageView"
            android:layout\_width="97dp"
            android:layout\_height="32dp"
            android:id="@+id/textView"
            android:layout\_alignParentLeft="true"
            android:layout\_marginLeft="66dp"
            android:layout\_alignParentRight="true"
            android:gravity="center\_vertical"/>

</RelativeLayout>
```

See how I have placed an ImageView and a TextView within RelativeLayout. For each item one of these will be used.

### Adapter

A ListView needs an adapter to display items. And because of our slightly custom requriement of displaying images and text, we will create our own custom adapter. This can be done by creating a class which extends ArrayAdatpter<String>. In this class **getView** method is of interest to us. Within this method we will inflate the row layout we created earlier. We will then write some code to populate both ImageView and TextView. Below is the full code for our adapter.

```java
package com.debugrelease.android.listviewwithimagesandtext;

import android.content.Context;
import android.graphics.drawable.Drawable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.IOException;
import java.io.InputStream;

public class ItemAdapter extends ArrayAdapter<String> {

    private final Context context;
    private final String\[\] Ids;
    private final int rowResourceId;

    public ItemAdapter(Context context, int textViewResourceId, String\[\] objects) {

        super(context, textViewResourceId, objects);

        this.context = context;
        this.Ids = objects;
        this.rowResourceId = textViewResourceId;

    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

        LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT\_INFLATER\_SERVICE);

        View rowView = inflater.inflate(rowResourceId, parent, false);
        ImageView imageView = (ImageView) rowView.findViewById(R.id.imageView);
        TextView textView = (TextView) rowView.findViewById(R.id.textView);

        int id = Integer.parseInt(Ids\[position\]);
        String imageFile = Model.GetbyId(id).IconFile;

        textView.setText(Model.GetbyId(id).Name);
        // get input stream
        InputStream ims = null;
        try {
            ims = context.getAssets().open(imageFile);
        } catch (IOException e) {
            e.printStackTrace();
        }
        // load image as Drawable
        Drawable d = Drawable.createFromStream(ims, null);
        // set image to ImageView
        imageView.setImageDrawable(d);
        return rowView;

    }

}

```

What’s left now is to load the Model by calling Model.LoadModel static method, finding the ListView and assigning it the adapter. This is done in MainActivity class within overridden onCreate method.

```java
package com.debugrelease.android.listviewwithimagesandtext;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ListView;

public class MainActivity extends Activity {

    ListView listView;

    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        Model.LoadModel();
        listView = (ListView) findViewById(R.id.listView);
        String\[\] ids = new String\[Model.Items.size()\];
        for (int i= 0; i < ids.length; i++){

            ids\[i\] = Integer.toString(i+1);
        }

        ItemAdapter adapter = new ItemAdapter(this,R.layout.row, ids);
        listView.setAdapter(adapter);

    }
}
```

### Conclusion

In conclusion, displaying image and text in each cell of ListView is pretty simple. All you need to do is define your preferred layout for each cell, and create an adapter which will load that view for each position.
The code for this post and all my Android related posts is in a [Github repository](https://github.com/deepak-kapoor/debug-release-android-samples). For this tutorial look for ListViewWithImagesAndText folder within the repository.
Icons used in this post and the code are from [androidicons.com](http://www.androidicons.com/)
