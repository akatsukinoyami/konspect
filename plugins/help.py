from pyrogram	import filters
from client 	import app

bot_name = 'maine_handwrittenbot'

@app.on_message(filters.private & filters.command(['help', f'help{bot_name}']))
@app.decorator
def send_help(app, msg):
	formats = '".docx", ".txt"'
	bot_auth= 'akatsukinoyami (@nyawoobot)'
	fnt_auth= '(@fgxbturhjd)'

	bot_help = f"""Привет,
Я бот для перевода конспектов в рукописный вид.

Отправь мне файл {formats} или просто текстовое сообщение. 
Я обработаю твой текст и ты сможешь распечатать его на листочке в клеточку и сдать, не писав ничего от руки.
Чтобы все работало правильно, напиши "/font", скачай шрифты и установи в систему.

Автор бота: {bot_auth}.
Авторские шрифты использованы с разрешения автора {fnt_auth}."""

	msg.reply(bot_help)