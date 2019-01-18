# Client Project: Estimating Neighborhood Affluence with Yelp

<img src="./images/yelp.jpg" width="600" height="400" alt = "Photo courtesy of @eaterscollective on www.unleash.com" />
 
This project was developed for [New Light Technologies](https://newlighttechnologies.com)
- [Shannon Bingham](https://www.linkedin.com/in/shannon-bingham/) and
- [Roy Kim](https://www.linkedin.com/in/roybkim/)

as a part of the Data Science Immersive program with [General Assembly](https://generalassemb.ly) in January 2019.

## Problem Statement
The goal of the project is to estimate the affluence of a neighborhood based on the number of `$` of businesses and services (according to Yelp) in a given neighborhood (`$`, `$$`, `$$$`, `$$$$`). The project takes a list of zip codes as input and estimates the wealth of the locality. While traditional methods typically estimate wealth of a locality based on demographic characteristics (e.g. income or unemployment rate), the novelty of this approach is in its use of big data related to commercial activity and cost of product and services as an indicator for affluency.

### Repository Structure
**Folders**
- data : Data files created and needed for project.
- images : Image files that either have been produced by the project for presentation or other images added to presentation.
- notebooks : Notebooks used to gather, analyze, and model with the data.

**Notebooks**  


**Other Files**
- Presentation.pdf: Presentation for Non-Technical Audience

## Executive Summary
### Intro:
The rise of social apps related to commercial activity has given birth to a wealth of data with many applications. One of such social apps is Yelp, and the data collected by Yelp is descriptive of businesses by area and location. Specifically, Yelp uses certain markers (`$`, `$$`, `$$$`, `$$$$`) to indicate the relative cost of the services of a business. Can this data be used to estimate the affluence of a neighborhood, or at least be an added indicator to what is already available?

### Collecting Data:
Our group was tasked with using Yelp data to predict and estimate the economic affluence of a neighborhood. We decided to use the adjusted gross income (AGI) to predict affluency. We also decided to collect location data by zip codes, instead of other options. Therefore, we needed a means to collect both economic and geographic data, as well as the Yelp data. We collected this data through developmer tools (Yelp API) and traditional web scraping. Functions were written to automate the collection of data.

### Feature Engineering and Analysis:
In order to maximize signal from the data, we did some feature engineering based on the dollar amounts and the types of businesses in a zip code. We also took a look at some unsupervised learning with principal component analysis and clustering to see if there were any relationships between the features that could be informative.

### Modeling:
Using our feature engineered data, we ran a couple of models to try to predict the AGI. The best of our models ran at 

{

To add later

}

## Next Steps:
There are a few avenues to take to improve results. 
- First, having full access to the Yelp API is crucial in obtaining the most amount of data. The free version of the API limits the data that can be retrieved. 
- Second, pulling data from other resources, such as the Internal Revenue Service or the US Census, will allow a more informed model. 
- Lastly, building a functional tool by automating the whole process would make our work more accessible and instantly useable.

### Known Issues
- Collecting data from Yelp. Because there is a hard limit on how much data can be collected, our team tackled the issue from a statistician's viewpoint. Firstly, we rejected the open data that was provided by Yelp. We decided that the data was not representative of the whole of the US. Secondly, we chose a specific state (Wisconsin) that, at the time of the writing of this project, was ranked in the middle of all states in terms of average AGI. We then chose 100 random zip codes in the state to retrieve Yelp data for, in hopes that we would capture the trend of the whole. Because of this limitation, we only had about 100 observations (before train-test-splitting) to build our model with. 
- Accuracy of Yelp data. We were finding that some of the data on Yelp was inaccurate. We also questioned whether the Yelp data is exhaustively representative of businesses in an area. Further study of this could be beneficial, as well.
