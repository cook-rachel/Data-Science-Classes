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
label: "Next: Get Started with Tableau Prep Builder"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Get Started with Tableau Prep Builder]]"

```
```meta-bind-button
label: "Previous: Get Started with Tableau Desktop"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Get Started with Tableau Desktop]]"

```
# Introduction to Tableau Desktop
---
## The Tableau desktop workflow
### Explore the workflow
You have data and you want to explore it. How do you do that using Tableau Desktop?

To get a picture of the workflow for exploring data in Tableau Desktop, watch this five-minute video.

![[J0n-_g1ATWDDhkTp_transcoded-9mG1YFDsLin_B8WN-Combined conceptual slides.mp4]]
***The Tableau Desktop workflow***


> [!example|callout_tip] Tip:
> Tableau Online is now known as Tableau Cloud

#### Following an iterative workflow
The general workflow of connect, analyze, and share is flexible. As you become a more advanced user, your workflow becomes less linear and more iterative. 

You might add more connections to a data source, or decide to start over using a different data set or a different question. That is what Tableau Desktop is made to do: help you make discoveries, change direction, and build as needed.

![[Screenshot 2025-11-29 at 6.05.53 PM.png]]

**Connect and then analyze**: Once you have connected to data, you can start to analyze it

**Analyze and then share:** Once you have analyzed your data, share your insights with others in a dashboard or a story.

**Share and then connect:** While sharing your insights, you might realize that you need more data to help others understand you analysis or provide more context.

**Share and then analyze:** When you are sharing your insights, perhaps you or one of your colleagues has thought of another line or inquiry to pursue.

**Analyze and then connect to more data:** While answering some of your questions, you might realize that you need more data to complete your analysis. 


## Connecting to your data
### How to make your first data connection
Now that you have a sense of the Tableau Desktop workflow, let’s look in more detail about the first part: connecting to data.

#### Connect to a local file
To see how to connect to a local data source, view this short video. This demo uses the **Sample-Superstore** data that is included with your Tableau Desktop installation.

![[zPuHElibJcHKTUfA_transcoded-zdn_uRjMXOtiwjdb-Updated_Connect_Slide 3.mp4]]
***Connecting to a data source***

As you saw in the video above, Tableau opens on the **Start** page, which includes three main areas, **Connect**, **Open**, and **Discover**.

![[Screenshot 2025-11-29 at 6.45.31 PM.png]]

**Connect:** In the *connect* area you'll find the list of data source types you can connect to.

**File-based data sources:** Tableau can work with file-based data including: Excel spreadsheets, CSV files, PDFs, spatial files, such as Shapefiles and GeoJSON files; and statistical files, such as SAS, SPSS, and R data files.

**Server-based data sources:** Tableau can connect to database servers, including relational databases, cube databases or sources, and cloud data.

**Saved data sources:** Tableau can connect to saved data sources automatically installed as well as those that are user created.

**Open:** In the *Open* area you’ll find thumbnail images and links of your recently used or favorite saved visualizations, known as workbooks, and a link to browse for other workbooks. Below that, you find the *Sample Workbooks* included with Tableau Desktop. These are great examples of dashboards and the range of views you might build with your data.

**Start page:** Tableau opens on the *Start* page, which includes three main areas: *connect*, *open*, and *Discover*

**Discover:** In the *Discover* area you’ll find links to important training information like free videos as well as sign-ups for free live sessions. The Tableau blog and forums are especially valuable resources, offering informational demos and access to the Tableau community. The content in this area changes based on your Tableau product version.


#### Select and preview your data
Once you have connected to a data source, you need to select a specific sheet or table. In the short video below, learn the steps for selecting the sheets or tables you want to work with.

![[hxaXJmgTi03jxw4Q_transcoded-G3uo1ox7LH5Vmn88-Updated_Connect_Slide 4.mp4]]
***Selecting and previewing tables and sheets on the Data Source Page***

As you saw in the video above, the **Data Source** page contains a few key areas. Use the matching activity below to check your understanding of what each area contains.

#### What's next?
We’ve looked at data connection options, connected to a Microsoft Excel data source, previewed the data, and opened a new worksheet. 

Next, try this yourself. In the activity that follows this demo, you’ll connect to a data source file to practice the initial step in the Tableau Desktop workflow.


### Try it! Connect to and preview your data

We’ve explored the first part of the Tableau Desktop workflow, connecting to data. 

Here’s your opportunity to apply your knowledge by connecting to and previewing a local data file.

#### Hands-on activity
You will need Tableau Desktop for this hands-on activity. If you do not already have Tableau Desktop installed, [purchase it or download a free trial version](http://tabsoft.co/2qTFJ1H) now.

Note: The free trial is available for a limited number of days.

Imagine you’re studying data about library usage and costs worldwide. 

As the first step in the Tableau Desktop workflow, you need to connect to your data source, a Microsoft Excel file, using Tableau Desktop. You’ll do that in this activity. Note that you do not need to have Microsoft Excel installed to use this activity file.

Good luck!

```button
name Open Global Library Data.xlsx
type link
action file:////Users/rachel/Library/CloudStorage/SynologyDrive-SharkologyDC/GitHub Repos/Data-Science-Classes/Tableau eLearning/downloadable data/Global Library Data.xlsx
color blue
```

Follow the steps below to complete this activity.

1. Connect to the Microsoft Excel file, Global Library Data.xlsx
	Expected result: 
	You should see the **Data Source** page after completing this step.
	
	![[Tableau Analyst Learning Pathway/images/sxTCiBDYGCBNQMBx_pEBjsTfexVcdf2SB.png]]
	Hint: 
	1. On the **Start** page, under **Connect**, **To a File**, click **Microsoft** **Excel**.
	2. In the **Open** dialog box, navigate to where you saved the **Global Library Data.xlsx** practice file.
	3. Select Global Library Data.xlsx and click **Open**.
	
2. On the **Data Source** page, add the **Country Data** sheet to the canvas.
	Expected result:
	![[Tableau Analyst Learning Pathway/images/EzhLw6UxWDj-tegG_xdrpgKNoVysUUvYB.jpg]]
	Hint: 
	Under **Sheets**, drag the **Country Data** sheet to the canvas (where it says, “**Drag tables here**”) OR double-click the **Country Data** sheet.

3. Examine the previewed data to answer the following question.
	How many fields are in this data source?
	a. Five
	b. Six
	c. Seven
	d. Eight
	
4. Open a new worksheet to get ready to analyze your data, which you will do in the next hands-on activity in this module.
	Expected result: You'll see your data in the workspace and also the name of the data source.
	![[Tableau Analyst Learning Pathway/images/EzhLw6UxWDj-tegG_xdrpgKNoVysUUvYB.jpg]]
	Hint:
	1. Click the **Sheet 1** tab at the bottom left of the window to open a new worksheet.
	2. This opens the Tableau Desktop workspace.
	
5. (Optional) Save the file.
	Expected result:
	![[Tableau Analyst Learning Pathway/images/XDAyUUVsQDMnTCuI_J_6FLgMrkYs0hhOe.png]]
	Hint: 
	1. If you would like to save this file to use it for the other activities in this module, then on the **File** menu, click **Save**.  
	      Note: The first time you save a workbook, Tableau Desktop defaults to the **My Tableau Repository\Workbooks** folder.  
	      To save it elsewhere, browse to the desired location.
	2. Give the workbook a name of your choice, such as "Global Library Data."
	3. Click **Save**.
	
Great work! You connected to a local spreadsheet and loaded your data.


## Analyzing your data
### Analyze data by building views
Let's get back to our **Sample-Superstore** data.

Now that we have connected to the data, we have some questions that we want to answer. For example, how are our product categories performing across all regions? To explore that kind of question, we'll look at how to analyze data in the Tableau Desktop workspace.

In this lesson, we'll look at the second part of the Tableau Desktop workflow: analyzing data.

#### Workspace essentials in Tableau Desktop
In this short video, discover the essential areas of the Tableau Desktop workspace. This demo uses the **Sample-Superstore** data that is included with your Tableau Desktop installation.

![[BMkz6swc9cKPdWMM_transcoded-6OdomTqIflQIKfFJ-Updated_ITD_Analyze_Slide 2.mp4]]
***Essentials of the Tableau Desktop workspace.***

#### Analyze data in a bar chart
We would like to answer a few questions about our retail data:
- How do sales compare among product categories? 
- Which product categories are the most and least profitable?

In this short video, see how to build a bar chart that helps us find these answers.
![[uT9PiS8u5uckBI6K_transcoded-tbbmTNc3YTN4L_t0-Updated_ITD_Analyze_slide 3_4.mp4]]
***Create a bar chart to compare sales across product categories.***

#### Analyze data in a crosstab (text table)
As we discussed in the Tableau Desktop workflow lesson, in an iterative analysis, initial questions often lead to more questions. In our example, we now have a few more questions about our retail data:

- What are the detailed profit and sales numbers within the least profitable category? 
- Which product subcategories were the least profitable? 

In this short video, see how to create a crosstab, also known as a text table, that helps us answer these questions.

![[GhDMk6kDBQ0hxT9Y_transcoded-tb3q_-aGJQD3awjK-Updated_ITD_Analyze_slide 5.mp4]]
***Create a crosstab to compare profit and sales numbers side by side.***

#### Use the areas of the workspace to build views
As you saw in the videos above, the Tableau Desktop workspace contains several different areas that you use to build visualizations. Deepen your understanding by exploring the areas in the image below.

![[Screenshot 2025-11-29 at 7.09.15 PM.png]]

**Data Pane:** The *Date* pane lists all the fields from the source data.

**Data source:** The name of the data source connection, for example, the *Orders* sheet in *Sample-Superstore*, is listed near the *Data* pane tab.

**Dimensions:** Dimensions are fields that contain qualitative or categorical data for example, *City* and *Product Name*. Dimsensions slice our data into categories to show different details.

**Measures:** Measures contain quantifiable data, which consists of numerical values, for example, *Discount* and *Quantity*. When building a viz, you'll analyze aggregated measure values according to specific dimension categories.

**Filters:** *Filters* allow you to include and exclude specific data. The different types of filters will be covered in detail in other lessons.

**Marks card:** The *Marks* card is used to set different properties for fields in the visualization. As you drag fields to different properties on the *Marks* card, you add more information to the view. You use the *Marks* card to set the mark type and to encode your data in the view with color, size, shape, text, and other properties that add context, detail, and meaning to the marks in the view. 

**Columns and Rows:** The *Columns* and *Rows* shelves are used to create a structure for your visualization. You can place any number of fields on these shelves.

**View:** The view shows your visualization. To start creating a view from a tabular perspective, you can drop a field to any areas labeled *Drop field here*.

#### Use Show Me to build views
What if you don't know what kind of chart to make for a question you have? To see how to use **Show Me** to build views, watch this short video.

![[Fzo055r8sP3unIOQ_transcoded-yKLycu4UfR85EBVl-Updated_ITD_Analyze_slide 6.mp4]]
***Use Show Me when you want suggestions for which type of chart to build. ***

In the videos above, you've seen how you can build visualizations in several different ways, including:

- Dragging or double-clicking to put fields on **Rows** or **Columns.**
- Dragging fields to the **Marks** card.
- Dragging fields to the view.
- Selecting fields and clicking on a chart type in **Show Me.** 

You have also seen how to analyze data in a bar chart or crosstab. To see an example of when each chart type or method would be useful for analyzing your data, try the matching activity below.

#### What's next?
We have shown you how to use the areas of the Tableau Desktop workspace to begin an analysis of the **Sample-Superstore** data by building a bar chart and a crosstab. 

Now you are ready to try your own analysis, building visualizations to explore and answer questions about data. In the activity that follows this lesson, you’ll build a bar chart and a crosstab to answer questions about global library data.


### Try it! Analyze your data using a bar chart and crosstab
We’ve explored the second part of the Tableau Desktop workflow, analyzing data. Here’s your opportunity to apply your knowledge by analyzing the **Global Library** data set.

#### Hands-on activity
You will need Tableau Desktop for this hands-on activity. If you do not already have Tableau Desktop installed, [purchase it or download a free trial version](http://tabsoft.co/2qTFJ1H) now.

Note: The free trial is available for a limited number of days.

In the prior activity you connected to the **Global Library** data source, and now you want to analyze that data to answer these questions: 

- Which region has the fewest libraries? Which has the next fewest?
- Which country has the highest expenditures? Which country has the highest total users?

To find those answers, build two different views for analysis in Tableau Desktop: a bar chart and crosstab. Use the bar chart to compare the number of total libraries in the different regions. Then use the crosstab to see specific values for each country.

For this activity, you may use the Tableau workbook you saved in the first _Try it!_ lesson in this module. Or, download the starter activity file before you begin.

Good luck!


```button
name Open Analyze data in two views_starter.twbx
type link
action file:////Users/rachel/Library/CloudStorage/SynologyDrive-SharkologyDC/GitHub Repos/Data-Science-Classes/Tableau eLearning/downloadable data/Analyze data in two views_starter.twbx
color blue
```

Follow the steps below to complete this activity.

###### Create and analyze your data in a bar chart.
1. Open the starter file or the Tableau workbook you saved in the first _Try it!_ lesson. 
	For instructions on how to open a .twbx file in Tableau Desktop, see the [_Tableau eLearning User FAQs_](https://tabsoft.co/2LMDN6N)_._

2. Create a horizontal bar chart comparing **Total Libraries** by **Region**.
	Expected result:
	![[pc6Bi6No9JxMSRHS_pfxrPymEKbV018s1.png]]
	Hint:
	1. On the **Sheet 1** tab, drag the **Total Libraries** field to **Columns**.
	2. Drag the **Region** field to **Rows**.
	
3. Sort the view by **Total Libraries**, in descending order, so you can compare the regions. Which region has the fewest libraries? Which has the next fewest?
	Expected result: 
	**Oceania** has the fewest and then the **Middle East.**
	![[PywqFv4E2Q2WII64_5UNSSiUlrXG59LiO.png]]
	Hint:
	Point to the **Total Libraries** header on the x-axis, and click the sort icon to sort the list in descending order (biggest to smallest). This sorts the **Total Libraries** values from highest to lowest.
	
4. To see more details about the data, point to any bar to view its tooltip. Use these details to answer the following question.
	Examining the bar chart you have created, which region has 43,572 libraries, and where does it fall in the order, from highest to lowest?
	![[yTw2ex2X8oZg6IbS_3vI7ijd7YALErFZI.png]]
	a. Latin America, fourth
	b. Africa, fifth
	c. Middle East, sixth
	d. Oceania, seventh
	
5. Give the worksheet a title, “Total Libraries by Region”.
	Expected result:
	![[XZd0QcbKaWr4_f_y_vT9Rnwiqy-1sRRfE.png]]
	Hint:
	At the bottom of the worksheet, double-click the **Sheet 1** tab, and type the name for the view: “Total Libraries by Region”.
	
Great; now move on to the next part of the activity. 

###### Create and analyze your data is a crosstab
Next, you want to find the country with the highest library expenditures and the one with the highest total library users. To compare specific values for each country, you'll build a crosstab.

1. Start a new worksheet for your crosstab.
	Expected result:
	![[25HMcdsgdzz3yc0R_9d2iNlvK6xwlI11w.png]]
	Hint:
	To the right of the **Total Libraries by Region** tab, click the **New Worksheet** tab.
	
2. To start the crosstab, create row headers for each **Country**.
	Expected result:
	![[Sa7i_Rrho8MUVPWz_IeVkAOb5QLKZVFR6.jpg]]
	Hint:
	Drag the **Country** field to **Rows**.
	
3. Add data to the crosstab for the following measures: **Expenditures**, **Total Libraries**, **Total Users**, and **Total Volumes**.
	Expected result:
	![[aYpODgj4esMUfx1q_5JO7O-M5JnvOegJK.png]]
	Hint:
	1. Drag the **Expenditures** field into the view area toward the text column; drop it when you see the column outlined in black, and Tableau Desktop displays “Show Me”.
	2. Drag the **Total Libraries** field into the view to the right of **Expenditures**.  This adds column headers for both.
	3. Drag **Total Users** into the view on the right.
	4. Repeat the previous step with **Total Volumes**.  
      
    You now have four columns of measure data for each country.

	Note: You’ll see that for some countries, certain cells are blank due to lack of information in the original data.

4. Sort the columns to find the country with the most library **Expenditures** and the one with the most **Total Users**. Remember that each sort re-sorts the rest of the table.
	Expected result:
	The **United States** has the highest expenditures and **South Korea** has the highest total users.
	
	Hint:
	1. Point to the **Expenditures (US Dollars)** header at the top of the column, look for the sort icon that appears (it should have bars in descending order), and click it. This sorts every column according to highest to lowest values in the **Expenditures** column.
	2. Similarly, sort the data by **Total Users** in descending order.
	
5. Analyze your data further by sorting the data again and answering the following question.
	Examining the crosstab, which country has the greatest number of **Total Volumes**?
		a. United States
		b. Germany
		c. South Korea
		d. India 
	
6. Name the worksheet “Country Details” and (optionally) save the file.
	Expected result:
	![[cXPabCo9MYm54Ata_fVRXOnD1ErUZW-00.png]]
	Hint:
	1. To name the worksheet, double-click the **Sheet 2** tab, and type “Country Details”.
	2. If you would like to save this file to work with later in the module, then on the **File** menu, click **Save As**.  
	    Note: The first time you save a workbook, Tableau Desktop defaults to the **My Tableau Repository\Workbooks** folder. To save it elsewhere, browse to the desired location.
	3. Alter the workbook name if you wish, and click **Save**.
	

Great work! You've analyzed the **Global Library** data by creating and examining a bar chart and a crosstab.


## Sharing your analysis
### Build a dashboard or story to share insights
Let's get back to our **Sample-Superstore** data. We‘ve been examining the typical workflow in Tableau Desktop. This began with connecting to our data source. Then we started analyzing our data by building visualizations. Now we’re ready to share our views and discoveries with colleagues, to enable _them_ to explore the data as well.  

In this lesson, we'll look in more detail about the third part of the Tableau Desktop workflow: sharing your work with others.

#### Build a dashboard with two views
In the prior demonstration, we showed how to analyze **Sample-Superstore** data by creating a bar chart and a crosstab. We have modified and further refined both the bar chart and crosstab by adding more dimensions so we could analyze the sales and profit for individual products by sub-category.

To see how to build a dashboard to pull these two worksheets together in one place, view this short video.

![[ikZirY4OgVqGj3Dc_transcoded-4tZzwpMGMrqJkXEb-Updated ITD Share_Slide 4.mp4]]
***Creating a dashboard from two previously built views***

We've created a dashboard consisting of two views. We can now make some small adjustments to the dashboard to make it easier for others to use and explore the data on their own.

##### Fine-tune a dashboard
Now that we have our two views in the dashboard, we'll do some fine-tuning before we share it. In this short video, you'll learn how to:

- Adjust the views to fit the dashboard space.
- Apply a filter so users of the dashboard will be able to drill into profit and sales details, according to the product sub-categories they’re interested in.
- Add a dashboard title and instructions for colleagues on how to use it.

![[9c5QBu3UE9VlXC7E_transcoded-KfFSHHPsP1tLdlFT-Updated ITD Share_Slide 5.mp4]]
***Fine-tuning a dashboard and applying some best practices.***

We've applied a filter in our dashboard so the views work together. In addition to using one view in a dashboard as a filter for the other view, there are many more options for filtering your data. For example, you could create a filter to show only the data that meets a certain condition, such as the top 10 products in sales. Learn more in the later module about filtering your data.

##### Save a dashboard
Now that we have fine-tuned our dashboard, we're ready to save it. To look at options for saving workbooks, view this short video.

![[TizJ-2OC_QGjctu0_transcoded-5Z9CIDx7R4MXT7um-Updated ITD Share_Slide 6.mp4]]
***Saving a dashboard as a Tableau workbook or a Tableau packaged workbook***

Learn about publishing workbooks for sharing in our module about sharing your work.

#### Create a story
Dashboards enable you to share multiple views at the same time, informing others and allowing them to explore the data on their own.

But what if you have a particular insight you want to share? Watch this short introduction to learn about using stories in Tableau.

![[Se14kdzshjaEfGgc_transcoded--qoClAuCQRY5M_H9-Updated ITD Stories Concept_Slide 2 and part 3.mp4]]
***Tableau stories and when to use them***

As shown in the video above, a Tableau story consists of visualizations or dashboards used in a sequence to create a narrative about your data. A story is a collection of sheets, so the methods you use to create, name, and manage worksheets and dashboards still apply. Each individual sheet in a story is called a story point.

Create stories to tell a data narrative, provide context, demonstrate how decisions relate to outcomes, or simply make a compelling business case. In a later module, we go into detail about telling stories with data.

#### What's next?
We've shown how to create an interactive dashboard composed of a bar chart and a crosstab to share an analysis of our **Sample-Superstore** data. 

Now you are ready to create your own interactive dashboard to share with others. In the activity that follows this lesson, you’ll build a dashboard from a bar chart and a crosstab for the **Global Library** data.


### Try it! Create an interactive dashboard to share with others
We’ve explored the third part of the Tableau Desktop workflow, sharing our views and discoveries with others. Now it is your turn to apply this new knowledge by creating an interactive dashboard with the views that you have already built to analyze the **Global Library** data set.

#### Hands-on activity
To analyze your global library data, you’ve built two visualizations: a bar chart that shows measure data by region, and a crosstab that shows additional values by country.

Now, create a dashboard with these views for your colleagues. Use the bar chart as a filter to help people explore data for specific regions by countries of interest. 

For this activity, you may use the Tableau workbook with the views that you created in the previous activity. Or you may download the starter activity file before you begin. 

Good luck!

![[l620RaZyZrdkhuZ5_iDLTwzVtnAHEmUMp.png]]
***Final dashboard when the steps have been completed***

**Download** the file below to use this activity. 

```button
name Open Share data in a dashboard_starter.twbx
type link
action file:////Users/rachel/Library/CloudStorage/SynologyDrive-SharkologyDC/GitHub Repos/Data-Science-Classes/Tableau eLearning/downloadable data/Share data in a dashboard_starter.twbx
color blue
```

Follow the **steps** below to complete this activity.
1. Open the starter file or the Tableau workbook you saved in the previous _Try it!_ lesson.  
    For instructions on how to open a .twbx file in Tableau Desktop, see the [_Tableau eLearning User FAQs_](https://tabsoft.co/2LMDN6N)_._

2. Create a dashboard with the **Total Libraries by Region** bar chart on top and the **Country Details** crosstab on the bottom.
	Expected result:
	![[gOIKEJyi1dYSQ1Am_W_JREU9uFXVDClIK.jpg]]
	Hint:
	1. Click the **New Dashboard** tab (along the bottom, to the right of the **New Worksheet** tab).
	2. Under **Sheets**, drag the **Total Libraries by Region** bar chart into the open space on the right.
	3. Drag the **Country Details** crosstab and place it below the bar chart.
	4. Click outside of the dashboard to deselect the view.

3. Adjust the **Country Details** crosstab to fit the width and make the size taller.
	Expected result:
	![[D5p42TYGPkGzMRcw_Pgg6v4UG6xuimM8K.jpg]]
	Hint:
	1. In the dashboard, click the **Country Details** crosstab view to select it.
	2. On the toolbar, open the **Fit** menu, and change it from **Standard** to **Fit Width**.
	3. To make the **Country Details** view slightly taller, point to its top border, and use the sizing arrow to drag the border upward a bit.
	
4. Set the **Total Libraries by Region** bar chart to be used as a filter for the **Country Details** crosstab.
	Expected result:
	![[nxne3bmaZQoExNRX_mSSghmxEHwdtUKpv.jpg]]
	Hint:
	1. Click the **Total Libraries by Region** view to select it. This displays the little context menu on the right. 
	2. In the top right corner, click the **Use as Filter** icon (it looks like a small funnel). When the **Use as Filter** icon is activated, it is filled in.
	3. Test the filter by clicking one of the **Region** bars, such as **Middle East**, and check to see that the **Country Details** view gets filtered to countries in that region.  If all the countries are showing, the filter hasn’t been applied. To apply it, repeat steps 1 and 2.
	
5. Use the bar chart filter and use sorting to determine which country in **Asia** has the highest library **Expenditures**.
	Expected result:
	**Japan** has the highest library expenditures in **Asia**.
	![[lvT0AHbIwOTt9v2g_fhPDeLr0p-1UnvsA.jpg]]
	Hint:
	1. Select **Asia** in the bar chart.
	2. In **Country Details**, the columns are currently sorted by **Total Users**, which was the sort order when the sheet was added to the dashboard. To sort by total expenditures, point to the **Expenditures** column, and sort it “descending” (meaning the values are listed highest to lowest).
	3. The highest number will appear at the top. The corresponding country will be listed on the left for that row.
	4. To return the dashboard to an unfiltered state, either click the selected bar, or click in a white space within the view.
	
6. Explore the data further by answering the following question.
	Which *Latin American* county has the greatest number of *Total Libraries*?
		a. Anguilla
		b. Barbados
		c. Brazil
		d. Mexico
	
7. Title the dashboard and include instructions on how to filter.
	Expected result:
	![[0Xu4M4MfiosvfEaa_OB5F4YIhYYTh2D7r.png]]
	Hint:
	1. Double-click the **Dashboard 1** worksheet tab, and type a title, such as: “Country Details by Region”.
	2. On the **Dashboard** menu, click **Show Title**.  The title now appears, at the top of the dashboard.
	3. To add instructional text for the dashboard, double-click the dashboard title.
	4. In the **Edit Title** dialog box, place your cursor under the Sheet Name title, and type instructions for users, such as: “Click a region to filter the country data”. 
	5. Select this text, and change its point size from **18** to **12**, then click **OK**.
	
8. Save the file as a **packaged workbook (.twbx)**.
	Hint:
	1. On the **File** menu, click **Save As**.
	2. In the **Save As** dialog box, be sure that in **Save as type**, the file type selected is **Tableau Packaged Workbook (.twbx)**.  
	3. If you want to save the starter file with a different name or in a different location, make those changes.
	4. Click **Save**

Great work! Using the **Global Library** data, you created an interactive dashboard that you can share with others for analysis.


#### Module summary
In this module, you explored the key phases of the Tableau Desktop workflow, trying out each part yourself. You connected to the **Global Library** data source and built two types of charts, a bar chart to compare data across regions and a crosstab to see specific values for each country. Then, you used the views in an interactive dashboard to share with others.

Now, use this knowledge to connect to, analyze, and share insights with your own data!



`BUTTON[previous, next]`
