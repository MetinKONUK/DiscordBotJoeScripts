import datetime
import logging
from fileinput import filename
from discord.ext import commands
from discord.utils import get
from random import uniform, randint

logging.basicConfig(filename="logs.txt", level=logging.INFO, format="%(asctime)s %(message)s")
bot = commands.Bot(command_prefix="*")

with open("token.conf") as f:
    token = f.readline()

def ReactionGenerator():
    reactions = ["🐦", "🐧", "🐨", "🐇", "🦄", "🌸", "🌹", "🌻", "🌷"]
    n = len(reactions)
    random_number = randint(0, n)
    return reactions[random_number]

@bot.event
async def on_ready():
    log_msg = "bot initialized"
    print(log_msg)
    logging.info(log_msg)

@bot.command()
async def hello(ctx): #*hello
    reply = "Hi there 👋👋👋 my name is Joe ♥️♥️"
    await ctx.reply(reply)

@bot.event
async def on_message(message):
    if bot.user.id != message.author.id:
        random_number = uniform(0, 100)
        if(0 <= random_number and random_number <= 90):
            reaction = ReactionGenerator()
            await message.add_reaction(reaction)
        await bot.process_commands(message)
bot.run(token)