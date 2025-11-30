---
tags:
  - datascience
  - notes
  - tableau
university: Tableau eLearning
year: "2025"
link: https://elearning.tableau.com/path/analyst-learning-path
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
label: "Next: Get Started with Tableau Pulse"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Get Started with Tableau Pulse]]"

```
```meta-bind-button
label: "Previous: Introduction to Tableau Prep"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Introduction to Tableau Prep Builder]]"

```
# Stepping through the workflow
---
## The Tableau Prep Builder data preparation process

### Explore the data preparation process
Have you ever been deep in analysis and then realized that your data is "dirty" with inconsistencies and needs to be cleaned before you can continue? Tableau Prep Builder is a visual data preparation tool you can use to clean and prepare data for these situations and more, such as reshaping and combining your data.

#### Three high-level steps
In this short video, you’ll see an introduction to the three main steps to preparing data in Tableau Prep Builder and how the rest of the module will help you learn how to use these steps.

![[aw6T8aY6brw7EFMK_transcoded-6HYDOFCeigzWwD_Z-Data Prep Process.mp4]]
***An introduction to the three main steps to preparing data in Tableau Prep Builder***

As shown in the video, the three main steps to preparing data in Tableau Prep Builder are:
- Connect to data.
- Clean the data.
- Output the data.

**Connect the data**
Connect to numerous popular data types using built-in and custom connectors. Tableau data extracts, and Tableau published data sources.

**Clean the data**
Clean using one-click and more complex operations. You can also use other operations to shape and combine data.

**Output the data**
Output the cleaned data to a published data source, a database table, or a file (Prep desktop application only).

You will see demos and perform hands-on activities for each of these main steps in the other lessons in this module.

#### Example: The need for data cleaning

Use Tableau Prep Builder to clean up data inconsistencies, such as misspellings, extra spaces, capitalization, and punctuation to make your analysis in Tableau more efficient. 

Watch this short video to see an example of how these data inconsistencies can impact your analysis.

![[a5bX__1S2d7sxBMR_transcoded-cZI14jCSlJZSRJoy-Need for Data Prep.mp4]]
***Data inconsistencies interfering with analysis in Tableau***

#### Summary
In this lesson you learned the three main steps for preparing data in Tableau Prep Builder: connecting to data, cleaning the data, and outputting the data.

In the activity that follows, you’ll practice the first step by opening Tableau Prep Builder and connecting to data.



## Connecting to data
### Try it! Connect Tableau Prep Builder to your data source
You've been introduced to the three main steps for preparing data in Tableau Prep Builder. Here’s your opportunity to practice the first step and get oriented to using the Tableau Prep Builder workspace.

#### Hands-on activity
You will need Tableau Prep Builder on the desktop or on the web for this hands-on activity. If you do not already have Tableau Prep Builder installed, you may purchase it or download a free trial version from the following locations:

- [Tableau Prep Builder](https://tabsoft.co/2PWTl8r)[](http://tabsoft.co/2qTFJ1H)

Note: The free trial is available for a limited number of days.

Imagine that you have data about donations made to a non-profit company. To start the data prep process, open Tableau Prep Builder, and connect to your data. To begin exploring your data, you’ll add a step to the flow. 

Good luck!

![[Cj6wl4UOXnEPSYJr_Hb65yd_KKyW8IuaT.jpg]]
***Final view when the steps have been completed***

Download the **file** below to use with this activity:

```button
name Open Non-Profit Donations South.csv
type link
action file:////Users/rachel/Library/CloudStorage/SynologyDrive-SharkologyDC/GitHub Repos/Data-Science-Classes/Tableau eLearning/downloadable data/Non-Profit Donations South.csv
color blue
```

Follow the **steps** below to complete this activity
1. In Tableau Prep Builder, connect to the text file, **Non-Profit Donations South.csv**.
	Expected result:
	![[Xfa3l31W43b3WYaT_tCvnut_aWQK2S4-4.jpg]]
	Hint:
	1. On the Tableau Prep Builder **Start** page, click the **Connect to Data** button.
	2. The **Connections** pane expands, and you see a list of types of data sources.
	3. In the list of connections, click **Text file**.
	4. In the **Open** dialog box, browse to where you saved the file you downloaded, **Non-Profit Donations South.csv**.
	5. Select the file, and click **Open**.
	
2. Get oriented to the Tableau Prep Builder workspace.
	Expected result:
	![[PVLilYcwZaXQPEJu_TANGmpbKQKH3WJXH.jpg]]
	Hint:
	1. The data file appears in the **Connections** pane.
	2. Tableau Prep Builder has created an input step for the single table of data.
	3. The input step is added to the flow pane as the first step in the flow.    
	4. The input pane lists the fields in your data and other details, such as the field name and data type.
	
3. Check your understanding. Looking at the fields listed in the input step in the flow, use the input pane to answer the following question: **How many fields are in this data?**
	Answer: There are 9 fields in the data.
	![[XwN7Agg30ZJ8x6pW_AgkU9QJDOrd_s66H.png]]

4. Add a cleaning step to the flow.
	Expected result:
	![[vgUqezn4rTo1hoNC_Ekfydx8J5R3bkQ-D.jpg]]
	Hint:
	1. In the flow pane, next to the input step, click the plus icon.  A menu displays the types of steps you can add to a flow.
	2. Click **Clean Step**.  You’ll see that your data now displays in a different way.
	Note: Alternatively, for the very first cleaning step, click the dashed box labeled "View and clean data."
	
5. Explore the workspace.
	Expected result:
	![[GpEdMT_ry25JSyNn_DJLWF-NcI72Dl7Zk.png]]
	Hint: 
	When the cleaning step is selected in the flow pane, you see these areas in the workspace:
	1. The profile pane shows information about the structure of the data.
	2. The data grid gives a view of the data row by row.
	
6. Check your understanding.  Noting that the number of unique values is shown to the right of each field name in the profile pane, use your work to answer the following question:  **How many unique values are there in the Donor Potential field?**
	Answer: There are 7 unique values for the **Donor Potential** field.
	![[jeW4Fr1b0geJTqTG_thSnd213m1wH9h2K.png]]


#### Resources
The following resources describe:
- The main components of the Tableau Prep Builder workspace and the purpose of each.
- The types of steps you can use in Tableau Prep Builder, including the input and cleaning steps you created in this activity.

Download the **files** below to use as reference guides when you work in Tableau Prep Builder.

[[The Tableau Prep Workspace.pdf]]
[[Flow Pane Steps.pdf]]


#### Summary
Great work! You’ve connected to data in Tableau Prep, added a step to the flow, and got oriented to using the workspace. Keep your flow open so you can use it in the second hands-on activity.

In the upcoming lessons, we’ll work in the profile pane to clean the data.


## Cleaning the data
### Edit data values
Now that we have connected to data and are oriented in the Tableau Prep Builder workspace, we are ready to start taking a closer look at the data and start cleaning it.








### Try it! Edit your data by grouping values

## Outputting and using the cleaned data
### Output the cleaned data
### Try it! Output your cleaned data
### Use the output file as a data source and keep it fresh












> [!example|callout_purple_notepad] Question #1 Response:
> Text here


> [!example|callout_blue_notepad] Read more: 
> Text here


> [!example|callout_quote] Quote
> Text here


> [!example|callout_tip] Tip:
> Text here



```button
name Open aggregation_granularity_and_ratio_calculations.zip
type link
action file:////Users/rachel/Library/CloudStorage/SynologyDrive-SharkologyDC/GitHub Repos/Data-Science-Classes/Tableau eLearning/downloadable data/aggregation_granularity_and_ratio_calculations.zip
color blue
```


`BUTTON[previous, next]`
