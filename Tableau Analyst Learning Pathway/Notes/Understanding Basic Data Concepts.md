---
tags:
  - datascience
  - notes
  - tableau
university: Tableau eLearning
year: "2025"
link:
cover:
description:
---

`BUTTON[class_home, class_link]`

 ```meta-bind-button
label: Return to Analyst Learning Path
icon: "home"
hidden: true
class: navigation-buttons
tooltip: ""
id: class_home
style: primary
actions:
  - type: open
    link: "[[Analyst Learning Path]]"

```
```meta-bind-button
label: Analyst Learning Path
icon: "globe"
hidden: true
class: course-navigation-buttons
tooltip: ""
id: class_link
style: primary
actions:
  - type: open
    link: "https://elearning.tableau.com/path/analyst-learning-path"

```
```meta-bind-button
label: "Next: Part 2 - Reading Common Chart Types"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Reading Common Chart Types]]"

```
```meta-bind-button
label: "Previous: Basics of Reading Data"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Basics of Reading Data]]"

```
# Understanding Basic Data Concepts
---
## Common Types of Data Sets

What is a data set?

A data set (sometimes referred to as data source, or database) in the context of Tableau, contains the data used to build visualizations. Every bar chart, scatter plot, or line chart you see in Tableau has a connected database or spreadsheet that supplies the data.

You can learn more about different data source types below.

**Spreadsheets:** A spreadsheet, such as Microsoft Excel or Google sheets, organizes data in a flat structure, which means the records are stored as single rows of data.

**Rational databases:** Relational databases store data in multiple tables, with each row assigned a unique identifier. Users pull data from different tables together using Structured Query Language (SQL). The "relational" aspect indicates a logical connection between different tables.

**Cloud data:** Sometimes, organizations prefer to store their data in the cloud so they do not have to support on-premises servers. This includes data stored in such places as Amazon Web Services or Microsoft Azure.

**Other types of connections:** Tableau also connects to spatial files for mapping, such as .kml or .shp, and statistical files created in R.

### What happens when Tableau Desktop connects to a data set?

When users connect to Tableau, the data fields in their data set are automatically assigned a _role_ and a _type_.

| Role                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A field can be assigned to a _Dimension_ role or a _Measure_ role.  <br>  <br>We'll learn more about dimensions and measures in the next lesson. | The field's data type defines if the field is, for example, a string, integer, or date.  <br>  <br>Data types can be changed by the user if Tableau does not assign the type appropriately. Any changes are saved in a Tableau data source (.tds) file as *metadata — which is a set of data that describes other data.* |

### After Tableau connects to data....
General process after connection:

#### Connect
![[connect.png]]

After the connection, Tableau reads the data and assigns a data type to each field (see orange box).

#### Evaluate
![[evaluate.png|white]]

Users verify that Tableau has correctly assigned data types, and they can make changes on the **Data Source** page if the data type is wrong. They can also rename unclear or misspelled fields.

Any changes made in Tableau are not written to the native data source. Changes are instead stored as metadata in a Tableau file called a Tableau Data Source, or .tds.


#### Analyze and Share
![[analyse_and_share.png]]

After connecting to data and adjusting the metadata, users can open a sheet to begin building charts, analyzing data, and sharing results.



> [!example|callout_quote] Quote
>   
To read a chart, you don't need to be an expert in databases or spreadsheets. But with a small amount of data knowledge, you'll feel more at ease in the world of data.




## A Closer Look at Fields

### What is a field?
A field, also known as a column, is a single piece of information from a record in a data set. 

For example, if you were to collect data on how many times a week a commuter chose different modes of transportation, your data set could include:

|Commuter name|Mode|Days per week|
|---|---|---|
|Neil|Walk|2|
|Neil|Bus|3|
|Lin|Bicycle|1|
|Lin|Carpool or Vanpool|3|
|Lin|Bus|1|
|Mae|Car (Single Occupancy Vehicle)|2|
|Mae|Bicycle|3|

_Commuter name_, _Mode_, and _Days per week_ are all fields. Commuter name and Mode are qualitative fields, while Days per week is a quantitative field. 

The members of the Commuter name and Mode field are limited to relevant categories. You would not include _apple_ as an option in Mode because it doesn't match the definition of the field.

The Days per week uses a range of 1-7 rather than categorical members. If you wanted to collect data on modes that people did not use, your range might include 0, too.  

You would not include negative values in the Days per week range, since you can't measure a negative trip. If you were measuring temperatures or profit, however, you could have a range that included negative numbers.

In Tableau, quantitative fields are referred to as _Measures_, and qualitative fields are referred to as _Dimensions_.

#### Qualitative Fields (Dimensions)
- Describes or categorizes data
- Tells you what, when, or who
- Slices the quantitative data

#### Quantitative Fields (Measures)
- Numerical data
- Provides the measurement for qualitative category
- Can be used in calculations


> [!example|callout_quote] Quote
> Dimensions and measures are the building blocks of Tableau charts.



### Fields in Tableau

![[Datapane.png]]

When Tableau connected to this data set, it assigned the fields to either Dimensions or Measures.

- The qualitative fields that describe categories of data are in the top part of the pane, under **Dimensions**.
- The quantitative fields that measure categories of data are in the bottom part of the pane, under **Measures**.

### How do these fields create a visualization?

Let's build a chart! Even if you aren't a builder of charts, as a consumer you can better understand the finished product if you see how dimensions (qualitative) and measures (quantitative) are used to create visualizations and explore data.

#### How many wildlife strikes occurred?

![[dim_meas_step1.png]]
First, drag out a quantitative field, or measure, to find out "how many?" We'll use **Number of Strikes**. Notice that the field displays on the **Columns** shelf in green. 

Tableau created a long bar and an axis showing a range of values.

#### How many wildlife strikes by animal category?

![[dim_meas_step2.png]]

We need to bring in qualitative fields, or dimensions, to better understand our data. If we add the dimension **Animal Category**, we can see that birds make up most of the wildlife strikes. The single bar breaks into four, one for each category. Dimension fields display in blue when brought onto the sheet.

#### Which birds account for the most wildlife strikes?

![[dim_meas_step3.png]]

First, let's make **Animal Category** a filter, and add the **Animal Species** dimension field to look more closely at each category.

To see more details about the birds specifically, we filter the view to show only bird species.

#### Which species of bird is associated with the highest costs?

![[dim_meas_step4.png]]

We can add another measure field, **Cost: Total $**, to C**olor** to see which species of birds result in the costliest accidents.

It is interesting that the Canada goose is not involved in the highest number of bird strikes, but caused the most damage.

#### What did we discover?
- As we added more dimensions to the view, the single bar representing all of the wildlife strikes was sliced into smaller categories of data. 
- Using the filter allowed us to focus on a specific subset of data. 
- We found an interesting data slice regarding the Canada goose that we should probably ask more questions about. 

In Tableau, moving dimensions and measures in and out of the view changes the resulting chart. It's a useful way to view different aspects of your data, and helps uncover the trends and stories that affect your organization.


## What is a row-level record?

> [!example|callout_quote] Quote
> Understanding how to answer the question "What does a row of data contain?" empowers you to ask questions about the data you encounter.


"What does a row of data contain?" is a simple but important question, and it can have a complex answer.  Remember the commuter data we reviewed in the previous lesson?

|Commuter name|Mode|Days per week|
|---|---|---|
|Neil|Walk|2|
|Neil|Bus|3|
|Lin|Bicycle|1|
|Lin|Carpool or Vanpool|3|
|Lin|Bus|1|
|Mae|Car (Single Occupancy Vehicle)|2|
|Mae|Bicycle|3|

Each row captured the number of days per week a commuter used a particular mode of transportation to get to work, but it did not include a lot of details about the trips. For example, most people take two commuting trips a day if they go to work, and they might choose a different mode of transportation for each. Commuters might use multiple modes on a single trip to get to work or to get home. Our first data set doesn't capture those details.

What if you wanted to know:

- How many commuters used multiple modes of transportation in a single day?
- How did commutes to work compare against commutes from work?
- How long did different commutes take?
- What was the length of each trip?

If you wanted to answer those questions, you would need to collect more detailed data, like this:

|Commuter name|Trip|Time start|Time end|Date|Mode|Est. miles|
|---|---|---|---|---|---|---|
|Mae|To work|7:45 am|8:50 am|7/17/2019|Bicycle|9|
|Mae|From work|5:15 pm|5:45 pm|7/17/2019|Bus|6|
|Mae|From work|5:45 pm|6:15 pm|7/17/2019|Bicycle|3|

**In the second data set, a row of data is more detailed, or, *granular*, than in the first data set.**

### Why does knowing data granularity matter?
Data granularity refers to the level of detail for a piece of data, wherever you are looking. As data becomes less granular, we might describe it as an _aggregation,_ or as _aggregated data_.  Aggregation refers to how data is combined. The level of granularity or aggregation in a row or chart affects the questions we can ask of the data, and the discoveries we can make.

#### In a spreadsheet:
The row-level data in this data set records collisions from wildlife strikes and is detailed down to the date and time of the incident. We would describe the data here as more granular.

![[granularity_xls.png]]

#### In a chart:
In this view, wildlife strikes are aggregated into bars, representing all of the rows of data associated with specific airports (shown by Airport code). We would describe this data as less granular.

![[granularity_chart_example.png]]



#### What if it's not in the data?
Your ability to explore the data you have, and ask questions about it, can be limited by the level of granularity contained in the view or the data source itself.

If your questions reach the limits of your data:

- Raise data quality issues with your Data Steward. 
- Ask champions and sponsors to consider expanding access to your organization's other sources of data. 
- Describe the data questions you hope to explore and answer.
- Provide detailed feedback so that others can develop a plan to collect more and better data.


### How can I determine the level of detail contained in a row of data when I only have access to a visualization?
You can select a mark in a visualization, and then right-click to view underlying data, if the view's author has enabled it. You can view the row-level records of the data behind the visualization, which is how you can determine the depth of detail the data set contains.


## Granularity and aggregation in Tableau
When you move dimensions and measures in and out of a view, the view's level of detail changes. 

- By default, measures placed in a view are aggregated by SUM, which means that the data for that field in all of the rows is combined.
- Measures can also be aggregated as average, median, count, or count distinct.
- Dimensions break down the aggregated total into smaller totals by category.

The "Aggregation, Granularity, and Ratio Calculations" video from Tableau goes into more detail about aggregation and data granularity. It uses the example of looking at profit ratios and can help you understand the behavior of Tableau charts.

![[transcoded-s9DXJIJRwuMNHxqO-aggregation-granularity-and-ratio-calculations.mp4]]
[[aggregation_granularity_and_ratio_calculations_transcript.pdf]]

If you have access to Tableau Desktop, **download** the workbook and solution zip file to follow along on your own.

```button
name Open aggregation_granularity_and_ratio_calculations.zip
type link
action file:////Users/rachel/Library/CloudStorage/SynologyDrive-SharkologyDC/GitHub Repos/Data-Science-Classes/Tableau eLearning/downloadable data/aggregation_granularity_and_ratio_calculations.zip
color blue
```


## How data is represented in Tableau
In the first lesson, Common data set types, we learned about data roles and data types. This lesson shows how they are represented in the Tableau user interface.

Each field in the Tableau **Data** pane has an icon to the left showing the field's data type. Fields are assigned both a data type and role automatically when you connect to data in Tableau. You can manually change the type in the data grid or **Data** pane.

![[ucNzPk90KCe8iuB6-datapane-withcallouts.png]]

**Hierarchy:** 
The Country, State, and City fields have been organized into a hierarchy.  This is useful for creating drill-downs in charts.

**Blue text field:** 
Customer name is a categorical, or qualitative, field. 

A  blue icon indicates that the field is discrete, which means it is data that contains separate parts.

Most dimensions are discrete fields.

**Invalid field:**
The red exclamation point on this calculated field indicates a problem. The red exclamation point can mean a field is missing, or, in this case, that the calculated field is broken.

**Date:**
The Ship Date icon is a date field. Dates can be discrete or continuous. The date in this image is blue, which tells us it is discrete.

If you are building charts that use date fields, it's important to understand how Tableau processes dates.

**Calculated field:**
Profit Ratio is a calculated field. The green icon indicates it is a continuous field. 

Continuous means data value in the set can be any value in the range. 

Most measures are continuous fields.

**Tableau-generated fields:**
The fields highlighted in orange are all Tableau-generated fields. 

Sometimes they are added to the view automatically, depending on the type of chart you are building. As you become more proficient at building charts, you will learn how to use these fields without Tableau's help.

The following video has more details about what Tableau does with different data fields, and it includes the following information:

- More about dimensions and measures, and discrete and continuous fields
- What happens when you change a default type
- The difference between axes and labels
- How different data fields behave in views

![[transcoded-R2oSh206VwUjk9MC-understanding-pill-types.mp4]]
[[understanding_pill_types_transcript.pdf]]

If you have access to Tableau Desktop, **download** the workbook and solution zip file to follow along on your own.

```button
name Open understanding_pill_types.zip
type link
action file:////Users/rachel/Library/CloudStorage/SynologyDrive-SharkologyDC/GitHub Repos/Data-Science-Classes/Tableau eLearning/downloadable data/understanding_pill_types.zip
color blue
```




`BUTTON[previous, next]`
