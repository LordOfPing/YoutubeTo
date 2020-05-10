from pytube import YouTube

def res720(dossier = '720'):
    print(yt.streams.filter(file_extension='mp4',progressive=True).order_by('resolution').desc().first())
    yt.streams.filter(file_extension='mp4',progressive=True).order_by('abr').desc().first().download(dossier,title+'720')


def res1080():
    print(yt.streams.filter(file_extension='mp4',only_video=True).order_by('resolution').desc().first())

    for i in (yt.streams.filter(file_extension='mp4',only_audio=True).order_by('abr').desc()):
        print(i)

    yt.streams.filter(file_extension='mp4',only_video=True).order_by('resolution').desc().first().download('video',title)

    yt.streams.filter(file_extension='mp4',only_audio=True).order_by('abr').desc().first().download('audio',title)

def titre(yt):
    title = yt.title
    title = (((title.strip()).replace(".","")).replace('"','')).replace("'","")
    return(title)




if __name__ == "__main__":

    lien = input('url de la video : ')
    yt = YouTube(lien)
    title = titre(yt)
    res720()
