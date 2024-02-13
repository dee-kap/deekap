---
title: "Android - Linear Layout Example"
date: Tue, 07 Jan 2014 10:19:00 +0000
draft: false
tags: ["Android"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

In Android Layouts are containers in which you place your widgets like buttons, images, lists etc. Two of the most useful layouts are LinearLayout and RelativeLayout. In this post I will talk about LinearLayout. LinearLayout extends android.view.ViewGroup which extends android.view.View object. As the name suggests, LinearLayout is used to place widgets in a linear manner. By default widgets are stacked vertically as shown in the image below. ![verticalLayout](http://kapoor.io/wp-content/uploads/2014/01/verticalLayout-168x300.gif "verticalLayout") Here is another example of an app running in the emulator. ![image](http://kapoor.io/wp-content/uploads/2014/01/image-300x134.png "image") To get this layout you can use the following xml```

<?xml version="1.0" encoding="utf-8"?>

<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"  
 android:orientation="vertical"  
 android:layout_width="fill_parent"  
 android:layout_height="fill_parent">  
 <TextView  
 android:layout_width="fill_parent"  
 android:layout_height="wrap_content"  
 android:text="Hello World, MyActivity"  
 />  
 <TextView  
 android:layout_width="fill_parent"  
 android:layout_height="wrap_content"  
 android:text="New Text"  
 android:id="@+id/textView" android:layout_gravity="center"/>  
 <Button  
 android:layout_width="fill_parent"  
 android:layout_height="wrap_content"  
 android:text="New Button"  
 android:id="@+id/button" android:layout_gravity="center"/>  
 <WebView  
 android:layout_width="fill_parent"  
 android:layout_height="fill_parent"  
 android:id="@+id/webView"/>  
</LinearLayout>

````
Other than stacking widgets vertically, LinearLayout can also stack them horizontally. All you need to do is change android:orientation to be horizontal `android:orientation=”horizontal”`
Let’s look at some slightly advance concepts. First one is the fill model. In the code above you will notice that android:layout\_width and android:layout\_height are either set to fill\_parent or wrap\_content. These values are very useful when placing widgets in a LinearLayout or for that matter any kind of layout.
I will use this new example to explain few concepts. In this layout I have three TextView objects placed within a LinearLayout. To make them standout I have added some color. Here is the code.```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
              android:orientation="vertical"
              android:layout\_width="fill\_parent"
              android:layout\_height="fill\_parent" >

    <TextView
            android:layout\_width="fill\_parent"
            android:layout\_height="wrap\_content"
            android:text="Text View 1"
            android:background="#bfffd9"
            android:textColor="#000000"/>

    <TextView
            android:layout\_width="fill\_parent"
            android:layout\_height="wrap\_content"
            android:text="Text View 2"
            android:background="#ffd4b4"
            android:textColor="#000000"/>

    <TextView
            android:layout\_width="fill\_parent"
            android:layout\_height="wrap\_content"
            android:text="Text View 3"
            android:background="#a9d2ff"
            android:textColor="#000000"/>
</LinearLayout>
````

The view rendered by the code above will be  
![image](http://kapoor.io/wp-content/uploads/2014/01/image1-225x300.png "image")  
Let’s play a bit with the height property. I will set android:LayoutHeight of second TextView to be fill_parent. Doing so results in this  
![image](http://kapoor.io/wp-content/uploads/2014/01/image2-225x300.png "image")  
What happened to the third TextView? Where did it go? Technically it is still there but you cannot see it. The way this works is that the layout system places TextView 1, it then puts the second TextView if there is space available and then the third one if there is space available. Because the second TextView has taken up the remaing space, there is no space left for third TextView.  
What if I change Layout_Height of second TextView to wrap_content and for the third TextView make it fill_parent. Here is the full code.```

<?xml version="1.0" encoding="utf-8"?>

<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"  
 android:orientation="vertical"  
 android:layout_width="fill_parent"  
 android:layout_height="fill_parent" >

    <TextView
            android:layout\_width="fill\_parent"
            android:layout\_height="wrap\_content"
            android:text="Text View 1"
            android:background="#bfffd9"
            android:textColor="#000000"/>

    <TextView
            android:layout\_width="fill\_parent"
            android:layout\_height="wrap\_content"
            android:text="Text View 2"
            android:background="#ffd4b4"
            android:textColor="#000000"/>

    <TextView
            android:layout\_width="fill\_parent"
            android:layout\_height="fill\_parent"
            android:text="Text View 3"
            android:background="#a9d2ff"
            android:textColor="#000000"/>

</LinearLayout>
```  
This will give us  
![image](http://kapoor.io/wp-content/uploads/2014/01/image3-225x300.png "image")  
There is another important concept when it comes to placing widgets and that is “Weight”. Let’s look at the effect of weight on our TextViews. By default all widgets placed inside LinearLayout have the same weight i.e. zero. Let’s see what happens if we increase the weight of our first TextView to be 1.```
<TextView  
            android:layout\_width="fill\_parent"  
            android:layout\_height="wrap\_content"  
            android:text="Text View 1"  
            android:background="#bfffd9"  
            android:textColor="#000000"  
            android:layout\_weight="1" />
```  
![image](http://kapoor.io/wp-content/uploads/2014/01/image4-225x300.png "image")  
See how first TextView has pushed the other two down. One way to look at this is that first TextView is heavier (we are talking about weight here) than the other two and so takes up more room.  
What if we assign the same value for layout\_weight to all our TextViews.```
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"  
              android:orientation="vertical"  
              android:layout\_width="fill\_parent"  
              android:layout\_height="fill\_parent" >  
  
    <TextView  
            android:layout\_width="fill\_parent"  
            android:layout\_height="wrap\_content"  
            android:text="Text View 1"  
            android:background="#bfffd9"  
            android:textColor="#000000"  
            android:layout\_weight="1"  
            />  
  
    <TextView  
            android:layout\_width="fill\_parent"  
            android:layout\_height="wrap\_content"  
            android:text="Text View 2"  
            android:background="#ffd4b4"  
            android:textColor="#000000"  
            android:layout\_weight="1"/>  
  
    <TextView  
            android:layout\_width="fill\_parent"  
            android:layout\_height="wrap\_content"  
            android:text="Text View 3"  
            android:background="#a9d2ff"  
            android:textColor="#000000"  
            android:layout\_weight="1"/>  
</LinearLayout>
```  
We get this  
![image](http://kapoor.io/wp-content/uploads/2014/01/image5-225x300.png "image")  
All three TextViews have the same height. Do you see the power of layout\_weight here? One more example where we want the first and second TextView to take up half of the space combined and let the third one take the other half. This can be done by setting the layout\_weight of our third TextView to be 2.```
<?xml version="1.0" encoding="utf-8"?>  
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"  
              android:orientation="vertical"  
              android:layout\_width="fill\_parent"  
              android:layout\_height="fill\_parent" >  
  
    <TextView  
            android:layout\_width="fill\_parent"  
            android:layout\_height="wrap\_content"  
            android:text="Text View 1"  
            android:background="#bfffd9"  
            android:textColor="#000000"  
            android:layout\_weight="1"  
            />  
  
    <TextView  
            android:layout\_width="fill\_parent"  
            android:layout\_height="wrap\_content"  
            android:text="Text View 2"  
            android:background="#ffd4b4"  
            android:textColor="#000000"  
            android:layout\_weight="1"/>  
  
    <TextView  
            android:layout\_width="fill\_parent"  
            android:layout\_height="wrap\_content"  
            android:text="Text View 3"  
            android:background="#a9d2ff"  
            android:textColor="#000000"  
            android:layout\_weight="2"/>  
</LinearLayout>
```  
![image](http://kapoor.io/wp-content/uploads/2014/01/image61-225x300.png "image")  
Other than layout\_width, layout\_height and layout\_weight, there are many other attributes available which have significant affect on widget’s placement within a layout container. I will leave them for another day.
