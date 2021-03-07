from pyrogram 	import filters
from client			import app

@app.on_message(filters.command(['on', f'on@{app.username}']) & filters.user(app.katsu_id))
def switch_on(app, msg):
	app.switch = True
	msg.reply('Бот включен.')

@app.on_message(filters.command(['off', f'off@{app.username}']) & filters.user(app.katsu_id))
def switch_off(app, msg):
	app.switch = False
	msg.reply('Бот выключен.')