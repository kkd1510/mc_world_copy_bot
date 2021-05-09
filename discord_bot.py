import os

import discord

from copies_manager import list_copies
from runner import Runner, COPIES_DIR

CMD_PREFIX = '!'

DISCORD_TOKEN = "" # Your bot token here
DISCORD_GUILD = 1234567 # Your server ID here


def get_cmd(cmd_name):
    return f'{CMD_PREFIX}{cmd_name}'


CP_RUN = get_cmd('cp_run')
CP_LIST = get_cmd('cp_list')

client = discord.Client()
copies_runner = Runner()

async def run_cmd(message):
    if message.content == CP_RUN:
        await message.channel.send("Starting copy")
        copies_runner.make_single_copy()
        await message.channel.send("Copy is now complete")


    if message.content == CP_LIST:
        copies = list_copies(COPIES_DIR)
        await message.channel.send(f"There are {len(copies)} copies currently")
        await message.channel.send(f"Three most recent copies available:")
        for world_copy in copies[-3:]:
            await message.channel.send(f"{os.path.basename(world_copy)}")


@client.event
async def on_ready():
    guild = None
    for guild in client.guilds:
        if guild.name == DISCORD_GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await run_cmd(message)

client.run(DISCORD_TOKEN)
