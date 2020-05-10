import ffmpeg

def forma(form,title,where = ''):
    if form == 'mp3':

        vid = ffmpeg.input('720/'+title+'720.mp4')
        stream = ffmpeg.output(vid, where+title+'.mp3')
        stream.overwrite_output()
        ffmpeg.run(stream)

    elif form == 'mp4':

        vid = ffmpeg.input('video/'+title+'.mp4')
        aud = ffmpeg.input('audio/'+title+'.mp4')
        stream = ffmpeg.output(vid,aud, where+title+'.mp4')
        ffmpeg.run(stream)
