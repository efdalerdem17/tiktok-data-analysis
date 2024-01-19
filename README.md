# my-TikTok-data-analysis

here is the link to my website : https://efdalerdem17.github.io/tiktok-data-analysis/%3C!DOCTYPE%20html%3E.html 

This repository is a data analysis and visualization project that involves TikTok and Spotify user data. TikTok data includes various metrics such as daily view counts, 
like counts, profile visits, etc. It also includes Spotify data, which consists of daily music listening durations.

#motivation
Tiktok is an application that I frequently use , I want to examine how my video views are changing. Therefore, I can make videos that get more views.
The aim of the project is to measure the relationship between creativity and music listening. In this context, I aimed to measure creativity using daily TikTok views.
As creative content increases, my views also increase, and I attempted to understand how this correlates with my music listening habits.



#data source
Before selecting my daily TikTok views, I carefully examined my TikTok data to decide which parameters to use. I analyzed data between November 17, 2023, and January 15, 2024. 
During this process, I reviewed daily video views, likes, unique viewers (those who watched a video on my account for the first time), daily profile views,daily total followers, 
and gender distribution charts.The data for this project comes from my personal TikTok account and my personal spotify account. I collected the data by extracting information from the TikTok app, focusing on the period between November 17, 2023, and January 15, 2024. The data includes various metrics related to daily video views, likes, unique viewers, daily profile views, total followers, and gender distribution.Additionally, I analyzed my daily listening on Spotify in milliseconds using data from the third quarter of 2023.


#findings 
I created a graph to examine the correlation between my daily listening and daily video views. While there are occasional shifts in the graph, it is possible to say that there is a correlation between daily listening time and video views.This partially confirms my hypothesis. However, for complete confirmation, I need to work with larger datasets and test it repeatedly.


#techniques
I utilized Python programming language and various libraries, including Pandas, Matplotlib, Seaborn, and Plotly, for the data analysis. 
The different stages of the analysis involve:

Data Extraction: Reading TikTok and Spotify data from the app and extracting relevant metrics.

Data Cleaning: Handling missing values, ensuring data consistency, and preparing it for analysis.I compared both daily views and daily listening by taking only their common dates. Since daily listening is in milliseconds, it was challenging to compare directly, as there was a significant difference in scale. To address this, I divided it by 1000 to convert it to seconds.

Descriptive Statistics: Understanding the overall trends and patterns in the TikTok data.I noticed that the daily video views have a correlation with daily listening  that can be observed in the data. I have published only this correlation on my website.

Data Visualization: Creating scatter plots, line plots, and pie charts to visually represent different metrics.

Spotify Data Analysis: Exploring daily listening counts on Spotify and comparing it with TikTok metrics.

Hypothesis Statement: Formulating a hypothesis related to the correlation between creativity, TikTok metrics, and Spotify listening.

Web Development: Creating an interactive website to present the analysis, including graphs and findings.



#limitations and future work
I have compared two parameters based on the data from the last month; however, this is not sufficient to validate the hypothesis. More data is needed for verification.
In the continuation of the project, accuracy tests can be performed. Furthermore, a machine learning model could be developed to predict the average views of a video based on the
amount of music listened to.
Ayşe Efdal Erdem
