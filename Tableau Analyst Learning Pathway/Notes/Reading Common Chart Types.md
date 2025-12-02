---
tags:
  - datascience
  - notes
  - tableau
university: Tableau eLearning
year: "2025"
link: https://elearning.tableau.com/path/analyst-learning-path
cover: https://elearning.tableau.com/path/analyst-learning-path
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
label: "Next: Get Started with Tableau Desktop"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Get Started with Tableau Desktop]]"

```
```meta-bind-button
label: "Previous: Understanding Basic Data Concepts"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Understanding Basic Data Concepts]]"

```
# Reading Common Chart Types
---
## Why use data visualizations?

### Visualizations help us understand complex data 

The best reason to use a visualization to understand your data is that most data sets are far too large to consume in their raw format. Humans are limited in what information we can process and compare in our heads, especially if that information resides in a million row data set, but we are good at quickly processing visual information. 

Even if you are new to reading data in a chart, you already have the built-in capabilities to spot light and dark colors, large and small shapes, groups and orientations of objects. These are referred to as pre-attentive attributes.


> [!example|callout_quote] Quote
>   
Visual analytics leverages our _pre‑attentive attributes_ – visual cues humans process automatically with sensory memory. 

  

We can notice and interpret these kinds of attributes quickly and without special effort.


Some pre-attentive attributes are better at showing _quantitative_ (measured) data, and some are better at showing _qualitative_ (categorical) data. For example, using length of bars to represent amount of sales is an effective choice to indicate differences in sales across categories.

### Moving beyond spreadsheets

#### Tabular data, plain

![[6bB9CYiLuML_wMKH_GTuILa6o-oqkDgUc.png]]

You are probably familiar with the text table or cross tab. Cross tabs are one of the most common representations of data, and are useful for viewing specific numeric values.

#### Tabular data with values circled

![[G7kG69vfwB04cnqs_uUtR_CpB_xO2G-z9.png]]

If you were viewing this on paper, you might circle or highlight the high and low values so you could find them again quickly.

#### Tabular data with a color for negative values

![[Wk9JlIzcxtF688K9_bfyLhOyJ3jaaIDd7.png]]

Adding color to negative numbers makes them stand out, but only if you’re looking for negative numbers. Otherwise, you need to scan the entire table in order to compare high and low values.

#### Tabular data with sales and profitability by color gradients

![[J3xcl3FMVHeOIzYJ_5H-m9ZiahO7BHy0n.jpg]]

Next, as an intermediate format between a text table and a full visualization, you can use color to show high and low values. 

What if you also wanted to look at sales compared to profit?

#### Visual data by bar length and color

![[Aemi5VE8-ka0emU9_w_H1yWu1AK3sEGYk.png]]

Finally, using a bar chart shows the full visualization with sales by length and profit ratio encoded by color. Immediately, the viewer can see highest sales and lowest profit.

## Overview to reading Charts
You have learned about the advantages of viewing data in a visualization instead of spreadsheet or table, and you are ready to understand more about reading charts.

> [!example|callout_quote] Quote
>   
A well-designed chart should be easy to read and understand, and should not mislead. Here's how to be an educated data consumer.


There are three key components of this lesson:

- **Know what elements make up a chart in Tableau.** This will help you read the views others create.
- **Ask questions about what you see.** Visualizations can be the start of the exploration of your data and will lead to questions - which is a good thing.
- **Watch for misleading charts.** This lesson has a few examples, but there are many ways charts can confuse or mislead. Scrutinize, ask questions, and give feedback to your authors if you are not sure what a chart is attempting to convey.

### One: Know the elements of charts

Most charts you read and use in Tableau have common characteristics. Read below to understand each element.

![[gDNLNPiOis88Dt0p_IBxsxiYgodISOEMC.jpg]]

**Quantitative Axis:** In Tableau, quantitative fields (usually measures) create an axis that shows the range of values for the measure.

**Qualitative Axis:** Qualitative fields (usually dimensions), create an axis with headers when added to the view. The header has labels for the categorical data. 

**Labels**: These labels describe the product each bar represents.

**Mark:** Mark is the term used to describe the visual representation of the data. In this chart, the mark is called a *bar*.

**Tooltip:** In Tableau, when you click a mark, you can get more specific details about the data the mark represents.

**Filter:** In Tableau, you can click on a filter to view a specific subset of data. This filter allows you to view the data for All markets, or, just the data for a specific market, like USCA.

### Two: Ask questions
You are looking at charts to get insight from your data. Use these questions as guides when you are reading the charts and dashboards your organization produces.

**What does this chart represent?
- Does the chart or dashboard have a clear title and purpose?
- Can you understand the chart's intent in a few moments?

**Does this chart show any particular patterns or trends?**
- Can you see trends in seasonality (example: every November sales rise)?
- Does your data have any *outliers-data points that stand out as very different from the rest of the data-that should be reviewed or explored more closely?*

**Is this all of the data?**
- Does it look like the author deliberately excluded or hid relevant data?
- Can you answer all of your questions with what you see, or do you need more data?

**​Is it clear what has been measured, and what the numbers represent?**
- Has the author included helpful notes, labels, and navigational hints?
- Can you gather useful and actionable data from this chart?

### Three: Watch for misleading or confusing charts
When viewing charts, pay attention to the following items, as they are susceptible to design choices that mislead readers. Here are three examples.

**Bar charts with an axis not including zero (0)**
An axis without a zero can be misleading on a bar chart, as it can distort the scale of differences between categorical data.

![[RPF2DaUMuH0QbEfW_5AzKKc7V9IJhbQEz.png]]
The axis in this chart has been fixed at $390,000. The bars suggest a large discrepancy in shipping costs.


![[s7eE4Ggs1A9qFRxb_Y7IUQI-66ebQowYD.png]]
When this axis is set to zero, you can see there isn't really a large discrepency in shippung costs between categories. 


**Color confusion**
Color is an effective tool for drawing attention to or differentiating areas of data, but can cause confusion if not used carefully. For example, we usually associate density in maps with a darker color, but if the author reverses the color range, that can be confusing, and even misleading.

![[9XCylK2bHfuarBQq_j568VZcH7gdxbI6f.jpg]]

If you looked quickly at this map of airplane wildlife strikes, you might miss that the lighter shades indicate more strikes, not fewer.

![[dOPeRKGDNWsE9-c2_3t-r0j-Np65l45Jl.jpg]]

With the color range set to the usual conventions about density, the map is much clearer.

**Wrong chart type for the data**
Not all chart types work for the selected dimensions and measures.

![[mz3ntNaKEOGMviqd_HLOgXgtjcU-cMSnp.png]]
***This line chart is not the best for comparing data across categories.***

![[4JnS20kCTk74fC86_l_sdoLJu-0FqqZSJ.png]]
***A bar chart is better for comparing data across categories.***

## Chart types and their uses


> [!example|callout_quote] Quote
  > Charts are most effective and readable when matched to the right data and purpose.

![[Screenshot 2025-11-29 at 3.31.44 PM.png]]

**Line:** View trends in data over time.
*Example:* stock price change over a five year period or website page views during a month

**Bar:** Compare data across categories.
*Example:* Volume of shirts in different sizes, or percent of spending by department

**Heatmap:** Show the relationship between two factors.
*Example:* Segment analysis of target market, or sales leads by individual rep.

**Highlight Table:** Shows detailed information on heat maps.
*Examples:* The percent of a market for different segments, or sales numbers in a region.

**Treemap:** Show hierarchical data as a proportion of a whole.
*Examples:* Storage usage across computer machines, comparing fiscal budgets between years.

**Gantt:** Show duration over time.
*Examples:* Project timeline, duration of a machine's use, availability of players on a team.

**Bullet:** Evaluate performance of a metric against a goal.
*Examples:* Sales quota assessment, performance spectrum (great/good/poor).

**Scatterplot:** Investigate relationships between quantitative values. 
*Examples:* Male versus female likelihood of having lung cancer at different ages, or technology early adopters' and laggards' purchase patterns of smart phones.

**Histogram:** Understand the distribution of your data. 
*Examples:* Number of customers by company size, student performance on an exam, frequency of a product defect.

**Symbol Maps:** Use of totals rather than rates. Be careful, as small differences will be hard to see.
*Examples:* Number of customers in different geographies.

**Area Maps:** Use for rates rather than totals. Use sensible base geography. 
*Examples:* Rates of internet-usage in certain geographies, house prices in different neighborhoods.

**Box-and-Whisker:** Show the distribution of a set of the data.
*Examples:* Understanding your data at a glance, seeing how data is skewed towards one end, identifying outliers in your data.

## Bar Charts: Comparing categories of data
A bar chart is used to compare data across categories. Just like the cross-tab, bar charts are a very recognizable chart type, and if done well, are easy to read and interpret.

- The length of the bars tells you which category has the highest value.
- The axis of the bar chart indicates what that value represents.

Here's an example of sales across product categories.

![[1QizASK0yBVMSzBC_TBDkJfRFp6-FLpMt.png]]
***Bar chart showing sales by product category for 2012-2015.***

Sometimes, _if the bar chart is clear and_ _labeled_, the author removes the axis header to reduce visual clutter. In Tableau, an author might do this if the intention is to use the chart as a filter for other data, or to provide a high-level status. When you see a bar chart without an axis, ask:

- Is the chart labeled clearly?
- Can I determine the range of values?

![[Screenshot 2025-11-29 at 3.42.00 PM.png]]

**Hidden axis:** the axis was hidden because the labels provide enough information to the customer. Simplifying the view improves readability, and reduces wasted screen space. 

**Values as labels:** The bars, known as marks in Tableau, each display the total sales for the product category the bar represents. This value updates if the data behind the chart is refreshed.

### What can you learn from the following bar chart?

![[yRVvyp5Jt3MZaVbE_6igl9e5gKGBBBAj6.png]]
***This chart shows the profit rates of different product categories.***


> [!example|callout_purple_notepad] According to the axis, what is the approximate range of values in this chart? 
> -10% to 25% is the range of possible values for profit ratios in this chart.


> [!example|callout_purple_notepad] What does the legend describe?
> How to read the colors in the chart: gray for profitable, and orange for unprofitable. 

> [!example|callout_purple_notepad] Which products are most and least profitable, and what is the average profit ratio across all products? 
> Paper is most profitable and tables are least. The profit ratio across all products is 13%.


## Line Charts: Viewing data over time
### Looking for trends over time
Line charts are especially useful for viewing changes in data over time. Are sales going up or down, and by how much? Are there seasonal trends? 

A line chart can include a single set of values, like this chart below showing monthly sales for an office supply company over the course of a single year:

![[1vfkZi-dTvY7_RN0_GJ-r9_AvLF7F0-YB.png]]
***Monthly sales during 2012.***

What can you learn from this chart? You can see that sales generally increased, and were higher at the end of the year than at the beginning. You can see how sales varied throughout the year: sales fell in the summer months, particularly in July, but then rose again in September, and then rose again at the end of the year. 

This chart show sales for the entire company, which sells lots of products to different customer groups. Do your insights apply equally to all customer groups? How can you tell? 

Remember that a line chart isn't limited to a single line. You can add additional categories (or _dimensions_) to the view to gain additional insight about your data. What happens when you add a dimension like **Consumer Segment** to the view?

![[FkG0RrvSb6W6Xb9I_ChaS9MTrcvXltWQX.png]]
***Same data from the earlier chart, now showing detail according to customer segment.*** 

This view includes the exact same data as the one before it, but now it's broken down by Segment. You can see that the Consumer segment in blue had a big increase in sales in September, perhaps because of school resuming during that time. Corporate sales in orange had a big increase at the end of the year, perhaps due to budget or procurement requirements. By adding dimensions, you can see additional details about your data that weren't apparent before.

When you are looking at a line chart, watch for the following:

- When do trends rise and fall?
- Do any of the data allow you to identify or predict future trends?
- Pay attention to the axis - What is the typical range of values? Are the intervals uniform?
- What is the timeline: yearly? monthly? daily? Does the chart show the right amount of detail for your analysis?


## Scatterplots: Viewing data relationships and outliers

> [!example|callout_quote] Quote
> Use scatterplots to determine correlation between two measures. Correlation refers to a relationship between two or more things. 

If you've seen a chart with a lot of dots spread across it, chances are you were looking at a _scatter plot_. Scatter plots are useful when you want to examine the relationship between two measures or quantitative values. Is there a correlation between them, and if so, to what extent?  

For example, does a person's height correlate to their weight? Does the size of a house determine its price? Does the temperature outside affect ice cream sales? All of these questions could be analyzed by using scatter plots.

![[VEGy8khoKNr6S8IW_HG8wKcENGWseXgnG.png]]
***A scatter plot showing how marketing expenses correlate to sales of coffee and tea.*** 

In the scatter plot above comparing marketing expenses with sales, you can see a positive correlation between the two measures: in general, the more spent on marketing, the more sales can be expected.

> [!example|callout_tip] Tip:
> You may have heard the phrase, "correlation does not mean causation." When you find a correlation between two data points, you can't assume with certainty that one event causes the other without additional data and observation. Correlation between variables means a relationship exists, but *causation* indicates one actually causes a change in the other.

![[Screenshot 2025-11-29 at 4.17.16 PM.png]]

**Positive Correlation:** high or low values in the variables show similar trends. 
*Example:* as sales increase, profits also increase. 

**Negative Correlation:** high or low values show opposing trends. 
*Example:* as prices increase spending decreases.

**No Relation:** values in the variables show no apparent relationship. 
*Example:* size of headphones compared with price of headphones

### Outliers
Even when a correlation is shown in a scatter plot, sometimes there may be values that diverge from the trend, known as _outliers_. 

Outliers can be interesting and should be investigated so you know how to interpret them. Are they rare exceptions that can be disregarded? Or an indication of something to examine more closely? Or maybe they're simply errors in recording or transcription? To be sure, examine the underlying data to make your determination.

![[HF4RUODSBwVVIuXa_NSJ6guRu5wXkvRsv.png]]

In the example above, you can see a general positive correlation. As marketing spending increases, there is generally an increase in sales associated with it. 

However, notice the one outlier present, where significant marketing spending had a much lower impact on sales than might be expected. Why? In this example, the location represented by the mark is in a college town. Is it possible that the marketing was not effective for the student demographic? Perhaps.

### Questions that lead to viewing correlations
When deciding whether you need a scatter plot, consider the following questions:
- Will the user be interested in whether a variable increases or decreases with the changes in another variable?
- Will the user be interested in determining whether a change to one variable has an effect on another variable and what that effect is?
- Will the user need to know how closely a variable follows the changes to another variable?


## Practice activity: Can you escape the room?
You have learned about the basics of data, and how to read and understand different chart types. Here's an activity that guides you through viewing data visualizations in Tableau.

Access the Tableau Escape Room dashboard on Tableau Public (press the orange **Escape the Room** button below). Follow the instructions to see if you can successfully find the data answers required to escape the room.

`BUTTON[escaperoom]`

```meta-bind-button
label: Escape Room
icon: "home"
hidden: true
class: outside-buttons-center
tooltip: ""
id: escaperoom
style: primary
actions:
  - type: open
    link: "https://public.tableau.com/app/profile/mark.bradbourne/viz/EscapeRoom/CanYouEscape"

```



`BUTTON[previous, next]`
