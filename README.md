# Data analysis of the podcasts on iTunes platform

### Author: Andrii Zhurba
The relevant project is located in src directory, PodcastAndalysis.ipynb file.
Likewise, we created a dashboard in the Looker Studio. To view it, visit the following link: https://lookerstudio.google.com/reporting/3aa49f84-0fc8-490d-829a-60dea0b123c2


In this analysis, we thoroughly examine the 
podcasts available on the iTunes platform. 
We have data on the podcasts, their genres, 
and user reviews. Our analysis focuses on various
metrics, including ratings, the number of reviews, 
and their frequency in the dataset, to identify 
interesting podcasts and genres.


## Results:
Our analysis of iTunes podcasts reveals key trends and insights. The most frequent genres are Society-Culture, Education, Comedy, Religion-Spirituality, and Business, while volleyball, mathematics, chemistry, and physics are least frequent. Diverse podcasts like Pursue Excellence, Frazerrice.com, and Beyond Retirement have perfect ratings but low popularity. Crime Junkie dominates with significantly more reviews than other podcasts.
The true-crime and kids-family-stories-for-kids genres tend to collect the most reviews. Business podcasts have notably high ratings, while true-crime and news-daily-news have lower average ratings. We observed that higher ratings often correlate with fewer reviews, except for kids-related topics. Reviews peaked midweek, especially on Wednesdays.


### Source:
The data was downloaded on kaggle website: https://www.kaggle.com/datasets/thoughtvector/podcastreviews/versions/28 in the sqlite format. We turned the required tables into separate csv files for our analysis.


To run the notebook, install the following dependencies:

```
pip install -r requirements.txt
```
