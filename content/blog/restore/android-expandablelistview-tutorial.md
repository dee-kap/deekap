---
title: "Android - ExpandableListView Tutorial"
date: Wed, 31 Jul 2013 03:24:00 +0000
draft: false
tags: ["Android"]
---

<div class="restore">
This post is a part of the  <a href="/project-restore/">Project Restore</a>, with the primary aim of excavating my previous writings. The material contained herein may not hold practical relevance and is most likely completely useless.
</div>

### Introduction

In this tutorial I will show you how to use **ExpandableListView** widget in your Android app. ExpandableListView widget is used to display hierarchical data which is two levels deep. If your hierarchy is more than two levels then you should look at options other than ExpandableListView. Now let’s get started.  
We will develop an app which displays a bunch of countries with some of their cities. When a user taps the name of a country, the widget expands to show cities. Below is a screenshot of the app.

![](http://kapoor.io/wp-content/uploads/2013/07/ExpandableList2-260x300.png)

### Setup

First thing we need is a class to hold information about countries and cities. Let’s create a class called Country.

```
public class Country {
  private String Name;
  private List Cities;

  public Country(String name, List cities) {
    Name = name;
    Cities = cities;
  }

  public String getName() {
    return Name;
  }

  public List getCities() {
    return Cities;
  }
}
```

We will later populate a list of countries in our activity.

### Adapter

Like [ListView](http://www.debugrelease.com/2013/06/19/android-listview-tutorial/) widget, ExpandableListView also works with an adapter. Android SDK provides a BaseExpandableListAdapter which we can use for our simple example. We will provide a constructor which takes a Context and a List of countries as arguments.

```
public CountryAdapter(Context context, List countries) {
  this.countries = countries;
  inflater = LayoutInflater.from(context);
}
```

The constructor will set the private member countries which will be later used by overriden methods in our adapter. We will also set our private Inflater object by calling LayoutInflater.from() method.

Next come the overrides which do most of the work. Before we get into the methods, let’s understand how ExpandableListView works. The concept is very simple, you have groups which in our case are countries. Within each group you have children which are cities in our example. And it is just that simple. Let’s look at some of the methods we will override in our adapter.

````
@Override
public int getGroupCount() {
  return countries.size();
}

```**getChildrenCount** returns the count of children. This method accepts one argument which is groupPosition. What we return here is the count of children for a particular group. In our example we will return the count of cities for a country.

````

@Override  
public int getChildrenCount(int groupPosition) {  
 return countries.get(groupPosition).getCities().size();  
}

```**hasStableIds** method is used to inform if the id values for our objects will change during the course of our app.

**getGroupView** is used to return a view which will be drawn for each group item. In this case we are using the simple\_expandable\_list\_item\_1 layout which is a part of the SDK.

```

@Override  
public View getGroupView(int groupPosition, boolean isExpanded, View convertView, ViewGroup parent) {  
 if (convertView == null) {  
 convertView = inflater.inflate(R.layout.simple_expandable_list_item_1, parent, false);  
 }

((TextView) convertView).setText(getGroup(groupPosition).toString());  
 return convertView;  
}

```
Similarly **getChildView** returns the view used by each child item.

Some of the other methods such as getGroup, getChild, getGroupId and getChildId are fairly intuitive.
Below is the entire code for our adapter.

```

package com.debugrelease.android.ExpandableListViewTutorial;

import android.R;  
import android.content.Context;  
import android.view.LayoutInflater;  
import android.view.View;  
import android.view.ViewGroup;  
import android.widget.BaseExpandableListAdapter;  
import android.widget.TextView;

import java.util.List;

public class CountryAdapter extends BaseExpandableListAdapter {  
 private List countries;  
 private LayoutInflater inflater;

public CountryAdapter(Context context, List countries) {  
 this.countries = countries;  
 inflater = LayoutInflater.from(context);  
 }

@Override  
 public int getGroupCount() {  
 return countries.size();  
 }

@Override  
 public int getChildrenCount(int groupPosition) {  
 return countries.get(groupPosition).getCities().size();  
 }

@Override  
 public Object getGroup(int groupPosition) {  
 return countries.get(groupPosition).getName();  
 }

@Override  
 public Object getChild(int groupPosition, int childPosition) {  
 return countries.get(groupPosition).getCities().get(childPosition);  
 }

@Override  
 public long getGroupId(int groupPosition) {  
 return groupPosition;  
 }

@Override  
 public long getChildId(int groupPosition, int childPosition) {  
 return childPosition;  
 }

@Override  
 public boolean hasStableIds() {  
 return true;  
 }

@Override  
 public View getGroupView(int groupPosition, boolean isExpanded, View convertView, ViewGroup parent) {  
 if (convertView == null) {  
 convertView = inflater.inflate(R.layout.simple_expandable_list_item_1, parent, false);  
 }

    ((TextView) convertView).setText(getGroup(groupPosition).toString());
    return convertView;

}

@Override  
 public View getChildView(int groupPosition, int childPosition, boolean isLastChild, View convertView, ViewGroup parent) {  
 if(convertView == null) {  
 convertView = inflater.inflate(R.layout.simple_list_item_1, parent, false);  
 }

    ((TextView)convertView).setText(getChild(groupPosition,childPosition).toString());
    return convertView;

}

@Override  
 public boolean isChildSelectable(int i, int i2) {  
 return false;  
 }  
}

```

### Main Activity

The layout for our MainActivity will include an ExpandableListView within a [LinearLayout](http://www.debugrelease.com/2013/06/11/android-linear-layout-example/).

```

<?xml version="1.0" encoding="utf-8"?>

<manifest xmlns:android="http://schemas.android.com/apk/res/android"  
  package="com.debugrelease.android.ExpandableListViewTutorial"  
  android:versionCode="1"  
  android:versionName="1.0">  
 <uses-sdk android:minSdkVersion="15"/>  
 <application android:label="@string/app\_name" android:icon="@drawable/ic\_launcher">  
 <activity android:name="MainActivity"  
          android:label="@string/app\_name">  
 <intent-filter>  
 <action android:name="android.intent.action.MAIN"/>  
 <category android:name="android.intent.category.LAUNCHER"/>  
 </intent-filter>  
 </activity>  
 </application>  
</manifest>

```
In our MainActivity class we will tie everything together. In this class we will load up a list of countries and in the **onCreate** method, we will set the adapter for our ExpandableListView. Below is the code for MainActivity.java

```

package com.debugrelease.android.ExpandableListViewTutorial;

import android.app.Activity;  
import android.os.Bundle;  
import android.widget.ExpandableListView;

import java.util.ArrayList;  
import java.util.Arrays;  
import java.util.List;

public class MainActivity extends Activity {  
 private static List Countries;  
 private ExpandableListView expandableListView;  
 private CountryAdapter adapter;

@Override  
 public void onCreate(Bundle savedInstanceState) {  
 super.onCreate(savedInstanceState);  
 setContentView(R.layout.main);

    LoadCountries();
    expandableListView = (ExpandableListView) findViewById(R.id.expandableListView);
    adapter = new CountryAdapter(this, Countries);
    expandableListView.setAdapter(adapter);

}

private void LoadCountries() {  
 Countries = new ArrayList();

    ArrayList citiesAustralia = new ArrayList(
        Arrays.asList("Brisbane", "Hobart", "Melbourne", "Sydney"));
    Countries.add(new Country("Australia", citiesAustralia));

    ArrayList citiesChina = new ArrayList(
        Arrays.asList("Beijing", "Chuzhou", "Dongguan", "Shangzhou"));
    Countries.add(new Country("China", citiesChina));

    ArrayList citiesIndia = new ArrayList(
        Arrays.asList("Bombay", "Calcutta", "Delhi", "Madras"));
    Countries.add(new Country("India", citiesIndia));

    ArrayList citiesNewZealand = new ArrayList(
        Arrays.asList("Auckland", "Christchurch", "Wellington"));
    Countries.add(new Country("New Zealand", citiesNewZealand));

    ArrayList citiesRussia = new ArrayList(
        Arrays.asList("Moscow", "Kursk", "Novosibirsk", "Saint Petersburg"));
    Countries.add(new Country("Russia", citiesRussia));

}  
}

```

### Conclusion

Like most of the other widgets, ExpandableListView is also very simple to work with. In this tutorial we saw an example which displays two levels deep hierarchical data of countries and cities using ExpandableListView. I hope you enjoyed it. Please leave a comment if you’d like to discuss something or have any questions.
The code for this tutorial can be found in my [Github repository](http://bit.ly/debrel-android-samples). Within the repository look for ExpandableListViewTutorial folder.
```
