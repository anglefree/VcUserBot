
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
SESSION = os.getenv("SESSION","BAC6q0IASghjo_4xEbYrAN_f9v-LbB1Uoj6oRiHU801JnpsDlNAwrjo9b0tf7G9FsfIGi2dn85_4j4-8huEal5orXEGTRa021p2_xrN3irQMfaMlL528ScOp7tkJrBkPEGc25RvcXTClK52DqIX9JbPZHei7Fxi8CiZtBeNC3n3VfRCKtV7qUe_erBXCVVEgdQ4g4dMB76s9xQNdyaL1OKK4bnl3HpNxPqGbg01bj_Je1d6XZ6CZgRLY_c7vspUf0NmBQj2P5DeWIwb67XjO_JHIEnU9U2BebhVQkO5g9IYXzTuQICuekyiYLc4z05WWDH_wgoolxtS7Mdm3wq5DbTnFWsH8UgAAAAB_nb_6AA")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("1158888206").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Userbot"))
call_py = PyTgCalls(bot)
