from pytube import Playlist
from musicDownloader import dataDownload

# https://www.youtube.com/playlist?list=PL2IQ9gXsrDmLtkr5p0Bgg1JKdTTZNS1C1

class urlParser:
    def parser(self,url):
        if 'youtube' not in url:
            print('Invalid url')
            return
        if 'playlist' in url:
            for video_url in Playlist(url).video_urls:
                a=dataDownload()
                a.GetAudio(video_url)
            return
        else:
            a=dataDownload()
            a.GetAudio(url)
            return
            
                
                

# Test

# url=input('url > ')
# a=urlParser()
# a.parser(url)
