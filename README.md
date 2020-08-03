# Election Audit

## Overview of Project

### Purpose
The purpose of the election audit analysis is to determine the winning candidate and the county with the largest turnout as well as providing specific data regarding each county and candidate based on the raw election data. 

## Analysis and Challenges

### Analysis of Outcomes Based on Launch Date
Please refer to the linked txt file for details of analysis results
>[Election Results](analysis/Election_Results.txt)


I performed an analysis of theater outcomes based on their month of launch as depicted in the image above by creating a pivot chart (line graph) in Excel for the Parent Category "theater" and graphing the trend by months to see the number of successful, failed, and canceled theater campaigns in each given month. 

### Analysis of Outcomes Based on Goals
![Outcomes vs Goals](Resources/Outcomes_vs_Goals.png)
>[Contributing Spreadsheet for this Analysis](Kickstarter_Challenge.xlsx.xlsx)

I performed an analysis of plays outcomes based on dollar amount listed in each of the campaign goals. To do this, dollar amounts were grouped in buckets starting with "Less than 1000", "1000 to 4999", and so forth in $5000 increments all the way until "Greater than 50000". I then calculated the Percentage of successful, failed, and canceled campaigns in each bucket. The graphical depiction of the result can be seen above. 

### Challenges and Difficulties Encountered
One particular challenge that I faced was not during the analysis portion of this exercise, but instead in the GitHub section of this week's challenge. I had a lot of issues trying to upload links and images in the readme.md section of the deliverable for this week. Some of the things that I found helpful to overcome these challenges include the following: 

1. [How to Upload Images in GitHub](https://www.youtube.com/watch?v=hHbWF1Bvgf4)

2. [Basic GitHub Syntaxs](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax#links)

## Results

**What are two conclusions you can draw about the Outcomes based on Launch Date?**

Two conclusions I can draw about the OUtcomes based on Launch Date is that, consistent with the rest of the data in the kickstarter file, success rate appears to peak for theater campaigns between the months of May and June and steadily declines thereafter, with the lowest performing month in December. Secondly, there does not appear to be a strong correlation between failed/canceled theater campaigns and the time of year these were launched. 

**What can you conclude about the Outcomes based on Goals?**

Based on my analysis of the plays campaign outcomes based on goals, I noticed that none of the campaigns were canceled; they either succeeded to meet their targets or failed. Additionally, campaigns that were less than $1000 had the highest percentage of success, whereas campaigns greater than $45,000 and less than $49,999 had the highest percentage of failure. Based on this, we can say that, generally speaking, campaigns with lower dollar goals tend to be more successful than campaigns that were very expensive. 

**What are some limitations of this dataset?**

Some limitations of this dataset is that it only looks at a sample of kickstarter campaigns and it may not be representative of the population data. Additionally, the data is skewed to the right with several outliers beyond the normal standard deviation. We do not know what is causing this to happen as we do not know how this data was collected and/or whether there are inherent biases. 

**What are some other possible tables and/or graphs that we could create?**

Other possible tables/graphs we could've looked at is we could have evaluated the data for outliers using the box and whiskers graph. Additionally, we can further evaluate the data based on launch date and goals for specific countries and whether or not the campaign was staff picked. Additionally, instead of launch date, we could have looked at the length of the campaign, and the end date as well. 
