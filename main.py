from pytube import YouTube
from pytube import exceptions
import ffmpeg
import formatv
import tube


while True:
    lien  = input('url de la video à télécharger : ')
    try:
        yt = YouTube(lien)
        break
    except KeyError:
        print('Veuillez recommencer')
    except exceptions.RegexMatchError : 
        print("ceci n'est pas un lien Youtube")

title = tube.titre(yt)

resolution=''

formatvideo = str(input('mp3 ou mp4 : '))

while formatvideo != 'mp3' and formatvideo != 'mp4':
    print('Mauvaise saisie recommencer')
    formatvideo = str(input('mp3 ou mp4 : '))


if formatvideo == 'mp3':
    pass

elif formatvideo == 'mp4':

    resolution = str(input('720 ou 1080 : '))
    while resolution != '720' and resolution != '1080':
        print('Mauvaise saisie recommencer')
        resolution = str(input('720 ou 1080 : '))
else:
    print('erreur')

if resolution == '720' and formatvideo == 'mp4': 
    tube.res720(yt,title,"./")

elif formatvideo == 'mp3':
    tube.res720(yt,title)
    formatv.forma(formatvideo,title)

elif resolution == '1080' and formatvideo == 'mp4':
    tube.res1080(yt,title)
    formatv.forma(formatvideo,title)