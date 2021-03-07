from plugins.conspect_class	import Conspect
from pyrogram								import filters
from client									import app
import os, re

bot_name = 'maine_handwrittenbot'

@app.on_message(filters.private & filters.document)
@app.decorator
def conspect(app, msg): 
	func = None
	c = Conspect()
	if 	 re.search('.docx', msg.document.file_name): func = c.docx
	elif re.search('.txt' , msg.document.file_name): func = c.txt

	if func: 
		path = msg.download()
		path = func(msg, path)
		msg.reply_document(path)
		os.remove(path)
		

@app.on_message(filters.private & ~filters.command(['font', 'help', f'help@{bot_name}', f'font@{bot_name}']))
@app.decorator
def conspect_text(app, msg):
	c = Conspect()
	path = c.text(msg)
	msg.reply_document(path)
	os.remove(path)

