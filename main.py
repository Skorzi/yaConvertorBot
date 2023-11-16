from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from yandex_music import Client
from ya import download_track
from url_parser import Ya_parser_url
import os


'''
    Код написан на скорую руку, но я даже немного порефачил
    и есть еще пара файликов, может немного в будущем глаз порадуется.

    Короче, функция тест - для проверки в активе ли, вообще, бот.

    Функция юрл - вызывает функцию парсер, которая реализована в классе,
    ну по приколу можно в будущем еще какую функцию в этот класс запихнуть.
    После чего вызывает функцию скачивания трека, как ток скачается - отправитс
    Ну и после этого удалит трек, чтобы у меня тут на машинке ничего не висело

'''


# В активном ли состоянии бот?
async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Живой, живой, не ссы, {update.effective_user.first_name}')

# Обработка команды с url, 
async def url(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Обрабатываем ссылочку
    track_id = Ya_parser_url(context.args[0]).get_id_track()
    
    #Если трек id найден -> продолжаем, иначе шлем нахуй
    if track_id:
        await update.message.reply_text(f'Жди, спотифайтёнок')
        name_of_track = download_track(id=track_id)
        await update.message.reply_audio(name_of_track, caption='Твой трек')
        os.remove(name_of_track)
    else:
        await update.message.reply_text('Пошел нахуй с такими ссылками')


# Инициализация запуска
def main() -> None:
    app = ApplicationBuilder().token("TOKEN").build()

    app.add_handler(CommandHandler("test", test))
    app.add_handler(CommandHandler("url", url))

    app.run_polling()

if __name__ == '__main__':
    main()
