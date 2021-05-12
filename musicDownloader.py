import youtube_dl,os

def GetTitle(url):
    with youtube_dl.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url,download=False)
        _title_=str(info_dict['title'])
        if '/' in _title_:
            portion=_title_.split('/')
            titleWithoutSlash=''
            for i in portion :
                titleWithoutSlash+=i
            return titleWithoutSlash
        return _title_

class dataDownload:
    # Get audio
    def GetAudio(self,url,f='bestaudio/best'):     
        audioSavePath = os.path.dirname(__file__) + '\\music\\'+GetTitle(url)+".%(ext)s"
        ydl_opt={
            'format' : f,
            'outtmpl' : audioSavePath
        }
        with youtube_dl.YoutubeDL(ydl_opt) as ydl:
            ydl.download([url])



# Test

# url=input('test url > ')
# GetTitle(url)