# Пример ссылки
# https://music.yandex.ru/album/11019866/track/52065784

from dataclasses import dataclass
import requests
# Решил использовать дата классы, хоть тайп хинтинг у меня не везде проставлен
# Но мне нравится, как оно минималистично выглядит
@dataclass
class Ya_parser_url:
    url: str
    track_id: str | bool = False

    # Возможно, что ссылка правильная, однако такого трека не существует
    def check_valid_url(self):
        self.track_id = requests.get(self.url).status_code == 200
        return self.track_id

    # В случае, если прошел проверку функции выше, парсим и находим id трека
    def get_id_track(self) -> str | bool:

        if not self.check_valid_url():
            return False

        split_url = self.url.split('/')

        try:
            if split_url[-2] == 'track':
                self.track_id = split_url[-1]
        except IndexError:
            self.track_id = False

        return self.track_id
    
# Для тестиков
if __name__ == '__main__':
    print(Ya_parser_url('https://music.yandex.ru/album/11019866/track/5206574').get_id_track())
    print(Ya_parser_url('https://music.yandex.ru/album/11019866/track/5206578').check_valid_url())