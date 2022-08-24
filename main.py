import json
import datetime as dt
from googleapiclient.discovery import build

# Max Search Results (0-50 only)
MAX_RESULTS = 10

# INSERT YOUR API KEY HERE
api_key = 'INSERT YOUTUBE DATA API KEY HERE'
youtube = build('youtube', 'v3', developerKey=api_key)

# YouTube API request functions
def youtube_search(MAX_RESULTS):
    search_term = input("Enter a search term: ")

    while True:
        results_timeframe = input(
            "Select a search timeframe\n a) this week\n b) this month\n c) this year\n ")
        if results_timeframe == "a":
            timeframe = str(dt.date.today() -
                            dt.timedelta(days=7)) + "T00:00:00Z"
            break
        elif results_timeframe == "b":
            timeframe = str(dt.date.today() -
                            dt.timedelta(days=30)) + "T00:00:00Z"
            break
        elif results_timeframe == "c":
            timeframe = str(dt.date.today() -
                            dt.timedelta(days=365)) + "T00:00:00Z"
            break
        else:
            print("\nInvalid Selection. Try Again.\n")

    request = youtube.search().list(
        part="snippet",
        q=search_term,
        order="viewCount",
        maxResults=MAX_RESULTS,
        publishedAfter=timeframe,
        type="video",
        regionCode="US"
    )
    response = request.execute()
    return response


def vid_views(vid_id):
    request = youtube.videos().list(
        part="statistics",
        id=vid_id
    )
    response = request.execute()
    return response


def subs(chan_id):
    request = youtube.channels().list(
        part="statistics",
        id=chan_id
    )
    response = request.execute()
    return response


if __name__ == '__main__':
    #Calling the YouTube API search function
    response = youtube_search(MAX_RESULTS)

    #Print results
    print("VIEW RATIO | VIEWS | SUBSCRIBERS | CHANNEL NAME | TITLE | VIDEO ID | CHANNEL ID")

    for i in range(0, len(response['items'])-1):
        try:
            # Get video and channel stats from youtube search object
            video_id = response['items'][i]['id']['videoId']
            video_title = response['items'][i]['snippet']['title']
            channel_id = response['items'][i]['snippet']['channelId']
            channel_name = response['items'][i]['snippet']['channelTitle']

            # Get video views from youtube video object
            vv_response = vid_views(video_id)
            video_views = int(vv_response['items'][0]['statistics']['viewCount'])

            # Get subscribers count from youtube channel object
            subs_response = subs(channel_id)
            subscribers = subs_response['items'][0]['statistics']['subscriberCount']

            # Math to find viral videos
            view_ratio = round(int(video_views) / int(subscribers), 2)

            if video_views > 5000 and view_ratio > 0:
                print(
                    f"{view_ratio} | {video_views} | {subscribers} | {channel_name} | Title: {video_title} | VideoID: {video_id} | ChannelID: {channel_id}")
        except:
            print("YouTube Data API timeout")
