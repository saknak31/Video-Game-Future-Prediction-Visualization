import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm.auto import tqdm
from wordcloud import WordCloud

# Load the data
video_games_df = pd.read_csv('video_games.csv', encoding='utf-8')

# Convert release_date to datetime
video_games_df['release_date'] = pd.to_datetime(video_games_df['release_date'], errors='coerce')

# Drop rows with NaT in release_date
video_games_df = video_games_df.dropna(subset=['release_date'])

# Extract year from release_date
video_games_df['release_year'] = video_games_df['release_date'].dt.year

# Plot distribution of user reviews
plt.figure(figsize=(10, 6))
sns.histplot(video_games_df['user_review'], bins=20, kde=True)
plt.title('Distribution of User Reviews')
plt.xlabel('User Review Score')
plt.ylabel('Number of Games')
plt.show()

# Plot number of games released per platform
plt.figure(figsize=(14, 7))
platform_counts = video_games_df['platform'].value_counts()
sns.barplot(x=platform_counts.index, y=platform_counts.values)
plt.title('Number of Games Released per Platform')
plt.xlabel('Platform')
plt.ylabel('Number of Games')
plt.xticks(rotation=90)
plt.show()

# Plot number of games released over the years
plt.figure(figsize=(14, 7))
yearly_counts = video_games_df['release_year'].value_counts().sort_index()
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values)
plt.title('Number of Games Released Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Games')
plt.xticks(rotation=45)
plt.show()

from wordcloud import WordCloud

# Convert 'user_review' column to numeric, setting errors='coerce' to turn non-convertible values into NaN
video_games_df['user_review'] = pd.to_numeric(video_games_df['user_review'], errors='coerce')

# Drop rows with NaN in 'user_review' column
video_games_df = video_games_df.dropna(subset=['user_review'])

# Extract year from 'release_date' and create a new column 'release_year'
video_games_df['release_year'] = pd.to_datetime(video_games_df['release_date']).dt.year


# Calculate average user review score by platform
platform_avg_reviews = video_games_df.groupby('platform')['user_review'].mean().sort_values(ascending=False)

# Plot average user review score by platform
plt.figure(figsize=(14, 7))
sns.barplot(x=platform_avg_reviews.index, y=platform_avg_reviews.values)
plt.title('Average User Review Score by Platform')
plt.xlabel('Platform')
plt.ylabel('Average User Review Score')
plt.xticks(rotation=90)
plt.show()

# Calculate average user review score by year
year_avg_reviews = video_games_df.groupby('release_year')['user_review'].mean().sort_index()

# Plot average user review score by year
plt.figure(figsize=(14, 7))
sns.lineplot(x=year_avg_reviews.index, y=year_avg_reviews.values)
plt.title('Average User Review Score by Year')
plt.xlabel('Year')
plt.ylabel('Average User Review Score')
plt.xticks(rotation=45)
plt.show()

# Generate a word cloud from the summaries of the top-rated games
# Consider games with a user review score of 9 or higher as top-rated
top_rated_games = video_games_df[video_games_df['user_review'] >= 9]['summary']

# Join all summaries into a single text
all_summaries = ' '.join(top_rated_games)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_summaries)

# Display the word cloud
plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Top-Rated Games Summaries')
plt.show()
