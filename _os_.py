import os,glob,pydub

path=os.path.dirname(__file__)+'/music'

def isDir(filePath):
    portion=os.path.splitext(filePath)
    if portion[1]=='':
        return True
    else:
        return False

def get_mp3_name(file):
    newName=os.path.splitext(file)[0]+'_.mp3'
    return newName

class converter:
    def any_to_mp3(filePath):
        os.chdir(filePath)
        for file in glob.glob('./*'):
            if isDir(file)==False:
                print('Starting to convert '+file+' to mp3 format ...')
                sound=pydub.AudioSegment.from_file(file)
                sound.export(get_mp3_name(file),format='mp3')
                os.remove(file)
                print('Done ...')
            else:
                continue


# a=converter()
# a.any_to_mp3(path)