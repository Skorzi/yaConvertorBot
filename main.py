from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# TOKEN BOT = TOKEN


# В активном ли состоянии бот?
async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Живой, живой, не ссы, {update.effective_user.first_name}')

trippie = open('example.mp3', 'rb')
# Обработка команды с url, 
# вывод сообщения об ошибке в случае, если команда введена некорректно
async def url(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_audio(trippie, caption='Пока что только триппи')

# Инициализация запуска
def main() -> None:
    app = ApplicationBuilder().token("TOKEN").build()

    app.add_handler(CommandHandler("test", test))
    app.add_handler(CommandHandler("url", url))

    app.run_polling()

if __name__ == '__main__':
    main()
