import os

URL = "https://www.youtube.com/playlist?list=UULFHisYTStory"

os.system(f'yt-dlp -N 32 --concurrent-fragments 8 --force-ipv4 -f "bv*[height<=720]+ba/b" {URL}')
