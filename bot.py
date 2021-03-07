from os import getenv as env
from client	import app

app('handwritten_bot', env('API_ID'), env('API_HASH'), bot_token=env('TG_TOKEN')).run_custom()

