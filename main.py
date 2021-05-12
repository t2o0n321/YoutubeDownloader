import parseUrl

if __name__ == '__main__':
    while 1:
        url=input('Youtube url > ')
        if url != '':
            try:
                _parser_=parseUrl.urlParser()
                _parser_.parser(url)
                continue
            except:
                print('Error ...')
        else:
            break
        
    import _os_,os
    path=os.path.dirname(__file__)+'/music'
    os.chdir(path)
    _os_.converter.any_to_mp3(path)
    print('Bye !')
   
# import musicDownloader

# print(musicDownloader.GetTitle('https://www.youtube.com/watch?v=B74nzMu5zKY&ab_channel=%E6%84%9B%E8%93%81AiZhen'))
