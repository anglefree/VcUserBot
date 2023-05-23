
# FILES BELONGS TO @TEAMOCTAVE

import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploys
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("7719901"))
API_HASH = os.getenv("b4664923b5c8a18342b288377f7eb01e")
SESSION = os.getenv("BAB1y90An14Vhon07NjTOJTuWLvscsOHOiWkIf2MCGZ0OvsbI51kME_G4-9rdSG_SP9EiWHsxf5iuyM5RKiQ3KYSiFyc2fT69BiLg7dZ1TivdoR49nImqEI_QVJ2WTrtygQOdypn5Vo9G_kNZuNkUODcv3ikQ3X7631-eQ9BiiWfoN1WkmmFjziOq6EDWu36yrhVu0fEPge5DdnGBqRDrMRcdLJfv9f_NxrT7pdDyUDwXjyD8ZhvMJY893Q_5EfZmA_U8fLtHm7o9bjDrth3U1PgWG_RM0q8kec8A_4hDm1zsrncvZQSFj0Wg3KRPeKv_lrQdrcCfUPNTo6ikx4GwGXBvzOTvAAAAAB1LcJSAA")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("1158888206").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Userbot"))
call_py = PyTgCalls(bot)
