from fileinput import filename
import logging
from discord.ext import commands
from discord.utils import get
from random import uniform
from datetime.now import now
from logging import _Level, debug, info, error, DEBUG

logging.basicConfig(filename="logs.txt", level = DEBUG)
bot = commands.Bot(command_prefix="*")

def LogMessage(log_message):
    msg = "{}\n->{}".format(log_message, now())
    return msg

@bot.event
async def on_ready():
    log_msg = LogMessage("bot initialized")
    print(log_msg)
    info(log_msg)

@bot.command()
async def hello(ctx): #*hello
    reply = "Hi there 👋👋👋 my name is Joe ♥️♥️"
    await ctx.reply(reply)


