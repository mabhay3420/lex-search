from youtubesearchpython import Playlist, Video
import json
from collections import defaultdict

# create a Playlist object for the desired playlist
playlistLink ='https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4'

playlist = Playlist(playlistLink)
print(f'Videos Retrieved: {len(playlist.videos)}')

while playlist.hasMoreVideos:
    print('Getting more videos...')
    playlist.getNextVideos()
    print(f'Videos Retrieved: {len(playlist.videos)}')

print('Found all the videos.')

# playlistVideos = Playlist.getVideos(playlistLink)
# # print(playlistVideos)
# # print(playlistVideos.keys())

lex_video_info = defaultdict(dict)
for i, videos in enumerate(playlist.videos):
    # The link has in the end index=xx . Extract xx
    # Every title ends with #xx extract it
    episodeNumber =  videos['title'].split('#')[-1]
    lex_video_info[episodeNumber] = {
        "title": videos['title'],
        "link": videos['link'],
    }
with open("data/lex_video_info.json", "w") as f:
    json.dump(lex_video_info, f, indent=4)


