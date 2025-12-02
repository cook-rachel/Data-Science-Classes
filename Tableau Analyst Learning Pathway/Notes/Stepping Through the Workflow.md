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

#### Examine the data
Examining the data is the first step in the cleaning process. Watch this short video to see how to examine the donations data in Tableau Prep Builder using the profile pane and the data grid.

![[gmId_wJzsZVa5FZR_transcoded-VwM2mpJ1Lo_xM1eh-Cleaning_Examining.mp4]]
***Examining in the data***

#### Clean data values
Now that we have examined the data in Tableau Prep Builder, we are ready to perform some cleaning. 

Watch this short video to see how to clean the donations data in Tableau Prep Builder by typing to edit one of the **Donor Potential** values.

![[GgrEQgUq0Nlv3PTW_transcoded-u9kvwHn6GRW5YmMB-Cleaning.mp4]]
***Cleaning the data values using direct typing***

> [!example|callout_tip] Tip:
> - Previewing in Tableau Desktop is not available when using Prep Builder on the web.
> - When we clean a field value in Tableau Prep Builder, the changes are applied to all instances of the value in that field.


#### Save the flow
After cleaning your data, you save the changes in a flow file. This saves all the steps in the flow pane so that you can edit or share them later. 

The process of saving your flow varies depending on whether you are using Tableau Prep Builder on your desktop or on the web.

**Prep on the Desktop:**
1. Click the **Save** button or on the **File** menu click **Save As** and browse to a preferred location. By default, Tableau Prep Builder saves the file in the **My Tableau Prep Repository** folder, in **Flows** (but you can change it).
2. Name the flow with a meaningful name. For this flow, type: **Donation Data Cleaned.**
3. Select the flow file type. In this case, we will save the file as a packaged flow, a .tflx file, which will include the local .csv data source file in the saved flow file.
4. Click **Save**.
![[pFLRf-QMN3UWQNYJ_ZS-qKADP7YKE1w3E.gif]]


**Prep on the Web:**
1. Flows are saved automatically on the web, but you can also save using the **File** menu **Save Draft** option.
2. Double click to name the flow with a meaningful name. For this flow, type: **Donation Data Cleaned**.
![[p1B5w7uZfMlyTWm6_vtJHjlACFGPQ4vgO.gif]]

#### Summary
In this lesson, you've learned how to examine the donation data in Tableau Prep Builder, how to use direct typing to edit a value, and how to save a flow file.

In the activity that follows, you’ll use other options to group values to do more data cleaning. These options give you more specific control over what’s in a group.

### Try it! Edit your data by grouping values

We’ve explored cleaning data by editing values with Tableau. Here’s your opportunity to apply your knowledge by editing data values using group values options.

#### Hands-on activity
You will need Tableau Prep Builder on the desktop or on the web for this hands-on activity. If you do not already have Tableau Prep Builder installed, you may purchase it or download a free trial version from the following locations:

- [Tableau Prep Builder](https://tabsoft.co/2PWTl8r)[](http://tabsoft.co/2qTFJ1H)

Note: The free trial is available for a limited number of days.

Now that you have connected to your data about donations made to a non-profit company, you are ready to start your own cleaning. 

To edit the values under **Donor Potential**, you’ll use two different options for grouping values: **Manual Selection** and **Pronunciation**. 

In the demonstration in the previous lesson, we showed the direct typing method to change the **Med** value of **Donor Potential**. Here you will have the opportunity to try different methods.

Good luck!

![[LW6ZYVFoJNUeTQoL_N2DtqkPxtltySxRB.jpg]]
***Final view when the steps have been completed***

In this activity, you can keep working in the flow you created in the first activity, or download and open the starter flow file (available when using Prep on the desktop only).

**Optional**: Download the **file** below to use with this activity.

```button
name Open Donation Data Starter.tflx
type link
action file:////Users/rachel/Library/CloudStorage/SynologyDrive-SharkologyDC/GitHub Repos/Data-Science-Classes/Tableau eLearning/downloadable data/Donation Data Starter.tflx
color blue
```

Follow the steps below to complete this activity:
1. Keep working in the flow you created in the first activity, or open the starter flow file (available when using Prep on the desktop only), then select the **Clean 1** step.
	Expected result:
	![[wUjlAe6LdoDE7RM__x_yj9OlIuUHa57qB.jpg]]
	Hint:
	If you are using the starter file or have closed the saved flow from the previous activity:
	1. From the **Start** page, click **Open a Flow**.
	2. Navigate to the starter file or your saved flow and click **Open**.
	In the flow pane:
	- Click the **Clean 1** step.
	
2. Change the **Donor Potential** value of “Med” to “Medium”, using **Group Values by Manual Selection** then close the **Group Values** editor.  **Manual Selection** allows you to select values to be included in a group.
	Expected result:
	![[WTzG9IlxraaDfGNe_enaBsJbJUkysQog-.png]]
	Hint:
	1. Hover over the **Donor Potential** field header in the profile pane, click **. . .** to open the **More Options** context menu, point to **Group Values**, and click **Manual Selection**.
	2. In the **Group Values** editor, in the list under **Donor Potential**, click **Medium**.  In the column on the right, **Medium** is the selected value, and other available values for grouping appear below it.  
	3. In the column on the right, select the check box next to **Med**.
	4. In the **Group Values** editor, both the **Medium** and **Med** spelling are selected at the top on the right, showing as the two members of the **Medium** group.
	5. Click **Done** to close the **Group Values** editor. 
	A paperclip indicating the new group shows next to the value of **Medium** and in the **Donor Potential** field header in the profile pane, and above the cleaning step.
	
3. To group the **Donor Potential** values that sound alike, use **Group Values by Pronunciation**, then leave the **Group Values** editor open. Because the other values we want to clean sound the same when spoken, we can use the **Pronunciation** option to group them.
	Expected result:
	![[XW7tLdZu6MuAn7DO_QuaDXiHoJMY1bDBY.png]]
	Hint:
	1. Display the context menu in the **Donor Potential** column, point to **Group Values**, and click **Pronunciation**. This creates two new groups. The names of your groups may vary from the animation shown.
	2. Leave the **Group Values** editor open.
	![[YYLdxH3JHM0_sAx9_MB9JYr18TtQjP6-k.gif]]


4. Within the **Group Values** editor, click each new group to view the values within it, then leave the **Group Values** editor open.  It’s good practice to look at what is in a newly created group, to verify that the results are what you intended. Whenever a group doesn't contain the members you want, you can use the check boxes to correct it.
	Expected result:
	![[PT5xB8EVcrNXAuwP_uSleFiJsoUv7N63A.jpg]]
	Hint:
	1. Within the **Group Values** editor, click the first grouped value. On the right, we see that the group contains both the **Hi** and **High** values. That’s what we wanted. Note: The name of your group may vary from the animation shown.
	2. Click the second grouped value, and review its members. These should be both **Lo** and **Low**. Note: The name of your group may vary from the animation shown.
	3. Leave the **Group Values** editor open.
	![[AQVnA1R4it0oZIlH_efjgzER2yCoeFlor.gif]]


5. If your groups are named **Hi** and **Lo**, use direct typing to change the “Hi” and “Lo” group values to use the more conventional spellings: **High** and **Low**, then close the **Group Values** editor.
	Expected result:
	![[PEtY_Kmk-8WXo-Lg_Hm4Fw2LjrfafsSTJ.jpg]]
	Hint:
	1. In the **Group Values** editor, double-click the **Hi** group value, type **High**, and press **Enter**.
	2. Double-click the **Lo** group value, type **Low**, and press **Enter**.  
    Now the group names are **High** and **Low**.
	3. Click **Done** to close the **Group Values** editor.
	You have fixed all the inconsistent values for **Donor Potential**.


6. Expand the **Changes** pane to review the cleaning operations.
	Expected result:
	![[XDOQKPZpNpgF02qV_7qBFmV7qO-plKzPo.png]]
	Hint:
	- Click the **Changes** arrow to display the **Changes** pane. You’ll see two operations.

7. Rename the cleaning step to: **Clean Donor Potential**.
	Expected result:
	![[8NgHWefaIQBW9zrV_dyBx3hDtDtarDcGT.png]]
	Hint:
	1. Right-click the **Clean 1** step and click **Rename**.
	2. Type **Clean Donor Potential** and press **Enter**.
	Note: If you inadvertently close the profile pane, click the cleaning step in the flow.


8. Save the flow file with a descriptive name, for example, **Donation Data Cleaned**.
	Expected result:
	![[awKLpZQYChzkXxAv_DBwj0bJBPtvudLOi.jpg]]
	Hint:
	1. Click **File**, **Save As**.
	2. Type in a descriptive name, for example, **Donation Data Cleaned**.
	3. If you started using your flow file from the first activity, then select **Packaged Tableau Flow Files (* .tflx)** as the **Save as** **type**.  If you started the activity by opening the starter file, the **Save as** **type** will default to the save type as a packaged flow file, or .tflx file. Keep that as the file type.
	4. Save the file in a place of your choice.


Great work! You’ve cleaned the donations data by editing **Donor Potential** data values using group values options. To complete this activity, use your work to answer the following question.




## Outputting and using the cleaned data
### Output the cleaned data
We can use Tableau Prep Builder to perform more preparation steps, such as reshaping and combining your data, but this non-profit data has all the changes we want to make for our analysis and is ready for outputting.

The flow file describes all the preparation steps we have performed on the data, but the actual cleaned, prepared data is contained in the flow _output_.

Watch this short video to see a demonstration of outputting the prepared donations data using Tableau Prep Builder on the desktop. After the video, we’ll see how this differs using Tableau Prep Builder on the web.

![[g0LwauHnwiU-fCUl_transcoded-OrilaKnFG795U4oj-Outputting Data.mp4]]
***Output the prepared data***

###### Output options
The output options you can choose depend on whether you are using Tableau Prep Builder on your desktop versus on the web.

**Prep Builder on Desktop**
When using Tableau Prep Builder on the desktop, your choices include the following output types:
- A file, such as a Tableau Data Extract (.hyper), Comma Separated Values (.csv), or Microsoft Excel (.xlsx) file.
- A published data source
- An external database table

**Prep Builder on Web**
When using Tableau Prep Builder on the web, your choices include the following output types:
- A published data source
- An external database table

**Output the data on the web**
Before you can run your flow on the web to output the cleaned data, you must first _publish_ your flow. 

After publishing, you can run the flow on the web to output the data. If you have the Data Management Add-on, you can also use Tableau Prep Conductor to run published flows on a schedule. 

_Note: The animation below has no audio._
![[APaRLDdbb6FmDwcu_2OJSEVRXiFYOduRj.gif]]
***On the web, publish and then run the flow.***

#### Summary
In this lesson, you saw a demonstration of how to output the cleaned, prepared data in Tableau Prep Builder. 

In the activity that follows, you’ll output the data that you cleaned in the previous activity.


### Try it! Output your cleaned data
We’ve explored the Tableau Prep Builder workflow, including outputting the data. Here’s your opportunity to apply your knowledge by creating an output step and running your flow to output the cleaned data.

**Hands-on activity**
You will need Tableau Prep Builder on the desktop or on the web for this hands-on activity. If you do not already have Tableau Prep Builder installed, you may purchase it or download a free trial version from the following locations:

- [Tableau Prep Builder](https://tabsoft.co/2PWTl8r)[](http://tabsoft.co/2qTFJ1H)

Note: The free trial is available for a limited number of days.

You’ve created a flow in which you cleaned your data about donations made to a non-profit company. Now, output the cleaned data so it can be used as a data source for analysis.

The final result when the steps have been completed will look different depending on whether you are using Tableau Prep Builder on the desktop versus the web.

**Prep Builder on the Desktop**
![[IdPSx2f_oRyLKLF7_rAu6jNbLkjsyi20b.jpg]]

**Prep Builder on the Web**
![[pFFIiS1aiHE2SQJH_Gc1uBNzjmV_5oDhM.png]]


In this activity, you can keep working in the flow you created in the previous activity, or download and open the starter flow file (available when using Prep on the desktop only).

**Optional**: Download the **file** below to use with this activity.

```button
name Open Donation Data Output Starter.tflx
type link
action file:////Users/rachel/Library/CloudStorage/SynologyDrive-SharkologyDC/GitHub Repos/Data-Science-Classes/Tableau eLearning/downloadable data/Donation Data Output Starter.tflx
color blue
```

Follow the **steps** below to complete this activity.
1. Keep working in the flow you created in the previous activity, or open the starter flow file (available when using Prep on the desktop only), then add an output step to the flow after the **Clean Donor Potential** step.
	Expected result:
	![[Kfm0-t6DlHbMSAbx_2j0eJoYkPKmovG5x.jpg]]
	Hint:
	If you are using the starter file or have closed the saved flow from the previous activity:
		1. From the **Start** page, click **Open a Flow**.
		2. Navigate to the starter file or your saved flow and click **Open**.
	In the flow pane:
		- Click the plus icon next to the **Clean Donor Potential** step, and click **Output**.
	The **Output** pane shows the output settings and a snapshot of your cleaned data, with the output options depending on the Tableau Prep Builder platform.
	![[6uR8SfKuJRcUT_B8_d35tNnZ5dHdu5421.gif]]

2. Configure the output as a .hyper file for Prep on the desktop and as a published data source for Prep on the web with a name of **Output_Donation Data Cleaned**.
	Expected result:
	![[e6VsRHDZF0jbemSA_5GrND__oWC66Y0J4.jpg]]
	Hint:
	1. Under **Save output to**, leave **File** selected.
	2. Click **Browse**.
	3. In the **Save Extract As** dialog box, confirm the location or navigate to where you want to save the file. 
	4. Next to **File Name**, type **Output_Donation Data Cleaned**.
	5. Leave the **Output type** as **Tableau Data Extract (.hyper)**.
	6. Click **Accept**.
	7. Run the flow to generate the cleaned output data.
	![[ct_EjNO5u08Kbe17_9XicjnrOtFZTFYO_.gif]]

3. Run the flow to generate the cleaned output data.
	Expected result:
	![[3LEATw_YcEhfXYeg_DwjaOxPqTjkD3rbp.jpg]]
	Hint:
	1. Click **Run Flow**, at the bottom of the **Output** pane. A small window appears as the flow is running.
	2. When the flow is finished, click **Done** in the **Finished Running Flow** dialog box.
	You now have an output file of the cleaned data, which you could use as a data source for your analysis.
	![[t48rmeETRb690c-Z_4zYwell3qtfZU8Ga.gif]]


Great work! You’ve created an output step and run your flow to output the cleaned data. To complete this activity, answer the following question.


### Use the output file as a data source and keep it fresh
Once the cleaned data has been output, you can use it in your analysis. This lesson will walk through the steps of how to use the cleaned output data in a visualization, summarize the data preparation process in Tableau Prep Builder, and then describe how to keep the cleaned output current.

**Connecting to cleaned output and creating a visualization** 
Watch this short video to see a demonstration of how to use the cleaned data as a data source file and create a visualization about donor potential. The video shows the steps in Tableau Desktop; however, if you are creating your visualization on the web, the cleaned output that you connect to will be a Tableau published data source.  Note that outputs from Prep Builder on the web can also be published as database tables.

![[Qbb7p5WFBrArSQ8F_transcoded-svBW0Jlv-Za3F0gg-Using the Output File.mp4]]
***Creating a visualization with the cleaned data output***

**Recap of the Tableau Prep Builder workflow**
We've now performed the three steps in the Prep Builder workflow (connect, clean, and output) using the donations data. 

Watch this short video to see a recap of this workflow. This video uses Tableau Prep Builder on the desktop, but the process is similar when using Prep Builder on the web.

![[ueEqkIuelmth5Xie_transcoded--PY8M9iRqHIstcpE-Workflow summary.mp4]]
***Creating a visualization with the cleaned data output***

**Keeping everything fresh**

Now that you know how to use cleaned output for your analysis, how can you maintain your flow and cleaned data? To do so:
- Publish the flow.    
- Edit the flow when necessary.
- Update the cleaned data as needed.

**Publishing a flow**
You have already seen how to publish a flow when working in Tableau Prep Builder on the web. With the Creator license type and the appropriate permissions, you can also publish flows from Tableau Prep Builder on the desktop to a Tableau site. Publishing your flow makes your flow available so users with appropriate permissions can edit the flow and create their own flow outputs, for example, with a subset of the data for their department.

First, sign into your Tableau site from Tableau Prep Builder on the desktop using the **Sign in** option on the **Server** menu, and then follow the prompts. 

After signing in to your Tableau site from Tableau Prep Builder on the desktop, select **Publish Flow** from the **Server** menu.

![[qCnEOsrviVxqJZP2_bDjGAh1EoiJjVBSj.png]]

In the dialog box, fill in the destination project, name of the flow, and description and tags, if desired, then click **Publish**.

![[gp-JRowkg4fd0o7s_938sVUa53ZTJ7XDL.png]]

**Editing a flow**
Sometimes in order to keep your data fresh, you need to edit your flow. Perhaps you have determined that you need to perform more cleaning or additional shaping and combining operations, such as a union with donation data from another region. You can edit the flow from either Tableau Prep Builder environment.

**Prep Builder on the Desktop**
To edit a flow in Prep Builder on the desktop:
1. Open the flow from the **Start** page.
2. Edit the flow, as needed.

![[t0n_akAYjapjt5Zc_6QlW4pd4W6vsWbPg.jpg]]

Once you have made the desired edits to your flow, republish it using the process for the appropriate environment, as previously described.  

**Updating the cleaned data**
Once you generate your flow output as a cleaned data source, you need to keep it fresh by updating your output when the data changes. The way to generate updated output is to run the flow.

You can run your flow manually, from Tableau Prep Builder on the desktop or from the flow page or the **Explore** page on your Tableau site, as you have already seen in this module.

Alternatively, after you publish a flow to your Tableau site, you can run it on a schedule to refresh the flow output. To automatically run flows on a schedule, you must have Tableau Prep Conductor, a component of the Data Management Add-on, enabled. Tasks can be created to schedule flow runs on particular days and times and can be single tasks or linked together, if you have flows that are interdependent. From the **Scheduled Tasks** tab on the flow’s page, you can see whether the flow run succeeded and the date/times of the last and next scheduled runs.

_Note: The animation below has no audio._
![[3t_TlniVY3eiJ9Gd_9lA2_jkHIacfscSU.gif]]

From Prep Builder on the desktop or on the web, you can also configure your flow inputs and outputs to refresh incrementally so that only the new rows are retrieved and processed when the flow runs, saving you time and resources.

**Summary**
In this lesson, you saw a recap of the data preparation process in Tableau Prep Builder and learned how to use the cleaned output data in a visualization and how to keep the flow and cleaned output up to date.

**Module Summary**
In this module, you learned at a high level how to use Tableau Prep Builder from start to finish, including connecting to data, cleaning data, running the flow, and saving the output. Then you learned how to use the cleaned data in your analysis and how to keep it fresh to make sure your analysis reflects the latest information you need.

Now that you have an understanding of the high-level tasks, you are ready to apply them to your own data, or take additional modules to dive deeper into Tableau Prep Builder capabilities.




`BUTTON[previous, next]`
