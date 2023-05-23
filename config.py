
# FILES BELONGS TO @sufiansrk10

import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploys
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID","12233538"))
API_HASH = os.getenv("API_HASH","1140f52873a95287478ab500019370c0")
SESSION = os.getenv("SESSION","BABdzmj3Yp6tapTeNpvF8vUnC5eeR8E5_tlmLo7wqdMpMjTM98l7mpH4baijSBYm1hnswV4aXCOXW6qvu9C657XvfdBg_-7kWM4ZQpaj52ViICS0hnaDosvI9IO0hie8lvNVcaJSkecvkGbxtLuYPU8ab1xpCSHmACgzVTHgR8FvVXGIey2rImpXn7wmqp9AMwa_ZJl0MDGD9AzzcJj9pk43kfQVZbnuyyL75ApGjl17jdxMiQumYb495da_i9MmmzWf2P-UgBvXZFoX8b0_PIIKwSMX56aupi5BePY924ELa2EAXDxyN5T_8x-vqYHj-TL3LgxlXMCF5D8svU4CKVHLf52_-gA")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS","1158888206").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Userbot"))
call_py = PyTgCalls(bot)
