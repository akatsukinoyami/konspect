#!/usr/bin/python3
from pyrogram   	import Client, MessageHandler, Filters
from re				import search
from conspect		import Conspect
from os				import remove
from bot_help		import bot_help

app = Client("conspect_bot")

def decorator(func):
	def wrapper(msg):
		path = msg.download()
		path = func(msg, path)

		msg.reply_document(path)
		remove(path)
	return wrapper

@app.on_message(Filters.private & Filters.document)
def conspect(app, msg): 
	func = None
	if 	 search('.docx', msg.document.file_name):	func = decorator(Conspect().docx)
	elif search('.txt' , msg.document.file_name):	func = decorator(Conspect().txt)
	if func: func(msg)
		
@app.on_message(Filters.private & Filters.command('font'))
def send_font(app, msg):
	fonts = ('Regular', 'Bold', 'Italic', 'Bold_Italic')
	for font in fonts:
		msg.reply_document(f'fonts/Ебать_{font}.ttf')
	answer = 'Установите эти шрифты в свою систему для правильного отображения.\n\n'
	answer+= '**Для Windows:**\nСкчайте файлы шрифтов.\nНажмите правой кнопкой мыши на файл шрифта.\nНажмите "Установить шрифт".\n\n'
	answer+= '**Для Linux:**\nСкчайте файлы шрифтов.\nСоздайте папку ".fonts" в домашней папке "~/".\nСкопируйте туда шрифты.'
	msg.reply(answer)

@app.on_message(Filters.private & Filters.command('help'))
def send_help(app, msg):
	msg.reply(bot_help)

@app.on_message(Filters.private)
def conspect_text(app, msg):
	path = Conspect().text(msg)
	msg.reply_document(path)
	remove(path)

app.run()