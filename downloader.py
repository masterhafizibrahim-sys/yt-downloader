import os

url = "https://www.youtube.com/@HisYTStory/videos"

os.system(f'yt-dlp -f "bv*[height<=720]+ba/b" --force-ipv4 {url}')
