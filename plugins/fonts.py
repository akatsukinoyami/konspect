from pyrogram.types import InputMediaDocument
from pyrogram 			import filters
from client					import app
import os

bot_name = 'maine_handwrittenbot'

@app.on_message(filters.private & filters.command(['font', f'font@{bot_name}']))
@app.decorator
def send_font(app, msg):

	media_group = []
	for i in ('Regular', 'Bold', 'Italic', 'Bold_Italic'):
		media_group.append(InputMediaDocument(f'{os.getcwd()}/fonts/Ебать/{i}.ttf'))
	
	media_group[3].caption = '''Установите эти шрифты в свою систему для правильного отображения.
	
**Для Windows:**
 - Скчайте файлы шрифтов.
 - Нажмите правой кнопкой мыши на файл шрифта.
 - Нажмите "Установить шрифт".

**Для Linux:**
 - Скчайте файлы шрифтов.
 - Создайте папку ".fonts" в домашней папке "~/".
 - Скопируйте туда шрифты.'''
	msg.reply_media_group(media_group)
