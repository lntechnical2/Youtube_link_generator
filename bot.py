from pyrogram import Client,filters
import youtube_dl
from pyrogram.types import (InlineKeyboardButton,  InlineKeyboardMarkup)
import os

TOKEN = os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID", "")) 
API_HASH = os.environ.get("API_HASH", "")


app = Client("ytlink",bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH)

@app.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	await message.reply_text(f"👋 Hello {message.from_user.first_name}\n\n Get Link For voice chat From YouTube Send me YouTube link  😁\n\n 😢 Don't Forget to subscribe channel",reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton('Support 🙊',url = "https://t.me/lntechnical")]]))


@app.on_message(filters.regex("^https?:\/\/?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/).{11}"))
async def yt(client,message):
	ms = await message.reply_text("Wait for minutes 👨‍🔧..........")
	ydl_opts = {} 
	url = message.text
	with youtube_dl.YoutubeDL(ydl_opts)as ydl:
		meta = ydl.extract_info(url, download=False) 
		formats = meta.get('formats', [meta])
		linkfor1 = formats[0]
		linkfor2 = formats[1]
		linkfor3 = formats[2]
		link1 = linkfor1['url']
		link2 = linkfor2['url']
		link3 = linkfor3['url']

		await ms.edit(f"""
		Links .................
		[link1]({link1})
		[link2]({link2})
		[link3]({link3})
		
		Join @lntechnical
		
		""")
			
			
app.run()	
	
