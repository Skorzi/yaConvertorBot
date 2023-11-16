from yandex_music import Client
from yandex_music import DownloadInfo

# TOKEN YA_MUSIC = Token

client = Client('Token').init()
details_of_track = client.tracks('52065784')[0]
full_name_track = {'title': details_of_track['title'], 'album': details_of_track['albums'][0]['title']}
url_info = client.tracks_download_info('52065784')[0]
url_info.download(f'music/{full_name_track["title"]} - {full_name_track["album"]}.mp3')
