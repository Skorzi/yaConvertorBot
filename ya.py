from yandex_music import Client

def download_track(id) -> str:
    # Директория для скачанной музычки
    dir_of_music = 'music/'

    # Инициализация клиента Ямузыка
    client = Client('TOKEN').init()

    # Получить детали о треке и сделать из них название для нашего файла
    details_of_track = client.tracks(id)[0]
    full_name_track_info = {'title': details_of_track['title'], 'album': details_of_track['albums'][0]['title']}

    # Получить ссылку на скачивание нашего трека, скачать, записать, вернуть путь
    url_info = client.tracks_download_info(id)[0]
    full_name_track = f'{full_name_track_info["title"]} - {full_name_track_info["album"]}.mp3'
    url_info.download(dir_of_music + full_name_track)

    return dir_of_music + full_name_track
