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
label: "Next: Part 2: Stepping through the Workflow"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Stepping Through the Workflow]]"

```
```meta-bind-button
label: "Previous: Get Started with Tableau Prep Builder"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Get Started with Tableau Prep Builder]]"

```
# Introduction to Tableau Prep Builder
---
## Data Preparation within your workflow
### How data preparation supports analysis

Data preparation is the process of manipulating data into a form for further analysis. This manipulation includes cleaning, shaping, or combining it with other data sources. Regardless of its source, most data needs cleaning and shaping to optimize it for analysis.

#### The benefits of clean, prepared data

**More insightful, data-driven decisions**
Data that needs cleaning and shaping can hinder or even block your exploration. Clean data enables more accurate analysis which leads to more insightful, data-driven decisions.

**Easier for others to perform their analysis**
Factors like human error, disparate systems, and changing business requirements can contribute to dirty data, but data prep often necessitates more than just cleaning steps. You may need to adjust the granularity of the data or transform it to align and then union or join with other data. This means the data ready for analysis often looks very different from the original data source. 

If preparing data for others, reshape and combine data based on audience needs. Then it will be easier for others to perform their analysis which will lead to faster insights.

#### The analytics process
Tableau was founded on the idea that data preparation, analysis, and visualization should not be isolated activities but integrated parts of an analytics cycle. 

Usually, the goal of the analytics process is to answer important questions using data. You may have your own questions about data. Or, someone at your organization may have questions about data that they want you to answer. 

The process often starts with a task or question, but that might vary. The analytics cycle shows typical tasks that are done when answering questions using data.

![[Pjw5XMkqBZzPstgg_Cr-nxsC0p2JcpDPP.png]]

**Iterative and non-linear**
The analytics cycle is not a linear progression from one stage to the next. It may occasionally work that way, but in general the process is iterative. You can jump back and forth among the stages in the cycle. For example, your exploration of the initial question may lead to follow-up questions, and your exploration of the data may lead you to other lines of questioning within the same data set.

#### Data preparation within the analytics cycle
Data preparation does not just happen once. You may return to data prep again and again during your process of answering questions about your data. 

For example:

- In many cases, data preparation is driven by a specific question. The question often prompts you to find and prepare data in order to determine an answer.
- As you create visualizations to answer your question, you may decide you need to find more data to add to the analysis, which can lead to more data preparation and cleanup.
- Follow-up questions may require additional data that needs to be cleaned and combined.

## Why use Tableau Prep Builder?

### The benefits of using Tableau Prep Builder
Tableau Prep Builder is a visual data preparation tool. Tableau Prep Builder empowers you to get to your analysis faster by helping you quickly and confidently combine, shape, and clean your data.

Using Tableau Prep Builder, you can:
- Connect to data from multiple data sources.
- Clean your data using familiar operations such as filter, split, and rename.
- Edit values directly on rows of data.
- Combine data sources using unions and joins.
- Shape your data using pivots and aggregations.
- Create an output of your cleaned data for analysis in Tableau Desktop or Tableau Server/Cloud.
- Output your cleaned data as a new table, or adding to or replacing data in an existing table. You can output your prepared data in several formats, including a Tableau extract (.hyper) file, a text (.csv) file, or an external relational database.

This brief, one-minute video introduces Tableau Prep Builder's visual interface for building data flows to examine and clean data, review changes, combine data, and export the prepared data.

![[NWHyeHwoag_cGNyn_transcoded-w9BuJld0_ASLJMwP-Welcome to Tableau Prep Builder edited.mp4]]
***Brief introductory video showing Tableau Prep Builder's visual interface for preparing data. (Audio is background music only.)***

#### Key advantages of Tableau Prep Builder
Tableau Prep changes the way traditional data prep is performed in an organization. What features enable this change?

**Visual and direct**
Tableau Prep Builder provides a visual and direct way to prep your data.
- Three coordinated views provide a holistic picture of your data which leads to deeper understanding.
- Drag-and-drop functionality requires no scripting or programming.
- Direct and immediate experience helps you instantly see the result of your actions.

**Smart features**
Increase efficiency and productivity by using Tableau Prep Builder’s smart features.
- Fuzzy-match algorithms for common data prep challenges, such as finding and fixing spelling errors.
- One-click operations to do things like remove punctuation and trim spaces.
- Simple and fast operations that, for example, insert reusable flow components to reduce repetitive cleaning tasks.
- Smart SQL pushdown to determine the optimal execution strategy that makes the most of database investments.

**Ability to stay in the flow**
Stay in the flow of your analysis. Tableau Prep Builder enables you to prepare your data and stay within the naturally iterative, non-linear flow of how you work.
- Get up to speed quickly, since the Tableau’s data connectors, calculation language, and governance structure are same as other Tableau products.
- Easily open your flow output in Tableau Desktop or Tableau Server/Cloud to stay in the analytics cycle for faster speed to insights.
- Share flows and flow output to reduce friction and help you bridge the gap between analytics and data preparation.

##### Integrated Tableau Platform
Tableau Prep Builder is integrated with the other Tableau products in the Tableau platform.

In Tableau Prep Builder:
- Output data extract files that can be analyzed in Tableau Desktop and published to Tableau Server/Cloud for use by others.
- Seamlessly preview your cleaning in Tableau Desktop to check your data prep progress.
- Publish Tableau Prep Builder flows to Tableau Server/Cloud so Tableau Prep Conductor (requires the Data Management Add-on) can run them according to a schedule.

![[Screenshot 2025-11-29 at 8.30.10 PM.png]]

**Input Data:**
Input data can be:
- Server-based
- Web data
- Cloud-based
- File-based
- Tableau extract files

**Tableau Prep Builder:**
- Use Tableau Prep Builder on your desktop or in the browser.
- Clean, shape, and combine data.
- Validate/preview data prep in Tableau Desktop.
- Save cleaned and prepared data extracts to a file, publish to Tableau Server/Cloud, or write the output from your flows to an external relational database.
- Save flows or publish to Tableau Server/Cloud.

**Prep Flow Files**
Flow files describe all the steps within a flow and use the following formats:
- Tableau Prep Builder flow (.tfl) file 
- Packaged Tableau Flow (.tflx) file

**Prepared Data Output**
Output your cleaned data as a new table, or adding to or replacing data in an existing table. You can output your prepared data in several formats, including:
- As a Tableau (.hyper) extract file
- As a text (.csv) file
- In an external relational database

**Tableau Desktop**
- Create/save/publish visualizations
- Ad hoc analysis

**Tableau Server/Cloud and Tableau Prep Conductor**
- Create/save/publish visualizations
- Ad hoc analysis
- Run scheduled flows using Prep Conductor

#### When to use Tableau Prep Builder vs. Tableau Desktop
There are several tools you can use to prepare and clean your data, including Tableau Desktop and Tableau Prep Builder.

Fundamentally, Tableau Prep Builder helps you explore, clean, integrate, and reshape data. If your primary goal is to perform one or more of those tasks, that’s a good sign that Tableau Prep Builder is the right solution. Tableau Prep Builder is a tool optimized for data preparation with more advanced capabilities.

When your primary goal isn’t to explore, clean, integrate, or reshape data, remember that all the data preparation abilities of Tableau Desktop still exist. If a combination of the data interpreter, a pivot, or joins and unions gets your data into the form you need, use Tableau Desktop.

**Tableau Prep Builder:**
Preferred option for data preparation when consistency and repeatability is a requirement and there are dedicated user roles responsible for curating data for others to use. 

Tableau Prep Builder also offers more sophisticated data preparation capabilities beyond Tableau Desktop when advanced transformations are required.

Best choice for when data needs to be cleaned and combined, when you need to do multiple reshaping, combining or cleaning operations to build a data source.

Tableau Prep Builder allows you to profile and explore your data before analysis.

**Tableau Desktop:**
Tableau Desktop is a good data prep option when you are already using Tableau Desktop for analysis and content creation and you only need simple data preparation operations.

#### Why not both?
Interested in more details with examples? Jake Kinstler, a Tableau Product Consultant wrote a blog titled "[Should I use Tableau Prep or Desktop for data prep? The answer: Why not both?](https://tabsoft.co/dataprepwhynotboth)" which presents his guidelines of when each product is useful for data prep.



### Common use cases
Who is Tableau Prep Builder for? When is Tableau Prep Builder best used? Read on to find out.

#### User roles
Tableau Prep Builder efficiently helps users who fulfill many different roles. What kind of tasks do people in the following user roles perform?

**Author/Business User:** Creates visualizations and dashboards to make smarter business decisions.

**Analyst:** Presents data insights across lines of business to improve decision-making.

**Data Steward:** Curates and prepares data sources for the wider organization.

**Data Scientist:** Expertly derives valuable insights for large and varied data sets.

#### Common use cases
How would someone in these roles use Tableau Prep Builder?

**Author/Business User:** 
Uses Tableau Prep Builder’s visual and direct interface to manipulate data into the form desired to answer their own analysis questions.

*Example*: An author/business user combines data sources, creates calculations, and performs multiple pivots for survey data.

**Analyst:**
Uses Tableau Prep Builder’s visual and direct interface to reshape data to avoid complex table or LOD (level of detail) calculations in Tableau Desktop for themselves or others, then publishes their flows to run on a schedule using Tableau Prep Conductor. 

*Example*: An analyst calculates multiple aggregates for monthly or weekly summaries.

**Data Steward:**
Uses Tableau Prep Builder to clean data using smart algorithms and to prepare data for others, by adding business rules in calculations, combining, and shaping data, and then publishing curated data sources for the wider organization. 

*Example*: A data steward integrates current and historical data, cleans it and adds calculations and then shares the data source with the finance department.

**Data Scientist:** 
Uses Tableau Prep Builder to explore data visually and get data ready for their analysis while integrating more complex cleaning, machine learning and predictive modeling using Python/R scripts.

*Example*: A data scientist uses a Python script to add a predictive maintenance cost for a manufacturer's supply chain.


#### Typical scenarios
There are many scenarios when Tableau Prep Builder can be used.

##### Cleaning up messy or dirty data
Messy or "dirty" data, which is data that is poorly structured, incomplete, full of inaccuracies or inconsistencies, leads to inefficient or invalid analyses.

##### Making analysis easier for others
By taking care of more complex data shaping and combining in Tableau Prep Builder, analytics in Tableau Desktop or Tableau Server/Cloud will be simpler for others. For example, creating multiple data extract outputs can be useful if you are preparing the same data, but for different audiences.



`BUTTON[previous, next]`
