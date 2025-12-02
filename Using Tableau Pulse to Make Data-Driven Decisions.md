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
course id:
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
label: "Next: Get Started in VS Code"
icon: "arrow-right"
hidden: true
class: worksheet-button
tooltip: ""
id: "next"
style: primary
actions:
  - type: open
    link: "[[Get Started in VS Code]]"

```
```meta-bind-button
label: "Previous: Get Started in VS Code"
icon: "arrow-left"
hidden: true
class: navigation-buttons
tooltip: ""
id: "previous"
style: primary
actions:
  - type: open
    link: "[[Get Started in VS Code]]"

```
# Using Tableau Pulse to Make Data-Driven Decisions
---
## What is Tableau Pulse?
Available in Tableau Cloud, Tableau Pulse, is a reimagined data experience. It gives you instant access to the metrics that are most important to you, and it delivers smart, AI-driven data insights about those metrics. And because Tableau AI is built on the Einstein Trust Layer, your AI-powered experiences have a trusted and ethical foundation.

Tableau Pulse helps you see, understand, and act on your data. Imagine receiving a digest personalized to your work, with an automated summary directing your focus to what matters. Then, you dig deeper into the details of specific metrics to see and understand what's happening. Next, with automated key driver analysis, you can understand why things are off track, and if you have lingering questions, you can ask and get answers to them–all in natural language. Finally, you can share your findings to get everyone on the same page to figure out the best next step as a team.

You can see metrics and insights on your Tableau Pulse home page, as pictured in the following example, and you can receive personalized digests about your metrics in tools that are already part of your workflow, reducing the time from insight to action.

![[Final_result_follow.jpg]]

In this lesson, you'll see how Tableau Pulse can help users in an organization, and then you'll learn about the components of Tableau Pulse, and how they work together to deliver personalized, contextual, and smart analytics.


> [!example|callout_tip] Note:
> In this module, we will use the term _business user_ for stakeholders, decision makers, and anyone else in your organization who wants to make decisions based on data.  
> 
> Our developers are busy adding exciting new features and functionality to Tableau Pulse, and even updating its look, at a rapid pace. This module may not reflect all currently available features or all current aspects of the Tableau Pulse user interface (UI).


#### Review the benefits of Tableau Pulse
Tableau Pulse delivers a personalized, contextual, and smart analytics experience.

**Personalized**
Tableau Pulse is personalized to help you transform outcomes with the metrics that matter to you.
- Tableau Pulse guides you to insights you can immediately understand and act on. Digestible insight summaries ensure that you never miss an important trend. Metrics contain the essential context you need, such as a metric's current value, how it is trending, and how it compares to previous periods. 
- Tableau Pulse provides personalized digests composed of the metrics you follow, so the data you care about is always at the forefront. 
- You can also slice and dice existing metrics further to suit your individual needs.

**Contextual**
Tableau Pulse is contextual, helping you access relevant data within your flow of work.
- Tableau Pulse brings metrics and insights to you in the tools you already use, such as Slack and email.
- Because data is right in collaboration tools, you can easily share and discuss data in context, and make swift, data-driven decisions as a team.
- Across applications, you get a reliable view of your data. Tableau Pulse's metrics layer serves as a single source of truth maintained by analytics professionals, keeping metrics consistent across downstream assets.

**Smart**
Tableau Pulse is smart, helping you identify and communicate insights with AI. Here's how:
- Tableau Pulse automates the analysis of metrics to answer common business questions.
- Tableau Pulse's insights platform automatically detects hidden drivers, trends, contributors, and outliers for metrics you follow to proactively notify you of unusual changes.
- Tableau Pulse summarizes detected insights in natural language, supported with visual explanations so you can quickly understand what was found and take appropriate action.
- Tableau Pulse's conversational experiences help you interact with metrics on-demand by proactively recommending follow-up questions you may be interested in to guide you to answers you need.

#### Understand Tableau Pulse architecture
Now that you have a sense of Tableau Pulse's benefits, let's look at an overview of the three main components of Tableau Pulse:
- Metrics layer
- Insights platform
- Next-gen experiences

Generative AI enhances each layer of Tableau Pulse, making it easier for all users to discover relevant metrics, create metrics from existing content, understand insights, ask questions, conduct root cause analysis, and tie data to a real-world context.

![[Architecture.jpg]]

#### Metrics layer
The _metrics layer_ enables metrics to be defined once and then used across an organization, keeping core metric definitions consistent, so the data you see is always reliable.

Every scoped metric is based on a metric definition. An analyst in your organization uses Tableau Pulse to define metrics for your company's published data sources based on relevant organizational KPIs. These definitions serve as a single source of truth for your most important data. The metrics that are scoped, or related, to a metric definition are customizations so that the data is relevant to business users' areas of interest.

An analyst in your organization first defines metric definitions based on KPIs that are relevant. For example, in the previous scenario, Kendra followed metrics in order to receive email digests to alert her to changes or trends in call center wait time. An analyst would first have defined a metric to show callers' average wait times by hour of day and agent across a specific time range. 

Metric definitions are applied at the data source level, so each metric is a single source of truth, ensuring consistency. Additionally, when an analyst updates a metric definition, these updates propagate to all related metrics, so the metrics you follow are always the truth.

See the _Creating and Configuring Tableau Pulse Metric Definitions_ eLearning module for more details on how analysts can create metric definitions using Tableau Pulse.

#### Insights platform
The _insights platform_ runs on top of the metrics layer. This statistical service detects and communicates insights from the data in the metrics. These automated insights appear in visual and natural language explanations, and help you to understand what's happening in your data.

We saw some examples of the insights platform in action during Kendra's scenario. Now let's look at some other examples, this time using data about donations made to a non-profit organization.

**Insight summaries**
The insights platform uses generative AI to summarize top insights from your metrics into a narrative. These insight summaries help you focus on important patterns, trends, outliers, and changes across all the metrics you follow.

You can see the generative-AI powered insight summaries at the top of the Tableau Pulse digests you receive in tools, including email or Slack, and at the top of your Tableau Pulse home page. 

In the following example, we see a Tableau Pulse home page with an insight summary about donations at the top. The summary draws focus to a decline in yearly and weekly donations despite an increase in monthly donations.

![[Final_result_follow_2.jpg]]


**Metric cards**
Similar to the metric thumbnails in an email digest, on your Tableau Pulse home page, you'll see a thumbnail, or _metric card_, for every metric you follow. The metric cards contain automated numeric and visual explanations and a top natural language insight about that metric.

In the following example, we see three metric cards for total donations: one for the year to date, one for the month to date, and one for the week to date. On each card, we see a numeric explanation of the total donations for that time period and its comparison to the previous, similar time period above the visual explanation. Below the visual explanation, a top natural language insight displays.

![[Final_result_follow_3.png]]

**Insights exploration: Overview**
Select a metric card to open that metric's insights exploration page, where you can understand the metric at a glance, including:

- The current metric value.
- The percentage change from the prior period being compared.
- Filters applied to the metric definition.
- Natural language insights about that metric.

The **Overview** tab provides automated numeric and visual explanations of current trends in the data, and the natural language insights help you to understand those trends. If Tableau Pulse detects unusual patterns, changes, or new trends related to the metric, additional visualizations and insights may also appear.

In this example, we see a metric that tracks monthly total donations. At the bottom of the page, a second natural language insight and visual explanation show a steadily increasing trend in total donations over the past 18 days.

![[Top_insight_viz.jpg]]

**Insights exploration: Breakdown**
The **Breakdown** tab on the insights exploration page allows you to slide and dice a metric to see which associated dimensions are impacting the data. 

For example, in the breakdown of the non-profit metric, we can see which campaigns are the highest contributors to our overall donations.  

Note that the additional visualization and explanation about the top insight also display on the **Breakdown** tab.

![[Breakdown_page_2.jpg]]

**Guided follow-up questions**
The insights platform also provides interactive, guided follow-up questions based on the data's context. These questions display on both the **Overview** and **Breakdown** tabs of a metric's insights exploration page. 
  
In this example, the visualization and natural language insight answer the user's question: **What is the trend?**

![[Trend_question_2.jpg]]


> [!example|callout_tip] Note:
> Tableau AI must be turned on by your Tableau admin for insight summaries to be available.

#### Next-gen experiences
_Next-gen experiences_ deliver intuitive metrics in your flow of work, for example in Slack or email, so that you keep up to date on relevant metrics. These digests provide a simple, curated, newsfeed-like experience of the metrics you select.


> [!example|callout_tip] Note:
> We'll take a look at how to follow metrics, and how to access and interact with Tableau Pulse digests, the Tableau Pulse home page, and a metric's insights exploration page later in this module.

###



## Find, follow, and share metrics

## Interact with metrics and create related metrics

## Try it! Use metrics to track important data


























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
