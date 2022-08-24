# YouTube Viral Video Finder

**Description:** This python script will help you find a list of viral youtube videos based on a keyword and timeframe of your choice. THe results will output the number of views, number of channel subscribers, and a ratio of views to subscibers. I higher view/subscriber ratio will indicated the a video is viral (many more views than subscribers). Additionally the output provide information about the video, such as title, channel name, videoID and channelID.

**Who Is This For:** This python script can be used by YouTube content creators to find video ideas based on other videos that have already gone viral on the platform. 

**How To Use:** Before using the script you will need to obtain a YouTube Data API Key (more info here >> https://developers.google.com/youtube/v3/getting-started )

1. Open main.py in any code editor and insert your YouTube Data API Key on line 9 (where it says "INSERT YOUTUBE DATA API KEY HERE")
2. Set the MAX_RESULTS variable to the maximum number of results you'd like to see (more results = more time). If there are not enough results based on your keyword and timeframe then your results may be less than your max results.
3. Open command line and run main.py >> "python main.py"
4. Follow command line prompts for keyword and timeframe
5. Wait, results will be displayed


