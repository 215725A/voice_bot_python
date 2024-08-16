import json
import discord

from func.voice_vox import *
from func.func import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

json_path = "../settings/settings.json"

read_setting = open(json_path, 'r')
setting = json.load(read_setting)

voice_vox = VOICE_VOX()
process_message_command = [False]

skip_massage = ['!change', '!join', '!leave']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global process_message_command
    if message.author == client.user:
        return
    
    if process_message_command[0]:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        return
    
    await join_voice_channel(client, message)
    
    await leave_voice_channel(client, message)
    
    await change_voice_speaker(client, voice_vox, message, process_message_command)

    if message.content in skip_massage:
        return
    

    if message.author.voice:
        voice_vox.generate_wave(message.content)
        await play_sound(client, message, process_message_command)
client.run(setting['BOT_TOKEN'])