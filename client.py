from pyrogram import Client, idle, ContinuePropagation
import traceback, time, dns.resolver 

class app(Client):
	config_id	= -1001328058005
	katsu_id	=  600432868
	id 				= 1658522481
	username 	= 'maine_handwrittenbot'

	switch = True

	def run_custom(self):
		self.start()
		self.turn_on()

		idle()
		
		self.stop()

	@staticmethod
	def decorator(func):
		def wrapper(app, msg):
			if app.switch:
				try:			
					func(app, msg)

				except Exception as error:
					app.send_error(msg, error, traceback.format_exc())
				
				raise ContinuePropagation

		return wrapper
			
	def msg_del(self, msg):
		bot = self.get_chat_member(str(msg.chat.id), 1661588818)
		if bot.can_delete_messages:
			self.delete_messages(str(msg.chat.id), msg.message_id)

	@staticmethod
	def id_formatter(msg):
		txt = '**Bot:** __@hanekawa_nyanbot__'
		txt+= f'\n**Chat:** __{msg.chat.title}__'
		txt+= f'\n**Chat ID:** __{msg.chat.id}__**/**__{msg.message_id}__'
		user= msg.from_user
		txt+= f'\n**User:** __{user.first_name} __'
		txt+= f'__{user.last_name}__'			if user.last_name is not None else ''
		txt+= f'__ (@{user.username})__'	if user.username  is not None else '' 
		txt+= f'\n**User ID:** __{user.id}__'
		if msg.text is not None:
			txt+= f'\n**Text:** __{msg.text.html}__'
		if msg.media is not None and msg.media:
			if msg.audio is not None:
				txt+= f'\n**Audio ID**: __{msg.audio.file_id}__'
			elif msg.document is not None:
				txt+= f'\n**Document ID**: __{msg.document.file_id}__'
			elif msg.photo is not None:
				txt+= f'\n**Photo ID**: __{msg.photo.file_id}__'
			elif msg.sticker is not None:
				txt+= f'\n**Sticker ID**: __{msg.sticker.file_id}__'
			elif msg.animation is not None:
				txt+= f'\n**Animation ID**: __{msg.animation.file_id}__'
			elif msg.video is not None:
				txt+= f'\n**Video ID**: __{msg.video.file_id}__'
			elif msg.voice is not None:
				txt+= f'\n**Voice ID**: __{msg.voice.file_id}__'
			elif msg.video_note is not None:
				txt+= f'\n**Video note ID**: __{msg.video_note.file_id}__'
			if msg.caption is not None:
				txt+= f'\n**Caption**: __{msg.caption}__'

		return txt

	def send_error(self, msg, error, traceback):
		txt = '**Error occured in message:**\n\n'
		txt+= self.id_formatter(msg)
		txt+= f'\n**Error:** ```{str(error)}```'
		txt+= f'\n**Traceback:** ```{str(traceback)}```'

		self.send_message(app.config_id, txt)
		self.forward_messages(app.config_id, msg.chat.id, (msg.message_id,))

	def turn_on(self):
		self.bot = self.get_me()

		txt = f'**Turned on bot:**'
		txt+= f'\n**User:** `{self.bot.first_name}`'
		txt+= f'\n**Username:** `@{self.bot.username}`'
		txt+= f'\n**User ID:** `{self.bot.id}`'
		txt+= f'\n**Time:** `{time.strftime("%y/%m/%d %H:%M:%S", time.localtime())}`'
		txt+= f'\n**IP:** `{self.find_ip()}`'

		self.send_message(app.config_id, txt)


	@staticmethod
	def find_ip():
		resolver = dns.resolver.Resolver(configure=False)
		resolver.nameservers = ["208.67.222.222", "208.67.220.220"]
		return resolver.query('myip.opendns.com')[0]