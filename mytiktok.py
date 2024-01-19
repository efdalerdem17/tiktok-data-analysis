import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Excel file
excel_file = "/Users/efdalerdem/Desktop/Last 59 days.xlsx"  # Specify the full path to your Excel file
df = pd.read_excel(excel_file)

# Display the overview of the dataset
print("Reviewing the dataset:")
print(df.head())

# Display descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())

# Daily Video Views Plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Video Views', data=df, marker='o')
plt.title('Daily Video Views')
plt.xlabel('Date')
plt.ylabel('Video Views')
plt.xticks(rotation=45)
plt.show()

# Likes
sns.lineplot(x='Date', y='Likes', data=df, marker='o', label='Likes')
# likes graph
plt.title('Daily Likes')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()  
plt.show()


# unique video graph
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Unique Viewers', data=df, marker='o', color='green', label='Unique Viewers')
plt.title('Daily Unique Viewers')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()  
plt.show()

# Daily Profile Views Graph
sns.lineplot(x='Date', y='Profile Views', data=df, marker='o', color='blue', label='Profile Views')
# Graph
plt.title('Daily  Profile Views')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()  
plt.show()

# Total Followers 
followers_file = "/Users/efdalerdem/Desktop/Total Followers.xlsx"  
followers_df = pd.read_excel(followers_file)
print("Reviewing Total Followers dataset:")
print(followers_df.head())
# graph
plt.figure(figsize=(10, 6))
plt.plot(followers_df['Date'], followers_df['Followers'], marker='o', color='purple', label='Total Followers')
plt.title('Daily Total Followers')
plt.xlabel('Date')
plt.ylabel('Total Followers Count')
plt.xticks(rotation=45)
plt.legend() 
plt.show()

# Gender 
gender_file = "/Users/efdalerdem/Desktop/Gender.xlsx"  # Gender dosyanızın tam yolu
gender_df = pd.read_excel(gender_file)

print("Reviewing Gender dataset:")
print(gender_df.head())
gender_df['Distribution'] = gender_df['Distribution'].str.rstrip('%').astype('float') / 100.0

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(gender_df['Distribution'], labels=gender_df['Gender'], autopct='%1.1f%%', startangle=140, colors=['blue', 'pink'])
plt.title('Gender Distribution')
plt.show()

# Spotify 
spotify_file = "/Users/efdalerdem/Desktop/Streaming_History_Audio_2023_7.json"  # Spotify dosyanızın tam yolu
spotify_df = pd.read_json(spotify_file)


print("Spotify Data Review:")
print(spotify_df.tail(30))


print("Basic Statistics:")
print(spotify_df.describe())


total_listening_time = spotify_df['ms_played'].sum()
print("Total Listening Time (in minutes):", total_listening_time / (1000 * 60))


top_songs = spotify_df['master_metadata_track_name'].value_counts().head(10)
print("Top 10 Listened Songs:")
print(top_songs)


spotify_df['ts'] = pd.to_datetime(spotify_df['ts'])
daily_listenings = spotify_df.resample('D', on='ts').size()
plt.figure(figsize=(12, 6))
daily_listenings.plot(kind='bar', color='skyblue')
plt.title('Daily Listening Counts')
plt.xlabel('Date')
plt.ylabel('Number of Songs Played')
plt.xticks(rotation=45)
plt.show()







spotify_ms_played_values = [
    4070, 168920, 190, 190, 170, 140, 0, 920, 190, 220,
    429222, 255426, 191129, 237573, 223643, 323475, 219742,
    20070, 216833, 146000, 251818, 63677, 8410, 146000,
    114000, 83689, 8408, 93000, 111633, 73935
]

spotify_ms_played_values = [value / 1000 for value in spotify_ms_played_values]


tiktok_video_views_values = [
    356, 430, 185, 99, 170, 168, 104, 157, 232, 169,
    177, 1223, 2020, 1110, 687, 314, 172, 103, 1758,
    977, 380, 260, 250, 229, 177, 196, 570, 315, 153,
    455
]


x_values = list(range(len(spotify_ms_played_values)))

# Spotify scatter plot
plt.scatter(x_values, spotify_ms_played_values, color='green', marker='o', label='Spotify Ms Played (Divided by 1000)')

# TikTok scatter plot
plt.scatter(x_values, tiktok_video_views_values, color='blue', marker='x', label='TikTok Video Views')


plt.title('Spotify Ms Played vs TikTok Video Views (Divided by 1000)')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend()
plt.show()
